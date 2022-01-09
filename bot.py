import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
driver = nonebot.get_driver()
nonebot.init(apscheduler_autostart=True)
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
nonebot.load_plugin('haolongbot.plugins.haruka_bot')
nonebot.load_plugin("haolongbot.plugins.nonebot_plugin_analysis_bilibili")
nonebot.load_plugin("haolongbot.plugins.haolong_picsearch")
nonebot.load_plugin("haolongbot.plugins.haolong_america_xinguan")
nonebot.load_plugin("haolongbot.plugins.haolong_longtu")
# nonebot.load_plugin("nonebot_plugin_gamedraw")

if __name__ == "__main__":
    nonebot.run()