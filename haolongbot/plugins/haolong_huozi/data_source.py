import re
import os
from pydub import AudioSegment
import pypinyin
from pathlib import Path


def is_chinese(uchar):
    if uchar >= '\u4e00' and uchar <= '\u9fa5':
        return True
    else:
        return False
 
def saveChinese(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str += i
    return content_str


def getSoundFileUrl(js,wavname):
    return Path.cwd().joinpath('haolongbot/plugins/haolong_huozi/'+js+'/'+wavname)
def getHuoZiSound(word,js):
    output_vio =AudioSegment.empty()
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        wavname = i[0]
        if(os.path.exists(getSoundFileUrl(js,wavname+".wav"))):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+".wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"1.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"1.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"2.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"2.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"3.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"3.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"4.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"4.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"01.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"01.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"02.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"02.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"03.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"03.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"04.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"04.wav"))
        elif os.path.exists(getSoundFileUrl(js,wavname+"05.wav")):
            output_vio+= AudioSegment.from_wav(getSoundFileUrl(js,wavname+"05.wav"))
        else:
            return "不存在"+wavname+"请联系管理员添加"
    return output_vio