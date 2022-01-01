import json
from typing import Dict
from pathlib import Path

# import nonebot
from nonebot import get_driver
from nonebot import matcher
from nonebot.adapters.cqhttp.event import Event
from nonebot.config import Config
from nonebot.plugin import on_keyword, on_message, on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.matcher import Matcher
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent, PrivateMessageEvent, Message
from nonebot.utils import DataclassEncoder


from .plugins.saucenao import get_des as get_des_sau
from .plugins.ascii2d import get_des as get_des_asc

from .plugins.utils import limiter
global_config = get_driver().config
config = Config(**global_config.dict())

hpics = on_message(rule=to_me(),priority=6)
@hpics.handle()
async def handle(bot:Bot,event:MessageEvent,state:T_State):
    #判断是不是回复的消息
    if(event.reply==None):
        msg = Message(event.message)
    else:
        msg = Message(event.reply.message)
    if("[CQ:image," in str(msg)):
        for i in msg:
            if(i.type == "image"):
                await bot.send(event=event, message="正在处理图片喵")
                msgs: Message = sum([msg if isinstance(msg, Message) else Message(msg) async for msg in get_des_sau(i.data["url"])]+
                [msg if isinstance(msg, Message) else Message(msg) async for msg in get_des_asc(i.data["url"])]
                )
                dict_data = json.loads(json.dumps(msgs, cls=DataclassEncoder))
                if event.sub_type == "normal":
                    await bot.send_group_forward_msg(group_id=event.group_id,
                                                    messages=[
                                                        {
                                                            "type": "node",
                                                            "data": {
                                                                "name": event.sender.nickname,
                                                                "uin": event.user_id,
                                                                "content": [
                                                                    content
                                                                ]
                                                            }
                                                        }
                                                        for content in dict_data
                                                    ]
                                                    )
                else:
                    for msg in dict_data:
                           await hpics.send(msg)
    else:
        await hpics.send(event=event,message="请发送图片给我喵/或者可能图片没了喵")
                    

