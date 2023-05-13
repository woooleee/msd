import os 
import sys
from unicodedata import normalize
import os

def DirNFCChange(dirname:str) -> None:
    """
    Especially for MAC OS. Some korean file names saved in MAC OS environment 
    cracks(자모분리현상) normal: '가나', cracked: 'ㄱㅏㄴㅏ'
    This function is for solving crack of korean. Returns nothing
    :param dirname: directory name of which contains cracked korean file names
    :return: None
    """
    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        os.rename(before_filename, after_filename)
    return None