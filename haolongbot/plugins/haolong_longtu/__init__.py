from pathlib import Path
from typing import List

# import nonebot
from nonebot import get_driver

from .config import Config
from nonebot import on_command, require, get_driver,on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.adapters.onebot.v11.utils import escape,unescape
import os
from .data_source import *

global_config = get_driver().config
config = Config(**global_config.dict())

longtu = on_keyword(['龙图'],priority=5)
ltlist = ['0']
musiclist = getKeywordsAndFullwords('voice')
videolist = getKeywordsAndFullwords('video')
print(videolist['basename'])
@longtu.handle()
async def fs(bot: Bot, event: Event, state: T_State):
    global ltlist
    if(ltlist[0]=='0'):
        ltlist = returnltlist('lt')
        print("写入成功！")
    pic=getrangelist(ltlist,'lt')
    msg = MessageSegment.image(file=pic)
    await bot.send(event=event,message=msg)

voice = on_keyword(musiclist['basename'],priority=5)
@voice.handle()
async def fs2(bot: Bot, event: Event, state: T_State):
    global musiclist
    text = event.get_plaintext()
    filefullname = ''
    for index,value in enumerate(musiclist['basename']):
        if(value in text):
            filefullname = musiclist['fullname'][index]
            evelist = event.get_session_id().split('_')
            if(evelist[0] =='group'):
                if(evelist[1]=='421803828' or evelist[1] == '807900779'):
                    filefullname = random.choice(['tmspade.wav','tmspade2.wav'])
            break
    fileurl = getSelectedvalueFile(filefullname,'voice')
    await bot.send(event=event,message=MessageSegment.record(file = fileurl))

video = on_keyword(videolist['basename'],priority=5)
@video.handle()
async def fs2(bot: Bot, event: Event, state: T_State):
    global videolist
    text = event.get_plaintext()
    filefullname = ''
    for index,value in enumerate(videolist['basename']):
        if(value in text):
            filefullname = videolist['fullname'][index]
            break
    fileurl = getSelectedvalueFile(filefullname,'video')
    msg=MessageSegment.video(file = fileurl)
    print(msg)
    await bot.send(event=event,message=msg)