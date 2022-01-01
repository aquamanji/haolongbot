
import asyncio
from contextlib import asynccontextmanager
import aiohttp
import lxml.html
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tortoise import run_async
from .db.db import *
from nonebot import require
scheduler = require("nonebot_plugin_apscheduler").scheduler

async def getAmericaData():
    try:
        headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
        url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"
        async with aiohttp.request('GET', url,headers=headers) as resp:
            text = await resp.json()
            return text
    except:
        return None
async def getAmreicamsg():
    data = await getAmericaData()
    if data:
        data = data['data']['areaTree']
        mg = {}
        for i in data:
            if i['name']== "美国":
                mg=i 
                break
        todayConfirm = mg['today']['confirm']
        todayDead = mg['today']['dead']
        totalConfirm = mg['total']['confirm']
        totalDead = mg['total']['dead']
        lastUpdateTime = mg['lastUpdateTime']
        msg = f"你说的对但是根据美国约翰斯·霍普金斯大学实时统计数据，截至北京时间{lastUpdateTime}，美国在过去的24小时内报告了超过{todayDead}例新冠死亡病例。此外，根据约翰斯·霍普金斯大学统计数据，美国目前至少有{totalConfirm}例新冠确诊病例，而且拥有{totalDead}例新冠死亡病例。"
        return msg

async def savetodb():
    async with DB() as db:
        await db.datasave(await getAmreicamsg())
async def readamdb():
    async with DB() as db:
        p1 = await db.dataget()
    return p1['msg']