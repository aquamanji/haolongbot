from tortoise.fields.data import CharField, IntField, BooleanField
from pathlib import Path
from .models import mg
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_queryset_creator
from tortoise import Tortoise, run_async
from tortoise.fields.data import CharField, IntField, BooleanField
from tortoise.query_utils import Q
from .utils import get_path
from nonebot import get_driver

class DB:
    
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        Tortoise.close_connections()
        pass

    # 初始化db
    async def dbinit(self):
        from . import models
        # 会自动创建一个db.sqlite3
        # 把对应的关系放到modules={'models': ['models']}
        await Tortoise.init(
            db_url=f"sqlite://{get_path('data.sqlite3')}",
            modules={'models': [locals()['models']]}
        )
        # 创建连接
        await Tortoise.generate_schemas()

    async def datasave(self, msga):
        if await mg.exists(id=1):
            await mg.filter(id=1).update(msg=msga)
        else:
            await mg.create(id=1, msg=msga)

    async def dataget(self):
        if await mg.exists(id=1):
            p1 = await mg.get(id=1).values()
            return p1
        else:
            return None


async def init():
    async with DB() as db:
        await db.dbinit()


get_driver().on_startup(init)
get_driver().on_shutdown(Tortoise.close_connections)