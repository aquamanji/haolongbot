from pathlib import Path

# import nonebot
from nonebot import get_driver
from nonebot import on_command, require, get_driver,on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import nonebot.adapters.cqhttp
import _thread
from .data_source import savetodb,readamdb
from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

scheduler = require('nonebot_plugin_apscheduler').scheduler
a = 0
@scheduler.scheduled_job('interval',seconds=86400000,id='Amrsavetodb')
async def getmsgtodb():
    print("savedb运行中")
    await savetodb()

yq = on_keyword(["美国","润了","麻了"],priority=5)

@yq.handle()
async def fs(bot: Bot, event: Event, state: T_State):
    global a
    if a == 0:
        await getmsgtodb()
        a=a+1
    msg = await readamdb()
    await bot.send(event=event, message=str(msg))
