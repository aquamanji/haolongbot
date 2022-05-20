# -*- coding: utf-8 -*-
import io
from typing import List, Tuple

import aiohttp
from lxml.html import fromstring
from nonebot.adapters.cqhttp import MessageSegment

from .formdata import FormData
from .proxy import proxy

from PicImageSearch import Network, SauceNAO
from PicImageSearch.model import SauceNAOResponse


api_key = "77479bbb5a93b2a31d2647d275e9bf5831f2bac0"
proxies = None


async def get_pic_from_url_new(url:str):
    async with Network(proxies=proxies) as client:
        saucenao = SauceNAO(client=client, api_key=api_key,numres = 3)
        resp = await saucenao.search(url)
        return resp.raw

async def get_des(url: str):
    try:
        image_data: List[Tuple] = await get_pic_from_url_new(url)
        if not image_data:
            msg: str = "找不到高相似度的喵"
            yield msg
            return
        for pic in image_data:
            msg = MessageSegment.image(file=pic.thumbnail) + f"saucenao搜索:\n相似度:{pic.similarity}\n标题:{pic.title}\n图片地址:{pic.url}\n作者:{pic.url}\n"
            yield msg
    except:
        msg: str = "网络爆炸喵"
        yield msg
    pass
