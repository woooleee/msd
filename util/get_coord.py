import psycopg2
import yaml
import os
import time
import json
import datetime 
import requests
import pandas as pd
import glob
import sys; sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from requests.exceptions import HTTPError
import pickle
from epsg_transform import coord_tranformation

# Path Generator
def pathGen(endpoint, sggbjd_cd, rn_cd, is_ugrnd, bd_main_cd, bd_sub_cd, resultType):
    """
    Using data values from dataview, func generates url path for querying X, Y coordinate of building.
    We utilize endpoint offered by business.juso.go.kr
    :params : All String(sggbjd_cd, rn_cd, is_ugrnd, bd_main_cd, bd_sub_cd)
    :return : String(url request path)
    """
    return f'{endpoint}admCd={sggbjd_cd}&rnMgtSn={rn_cd}&udrtYn={is_ugrnd}&buldMnnm={bd_main_cd}&buldSlno={bd_sub_cd}&resultType={resultType}' # &confmKey={confmKey}

class GetCoords():
    def __init__(self, logger, worker: str, test: str) -> None:
        self.cfg_path = "../security/security.yaml"
        self.worker = worker
        self.file_path = "../asset/postprocess/"
        self.logger = logger
        # self.pp = PrettyColors(self.logger)
        with open(self.cfg_path, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        self.psqlCfg = data_loaded['Postgres']['login_test']
        self.jusoGoKrCfg = data_loaded['JusoGoKr']
        # self.conn = psycopg2.connect(
        #     host=self.psqlCfg['host'],
        #     database=self.psqlCfg['dbname'],
        #     user=self.psqlCfg['id'],
        #     password=self.psqlCfg['pw'])
    
    def data(self):
        endpoint = self.jusoGoKrCfg["AddrCoordApi"]["endpoint"]
        resultType = "json"

        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path) # Create the directory if it does not exist

        # Access DB and Change from DB to pd.DataFrame
        self.pp.print_ok_green(f"[PostProcess-1]: Connect to DB")
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM bdaddrinfo')
        dataView = cur.fetchall()
        cols = [desc[0] for desc in cur.description]
        self.pp.print_ok_green(f"[PostProcess-1-Success]: Connect to DB")
        all_df = pd.DataFrame(data = dataView, columns = cols)

        # Get Coordinates
        using_cols = ['bd_mgt_cd', 'sggbjd_cd', 'rn_cd', 'is_ugrnd', 'bd_main_cd', 'bd_sub_cd']
        all_df = all_df[using_cols]
        all_df['url_path'] = all_df.apply(lambda row: pathGen(endpoint, row['sggbjd_cd'], row['rn_cd'], row['is_ugrnd'], row['bd_main_cd'], row['bd_sub_cd'], resultType), axis = 1)

        # Divide all df in to 4 dfs and Save 4 pickle files
        df_0 = all_df[all_df.index % 4 == 0]
        df_1 = all_df[all_df.index % 4 == 1]
        df_2 = all_df[all_df.index % 4 == 2]
        df_3 = all_df[all_df.index % 4 == 3]
        df_0.to_pickle(self.file_path + "bdaddr_0.p")
        df_1.to_pickle(self.file_path + "bdaddr_1.p")
        df_2.to_pickle(self.file_path + "bdaddr_2.p")
        df_3.to_pickle(self.file_path + "bdaddr_3.p")

    def get_coords(self):
        work_worknum_map = {
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "3"
        }

        arg_worker = self.worker
        confmKey = self.jusoGoKrCfg["apiKey"][arg_worker]
        todo_file_path = self.file_path + f"bdaddr_{work_worknum_map[arg_worker]}.p"
        
        with open(todo_file_path, "rb") as f:
            acquired_todo_pickle = pickle.load(f)
        todo_df = pd.DataFrame(data = acquired_todo_pickle)     

        xs = []
        ys = []
        bd_cds = []
        save_frequency = 10000 # if this val is 100, for every 100 indexes log file is updated and processed file is saved
        len_data = len(todo_df)

        if self.logger.read(arg_worker)["is_complete"] is False:
            start_i = int(self.logger.read(arg_worker)["is_done_until"])
            for i in range(start_i, len_data):
                time_chk_pt = time.time()
                print(i, arg_worker)
                if i % 10 == 0:        
                    time_to_rest = 5 - (time.time() - time_chk_pt)
                    time_chk_pt = time.time()
                    time.sleep(time_to_rest)

                try:
                    path = todo_df.iloc[i].url_path + f"&confmKey={confmKey}"
                    response = requests.get(path)
                    response.raise_for_status()
                    jsonResponse = response.json()
                    if int(jsonResponse['results']['common']['totalCount']) >= 1:
                        resData = jsonResponse['results']['juso'][0]
                        x = resData['entX']
                        y = resData['entY']
                        xs.append(x)
                        ys.append(y)
                        bd_cds.append(todo_df.iloc[i].bd_mgt_cd)
                        # print(todo_df.iloc[i].bd_mgt_cd, x, y)
                    else:
                        x = None
                        y = None 
                        xs.append(x)
                        ys.append(y)
                        bd_cds.append(todo_df.iloc[i].bd_mgt_cd)

                except HTTPError as http_err:
                    print(f'HTTP error occurred: {http_err}')
                except Exception as err:
                    print(f'Other error occurred: {err}')

                if (i % save_frequency == 0) and (i != 0):
                    save_file_path = self.file_path + \
                        f"bdaddr_{work_worknum_map[arg_worker]}_processed_{i-save_frequency}_{i}.p"
                    log_add = {
                        "todo_file_path": todo_file_path,
                        "is_complete": False,
                        "is_done_until": i
                        }
                    
                    self.logger.update(arg_worker, log_add)
                    data = {'x': xs, 'y': ys, 'bd_mgt_cd': bd_cds}
                    pd.DataFrame(data = data).to_pickle(save_file_path)
                    del xs
                    del ys 
                    del bd_cds
                    xs = []
                    ys = []
                    bd_cds = []

                else: pass

                if i == len_data - 1:
                    log_add = {
                        "todo_file_path": todo_file_path,
                        "is_complete": True,
                        "is_done_until": i
                        }
                    self.logger.update(arg_worker, log_add)
                else: pass

    def coord_transform(self):
        self.file_path = "../asset/postprocess/"
        target_file_pattern = '*_processed_*'
        target_file_paths = list(glob.glob(self.file_path + target_file_pattern))
        xs_all = []
        ys_all = []
        bd_cds_all = []
        
        # Loop through target file path, transform coordinate system file by file.
        # xs_all, ys_all, bd_cds_all contain all transformed data fron multiple files in target_file_paths
        for target_file_path in target_file_paths:
            with open(target_file_path, "rb") as f:
                acquired_todo_pickle = pickle.load(f)
            todo_df = pd.DataFrame(data = acquired_todo_pickle)
            xs, ys = todo_df.x, todo_df.y
            xs = pd.to_numeric(xs, errors = 'coerce').fillna(0)
            ys = pd.to_numeric(ys, errors = 'coerce').fillna(0)
            xs_transformed, ys_transformed = coord_tranformation(xs, ys, "epsg:5179", "epsg:4326")
            assert len(xs_transformed) == len(ys_transformed) == len(todo_df.bd_mgt_cd)
            xs_all.extend(xs_transformed)
            ys_all.extend(ys_transformed)
            bd_cds_all.extend(todo_df.bd_mgt_cd.to_list())  
    
        # Jot down now
        now = datetime.datetime.now()
        today_yyyymmdd = now.strftime('%Y-%m-%d') # e.g., 2012-12-12
        today_yyyymmddhhmmss = now.strftime('%Y-%m-%d %H:%M:%S')

        # Save transformed(followed by processed) data in pickle format
        data = {"x": xs_all, "y": ys_all, "bd_mgt_cd": bd_cds_all}
        pd.DataFrame(data = data).to_pickle(f"{self.file_path}transformed_{today_yyyymmdd}.p")
        pd.DataFrame(data = data).to_csv("fooo.csv")

        # Save meta data of data above
        meta_data = {
            "transformed_file_paths": target_file_paths,
            "transformed_done_time": today_yyyymmddhhmmss
        }
        with open(f"{self.file_path}transformed_file_meta_{today_yyyymmdd}.json", 'w') as file:
            json.dump(meta_data, file, indent=4)

    def insert_to_db(self):
        pass        
        # data = pd.read_pickle
        # if initial:
        #     # If initial create table.
        #     # `self.table_name` table for whole data
        #     self.db.create_table(table_name=self.table_name, variables=self.table_col_types)
        #     self.db.create_pkey(table_name=self.table_name, primary_key=self.p_key)
        #     # `self.table_name + _diff` for delta data.
        #     self.db.create_table(table_name=self.table_name + "_diff", variables=diff_types)
        #     self.db.create_pkey(table_name=self.table_name + "_diff", primary_key=self.p_key)