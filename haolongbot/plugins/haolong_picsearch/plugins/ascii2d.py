# -*- coding: utf-8 -*-
from typing import List, Tuple
from urllib.parse import urljoin

from lxml.html import fromstring
import aiohttp
from nonebot.adapters.onebot.v11 import MessageSegment

from haolongbot.plugins.haolong_picsearch.plugins.msk import getrandomjpname, msktoimg
from .proxy import proxy

from PicImageSearch import Ascii2D, Network
from PicImageSearch.model import Ascii2DResponse
import random

proxies = None
bovw = True  # 是否使用特征检索

async def get_pic_from_url_new(url:str):
        async with Network(proxies=proxies) as client:
            #色合
            ascii2d = Ascii2D(client=client, bovw=bovw)
            #特征
            ascii2dnotbovw = Ascii2D(client=client,bovw=False) 
            resp = await ascii2d.search(url)
            respnotbovw = await ascii2dnotbovw.search(url)
            allresp = []
            if resp.raw[0].url == "":
                allresp.append(resp.raw[1])
                allresp.append(resp.raw[2])
            else:
                allresp.append(resp.raw[0])
                allresp.append(resp.raw[1])
            if respnotbovw.raw[0].url == "":
                allresp.append(respnotbovw.raw[1])
                allresp.append(respnotbovw.raw[2])
            else:
                allresp.append(respnotbovw.raw[0])
                allresp.append(respnotbovw.raw[1])        
            return allresp


async def get_des(url: str):
    try:
        image_data: List[Tuple] = await get_pic_from_url_new(url)
        asc2dcomputer = 0
        if not image_data:
            msg: str = "找不到高相似度的"
            yield msg
        for pic in image_data:
            if asc2dcomputer<2 :
                asc2dcomputer= asc2dcomputer+1
                randomjpgname = "out"+str(random.randint(0,9999))+str(random.randint(0,9999))+str(random.randint(0,9999))+".jpg"
                msktoimg(url=pic.thumbnail,randomjpgname=randomjpgname)
                msg = MessageSegment.image(file=getrandomjpname(randomjpgname))+ f"ascii2d检索方式：色合\n名字:{pic.title}\n作者:{pic.author}\n原图地址:{pic.url}"
            else:
                randomjpgname = "out"+str(random.randint(0,9999))+str(random.randint(0,9999))+str(random.randint(0,9999))+".jpg"
                msktoimg(url=pic.thumbnail,randomjpgname=randomjpgname)
                msg = MessageSegment.image(file=getrandomjpname(randomjpgname))+ f"ascii2d检索方式：特征\n名字:{pic.title}\n作者:{pic.author}\n原图地址:{pic.url}"
            # print(pic)
            yield msg
    except:
        msg="网络爆炸喵"
        yield msg
