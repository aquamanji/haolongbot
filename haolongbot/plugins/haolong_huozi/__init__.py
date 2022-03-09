from pathlib import Path
from typing import List
import random
# import nonebot
from nonebot import get_driver

from .config import Config
from nonebot import on_command, require, get_driver,on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.utils import escape,unescape
from nonebot.rule import to_me
import os
from .data_source import *

global_config = get_driver().config
config = Config(**global_config.dict())

huozijr = on_command("嘉然活字印刷",priority=5)
huoziotto = on_command("otto活字印刷",priority=5)
huoziqihai = on_command("七海活字印刷",priority=5)

@huozijr.handle()
async def fs(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    args = saveChinese(args)
    print(args)
    sound = getHuoZiSound(args,'jr')
    if(type(sound)==type("asd")):
        print(sound)
        await bot.send(event=event,message = sound)
    else:
        wavename = "out"+str(random.randint(0,9999))+str(random.randint(0,9999))+str(random.randint(0,9999))+".wav"
        sound.export(wavename,format='wav')
        filieurl = Path.cwd().joinpath(wavename)
        await bot.send(event=event,message=MessageSegment.record(file = filieurl))
        os.remove(wavename)

@huoziotto.handle()
async def fs(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    args = saveChinese(args)
    print(args)
    sound = getHuoZiSound(args,'otto')
    if(type(sound)==type("asd")):
        print(sound)
        await bot.send(event=event,message = sound)
    else:
        wavename = "out"+str(random.randint(0,9999))+str(random.randint(0,9999))+str(random.randint(0,9999))+".wav"
        sound.export(wavename,format='wav')
        filieurl = Path.cwd().joinpath(wavename)
        await bot.send(event=event,message=MessageSegment.record(file = filieurl))
        os.remove(wavename)

@huoziqihai.handle()
async def fs(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    args = saveChinese(args)
    print(args)
    sound = getHuoZiSound(args,'hzj')
    if(type(sound)==type("asd")):
        print(sound)
        await bot.send(event=event,message = sound)
    else:
        wavename = "out"+str(random.randint(0,9999))+str(random.randint(0,9999))+str(random.randint(0,9999))+".wav"
        sound.export(wavename,format='wav')
        filieurl = Path.cwd().joinpath(wavename)
        await bot.send(event=event,message=MessageSegment.record(file = filieurl))
        os.remove(wavename)
