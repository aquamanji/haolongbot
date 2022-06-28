from PIL import Image
from PIL import ImageFilter
# 需要用到requests库来获取图片地址，用os库打开和写入文件。所以首先要先引用这两个库。
import requests
import os
from pathlib import Path
import random
def msktoimg(url,randomjpgname):
    # url图片的链接
    h={
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    # 定义一个根目录，定义为D盘下的A文件夹。这里的"\\",因为\是转义符，输出'\'要写成'\\'

    # 定义图片的保存路径，url.split('=')[-1]的意思是截取图片链接中最后一个=后的字符为图片名字
    path=Path.cwd().joinpath(randomjpgname)
    
    # 判断目录是否存在，如果不存在建立目录
    # 通过requests.get获得图片
    r=requests.get(url)
    r.raise_for_status()
    # 打开要存储的文件，然后将r.content返回的内容写入文件中，因为图片是二进制格式，所以用‘wb’，写完内容后关闭文件，提示图片保存成功
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("保存成功")

    im = Image.open(randomjpgname)
    im = im.convert("RGB")
    im1 = im.filter(ImageFilter.GaussianBlur(radius=5))
    im1.save(randomjpgname)
    im1.close()
def getrandomjpname(rjn):
    filieurl = Path.cwd().joinpath(rjn)
    return filieurl