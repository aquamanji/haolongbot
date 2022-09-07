import nonebot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init()
driver = nonebot.get_driver()
nonebot.init(apscheduler_autostart=True)
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})
driver.register_adapter(Adapter)
nonebot.load_builtin_plugins()
nonebot.load_plugin("nonebot_plugin_analysis_bilibili")
nonebot.load_plugin("haolongbot.plugins.haolong_picsearch")
nonebot.load_plugin("haolongbot.plugins.haolong_longtu")
nonebot.load_plugin("haolongbot.plugins.haolong_huozi")
nonebot.load_plugin("nonebot_plugin_addFriend")


if __name__ == "__main__":
    nonebot.run()