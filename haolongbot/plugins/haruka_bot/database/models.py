from tortoise.models import Model
from tortoise.fields.data import CharField, IntField, BooleanField


class Sub(Model):
    type = CharField(max_length=10)
    type_id = IntField()
    uid = IntField()
    live = BooleanField()
    dynamic = BooleanField()
    at = BooleanField()
    bot_id = IntField()


class User(Model):
    uid = IntField(pk=True)
    name = CharField(max_length=20)


class Group(Model):
    id = IntField(pk=True)
    admin = BooleanField()


class Version(Model):
    version = CharField(max_length=30)


class mg(Model):
    #pk就是选主键的意思
    #如果不选择主键会自动帮你生成主键
    id = IntField(pk=True)
    msg = CharField(max_length=255)

    #下面这个str可写可不写 但是写了更好
    #会在调试器和解释器中显示此模型的名
    def __str__(self):
        return self.msg
