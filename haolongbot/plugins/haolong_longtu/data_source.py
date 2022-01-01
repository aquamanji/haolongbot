import os
from pathlib import Path
from posixpath import basename
import random
def returnltlist(lx):
    file_dir = Path.cwd().joinpath('haolongbot\plugins\haolong_longtu\\'+lx)
    getfiles =  [files for files in os.walk(file_dir, topdown=False)]   # 当前路径下所有非目录子文件cls
    return getfiles[0][2]
def getrangelist(ltlist,lx):
    return Path.cwd().joinpath('haolongbot\plugins\haolong_longtu\\'+lx+'\\'+random.choice(ltlist))
def getSelectedvalueFile(file,lx):
    return Path.cwd().joinpath('haolongbot\plugins\haolong_longtu\\'+lx+'\\'+file)


def getKeywordsAndFullwords(keyword):
    a = returnltlist(keyword)
    c = {'basename':[],
        'fullname':[]
    }
    for b in a:
        fullname = os.path.basename(b)
        c['basename'].append(os.path.splitext(fullname)[0])
        c['fullname'].append(fullname)
    return c