# -*- coding: utf-8 -*-
from typing import List, Tuple
from urllib.parse import urljoin

from lxml.html import fromstring
import aiohttp
from nonebot.adapters.cqhttp import MessageSegment
from .proxy import proxy


def parse_html(html: str):
    selector = fromstring(html)
    pt1 = selector.xpath('//div[@class="container"]/div[@class="row"]/div[@class="col-xs-12 col-lg-8 col-xl-8"]/h5[@class="p-t-1 text-xs-center"]')[0].text
    for tag in selector.xpath('//div[@class="container"]/div[@class="row"]/div/div[@class="row item-box"]')[1:2]:
        picjson = {
            'pic_js':pt1
        }
        if pic_url := tag.xpath('./div/img[@loading="lazy"]/@src'):  # 缩略图url
            pic_url = urljoin("https://ascii2d.net/", pic_url[0])
            picjson['pic_url'] = pic_url
        if description := tag.xpath('./div/div/h6/a[1]/text()'):  # 名字
            description = description[0]
            picjson['description'] = description
        if author := tag.xpath('./div/div/h6/a[2]/text()'):  # 作者
            author = author[0]
            picjson['author'] = author
        if origin_url := tag.xpath('./div/div/h6/a[1]/@href'):  # 原图地址
            origin_url = origin_url[0]
            picjson['origin_url'] = origin_url
        if author_url := tag.xpath('./div/div/h6/a[2]/@href'):  # 作者地址
            author_url = author_url[0]
            picjson['author_url'] = author_url
        yield picjson

    pass
async def get_ascii2d_str(html:str):
    selector = fromstring(html)
    a = selector.xpath('/html/body/div[@class="container"]/div[@class="row"]/div[@class="col-xs-12 col-lg-8 col-xl-8"]/div[@class="row item-box"][1]/div[@class="detail-link pull-xs-right hidden-sm-down gray-link"]/span[2]/a')
    return a[0].attrib['href']
    pass

async def get_pic_from_url(url: str):
    base_base_url = "https://ascii2d.net"
    base_url = base_base_url+"/search/url/"
    real_url = base_url + url +"?type=color"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
    }
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64,verify_ssl=False)) as session:
        async with session.get(real_url,headers=headers) as resp:
            html: str = await resp.text()
            async with session.get(base_base_url+await get_ascii2d_str(html), headers=headers) as resp:
                html2: str = await resp.text()
        return [i for i in parse_html(html)]+[b for b in parse_html(html2)]


async def get_des(url: str):
    try:
        image_data: List[Tuple] = await get_pic_from_url(url)
        # print(image_data)
        if not image_data:
            msg: str = "找不到高相似度的"
            yield msg
        for pic in image_data:
            msg = MessageSegment.image(file=pic['pic_url'])+ f"ascii2d检索方式：{pic['pic_js']}\n名字:{pic['description']}\n作者:{pic['author']}\n原图地址:{pic['origin_url']}\n作者地址:{pic['author_url']}"
            # print(pic)
            yield msg
    except:
        msg="网络爆炸喵"
        yield msg
