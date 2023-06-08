SSD_PATH = '/Volumes/T7/asset/'

# POPULATION SEOUL COLS FOR GETTING DATA
POPSE_GEN_COLS = [
    "구분별", "동별", "항목", "단위",
    "202001", "202002", "202003", "202004", "202005", "202006", "202007", "202008", "202009", "202010", "202011", "202012",
    "202101", "202102", "202103", "202104", "202105", "202106", "202107", "202108", "202109", "202110", "202111", "202112",
    "202201", "202202", "202203", "202204", "202205", "202206", "202207", "202208", "202209", "202210", "202211", "202212",    
    "202301", "202302", "NN"
]

# CBD CODES
SCG_CD = '11650'
GNG_CD = '11680'
GG_CD = '11140'
JNG_CD = '11110'
YDPG_CD = '11560'

SCBD_CDS = [GG_CD, JNG_CD]
GBD_CDS = [SCG_CD, GNG_CD]
YBD_CDS = [YDPG_CD]

CBD_CDS = SCBD_CDS + GBD_CDS + YBD_CDS

# CBD NAMES
SCG_NM = '서초구'
GNG_NM = '강남구'
GG_NM = '중구'
JNG_NM = '종로구'
YDPG_NM = '영등포구'

SCBD_NMS = [GG_NM, JNG_NM]
GBD_NMS = [SCG_NM, GNG_NM]
YBD_NMS = [YDPG_NM]

CBD_NMS = SCBD_NMS + GBD_NMS + YBD_NMS

# MAINPURPOSE CODE
MAINPURPSCD_IN_INTEREST = ['03000', '04000','07000','14000','15000', '17000', '18000', '20000']



# METRO OD DATA DICT AMEND
keys = [
    '04시-05시 승차인원',
    '04시-05시 하차인원',
    '05시-06시 승차인원',
    '05시-06시 하차인원', 
    '06시-07시 승차인원', 
    '06시-07시 하차인원', 
    '07시-08시 승차인원',
    '07시-08시 하차인원', 
    '08시-09시 승차인원', 
    '08시-09시 하차인원',
    '09시-10시 승차인원',
    '09시-10시 하차인원', 
    '10시-11시 승차인원', 
    '10시-11시 하차인원', 
    '11시-12시 승차인원',
    '11시-12시 하차인원', 
    '12시-13시 승차인원', 
    '12시-13시 하차인원', 
    '13시-14시 승차인원',
    '13시-14시 하차인원', 
    '14시-15시 승차인원', 
    '14시-15시 하차인원', 
    '15시-16시 승차인원',
    '15시-16시 하차인원', 
    '16시-17시 승차인원', 
    '16시-17시 하차인원', 
    '17시-18시 승차인원',
    '17시-18시 하차인원', 
    '18시-19시 승차인원', 
    '18시-19시 하차인원', 
    '19시-20시 승차인원',
    '19시-20시 하차인원', 
    '20시-21시 승차인원', 
    '20시-21시 하차인원', 
    '21시-22시 승차인원',
    '21시-22시 하차인원', 
    '22시-23시 승차인원', 
    '22시-23시 하차인원', 
    '23시-24시 승차인원',
    '23시-24시 하차인원', 
    '00시-01시 승차인원', 
    '00시-01시 하차인원', 
    '01시-02시 승차인원',
    '01시-02시 하차인원', 
    '02시-03시 승차인원', 
    '02시-03시 하차인원', 
    '03시-04시 승차인원',
    '03시-04시 하차인원'
]


values = [
    '0405O',
    '0405D',
    '0506O',
    '0506D',
    '0607O',
    '0607D',
    '0708O',
    '0708D',
    '0809O',
    '0809D',
    '0910O',
    '0910D',
    '1011O',
    '1011D',
    '1112O',
    '1112D',
    '1213O',
    '1213D',
    '1314O',
    '1314D',
    '1415O',
    '1415D',
    '1516O',
    '1516D',
    '1617O',
    '1617D',
    '1718O',
    '1718D',
    '1819O',
    '1819D',
    '1920O',
    '1920D',
    '2021O',
    '2021D',
    '2122O',
    '2122D',
    '2223O',
    '2223D',
    '2324O',
    '2324D',
    '0001O',
    '0001D',
    '0102O',
    '0102D',
    '0203O',
    '0203D',
    '0304O',
    '0304D'
]

DF_METRO_COL_AMEND_DICT = {key: value for key, value in zip(keys, values)}


# GRID DF
GRID_DF_COL = ['ADM_SECT_C', 'geometry', 'idx']


# ENERGY DF
BDELCT = {
    'kr': '국토교통부_건물에너지정보 서비스_지번별 전기사용량 조회(bdelct)',
    'url': 'https://www.data.go.kr/data/15054212/openapi.do',
    'path': 'asset/rawfile/bdelct/',
    'download': {
        'download_url': None,
        'target_dir': 'asset/rawfile/bdelct/'
    },
    'endpoint': None,
    'procure_by': 'download', 
    'gen_key': ['pnu'],
    'gen_col_kr': [
        "사용년월",
        "대지위치",
        "도로명대지위치",
        "시군구코드",
        "법정동코드",
        "대지구분코드",
        "번",
        "지",
        "새주소일련번호",
        "새주소도로코드",
        "새주소지상지하코드",
        "새주소본번",
        "새주소부번",
        "사용량(KWh)"
    ],

    'kr_en_map': {  
        "사용년월": "useYm",
        "대지위치": "platPlc",
        "도로명대지위치": "newPlatPlc",
        "시군구코드": "sigunguCd",
        "법정동코드": "bjdongCd",
        "대지구분코드": "platGbCd",
        "번": "bun",
        "지": "ji",
        "새주소일련번호": "naRoadNum",
        "새주소도로코드": "naRoadCd",
        "새주소지상지하코드": "naUgrndCd",
        "새주소본번": "naMainBun",
        "새주소부번": "naSubBun",
        "사용량(KWh)": "kwh"
    },

    'gen_col_types': {
        "useym": "VARCHAR(6)",
        "platplc": "VARCHAR(500)",
        "newplatplc": "VARCHAR(400)",
        "sigungucd": "VARCHAR(5)",
        "bjdongcd": "VARCHAR(5)",
        "platgbcd": "VARCHAR(1)",
        "bun": "VARCHAR(4)",
        "ji": "VARCHAR(4)",
        "naroadnum": "VARCHAR(6)",
        "naroadcd": "VARCHAR(12)",
        "naugrndcd": "VARCHAR(1)",
        "namainbun": "NUMERIC(5)",
        "nasubbun": "NUMERIC(5)",
        "kwh": "NUMERIC(22)",
        "rlgcd": "CHAR(2)",
        "stdryear": "CHAR(4)",
        "stdrmonth": "CHAR(2)",
        "pnu": "CHAR(19)"
    },
    'save_cols': ['pnu', 'stdryear', 'stdrmonth', 'kwh', 'rlgcd']
}

BDGAS = {
    'kr': '국토교통부_건물에너지정보 서비스_지번별 가스사용량 조회(bdgas)',
    'url': 'https://www.data.go.kr/data/15054212/openapi.do',
    'path': 'asset/rawfile/bdgas/',
    'download': {
        'download_url': None,
        'target_dir': 'asset/rawfile/bdgas/'
    },
    'endpoint': None,
    'procure_by': 'download', 
    'gen_key': ['pnu'],
    'gen_col_kr': [
        "사용년월",
        "대지위치",
        "도로명대지위치",
        "시군구코드",
        "법정동코드",
        "대지구분코드",
        "번",
        "지",
        "새주소일련번호",
        "새주소도로코드",
        "새주소지상지하코드",
        "새주소본번",
        "새주소부번",
        "사용량(KWh)"
    ],

    'kr_en_map': {  
        "사용년월": "useYm",
        "대지위치": "platPlc",
        "도로명대지위치": "newPlatPlc",
        "시군구코드": "sigunguCd",
        "법정동코드": "bjdongCd",
        "대지구분코드": "platGbCd",
        "번": "bun",
        "지": "ji",
        "새주소일련번호": "naRoadNum",
        "새주소도로코드": "naRoadCd",
        "새주소지상지하코드": "naUgrndCd",
        "새주소본번": "naMainBun",
        "새주소부번": "naSubBun",
        "사용량(KWh)": "kwh"
    },

    'gen_col_types': {
        "useym": "VARCHAR(6)",
        "platplc": "VARCHAR(500)",
        "newplatplc": "VARCHAR(400)",
        "sigungucd": "VARCHAR(5)",
        "bjdongcd": "VARCHAR(5)",
        "platgbcd": "VARCHAR(1)",
        "bun": "VARCHAR(4)",
        "ji": "VARCHAR(4)",
        "naroadnum": "VARCHAR(6)",
        "naroadcd": "VARCHAR(12)",
        "naugrndcd": "VARCHAR(1)",
        "namainbun": "NUMERIC(5)",
        "nasubbun": "NUMERIC(5)",
        "kwh": "NUMERIC(22)",
        "rlgcd": "CHAR(2)",
        "stdryear": "CHAR(4)",
        "stdrmonth": "CHAR(2)",
        "pnu": "CHAR(19)"
    },
    'save_cols': ['pnu', 'stdryear', 'stdrmonth', 'kwh', 'rlgcd']
}

# METRO
SEOUL_METRO_NMS = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선', '8호선', '9호선']


# CBD EXPANSION
# Setting COLS
SIM_CAL_COLS = [
    'pp_pop', # X1
    'pp_od', # X2
    'bs_ebit', # X3
    'bs_gas', # X4
    'bs_elct', # X5
    'bd_platarea', # X6
    'bd_archarea', # X7
    'bd_totarea', # X8
    'bd_totflrcnt', # X9
    'bd_elvtent', # X10
    'bd_height', # X11
    'bd_vintage', # X12
    ]

STANDARDIZE_COLS = [
    'pp_pop', # X1
    'pp_od', # X2
    'bs_ebit', # X3
    'bs_gas', # X4
    'bs_elct', # X5
    'bd_platarea', # X6
    'bd_archarea', # X7
    'bd_totarea', # X8
    'bd_totflrcnt', # X9
    'bd_elvtent', # X10
    'bd_height', # X11
    'bd_vintage', # X12
    'bd_ilp' # X13
    ]

PP_COLS = [
    'pp_pop', # X1
    'pp_od', # X2
]
BS_COLS = [
    'bs_ebit', # X3
    'bs_gas', # X4
    'bs_elct', # X5
]
BD_COLS = [
    'bd_platarea', # X6
    'bd_archarea', # X7
    'bd_totarea', # X8
    'bd_totflrcnt', # X9
    'bd_elvtent', # X10
    'bd_height', # X11
    'bd_vintage', # X12
]