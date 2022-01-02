from nonebot import on_command
from nonebot.adapters.cqhttp import Bot
from nonebot.adapters.cqhttp.event import MessageEvent
from nonebot.typing import T_State
from nonebot.matcher import matchers

from ..utils import to_me
from ..version import __version__


help = on_command('直播帮助', rule=to_me(), priority=5)

@help.handle()
async def test(bot: Bot, event: MessageEvent, state: T_State):
    message = "帮助：\n添加主播\n删除主播\n"
    # for matchers_list in matchers.values():
    #     for matcher in matchers_list:
    #         print(matcher.__doc__)
    #         if ("haruka_bot" in matcher.plugin_name and matcher.__doc__!=None):
    #             message += matcher.__doc__+'\n'
    await help.finish(message)