import json
from typing import Dict
from pathlib import Path

# import nonebot
from nonebot import get_driver
from nonebot import matcher
from nonebot.adapters.onebot.v11.event import Event
from nonebot.config import Config
from nonebot.plugin import on_keyword, on_message, on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent, PrivateMessageEvent, Message
from nonebot.utils import DataclassEncoder

import os
from .plugins.saucenao import get_des as get_des_sau
from .plugins.ascii2d import get_des as get_des_asc

from .plugins.utils import limiter

global_config = get_driver().config
config = Config(**global_config.dict())

hpics = on_message(rule=to_me(),priority=6)
@hpics.handle()
async def handle(bot:Bot,event:MessageEvent,state:T_State):
    need_reply = 1
    #判断是不是回复的消息
    if(event.reply==None):
        msg = Message(event.message)
    else:
        msg = Message(event.reply.message)
        getuserid = await bot.get_login_info()
        userid = getuserid['user_id']
        if(event.reply.sender.user_id == userid):
            need_reply = 0    

    if("[CQ:image," in str(msg) and need_reply):
        for i in msg:
            if(i.type == "image"):
                await bot.send(event=event, message="正在处理图片喵 返回会有高斯模糊喵")
                msgs  = []
                async for msg in get_des_sau(i.data["url"]):
                    if isinstance(msg,Message):
                        msgs.append(msg)
                    else:
                        msgs.append(Message(msg))

                async for msg in get_des_asc(i.data["url"]):
                    if isinstance(msg,Message):
                        msgs.append(msg)
                    else:
                        msgs.append(Message(msg))
                dict_data1 = json.loads(json.dumps(msgs, cls=DataclassEncoder))
                dict_data = msgs
                if event.sub_type == "normal":
                    dict_contents = []
                    for content in dict_data1:
                        dict_contents.append(
                        {
                            "type": "node",
                            "data": {
                            "name": event.sender.nickname,
                            "uin": event.user_id,
                            "content": content
                                                            }
                        }

                        )
                    await bot.send_group_forward_msg(group_id=event.group_id,
                                                    messages=dict_contents
                                                    )
                else:
                    for msg in dict_data:
                           await hpics.send(msg)
                for msgfile in dict_data1:
                    if msgfile[0]['type'] == 'image':
                        picfilename = msgfile[0]['data']['file'][8:]
                        os.remove(picfilename)