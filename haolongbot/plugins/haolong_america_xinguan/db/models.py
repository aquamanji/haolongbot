
from tortoise.models import Model
from tortoise.fields.data import CharField, IntField, BooleanField
class mg(Model):
    #pk就是选主键的意思
    #如果不选择主键会自动帮你生成主键
    id = IntField(pk=True)
    msg = CharField(max_length=255)

    #下面这个str可写可不写 但是写了更好
    #会在调试器和解释器中显示此模型的名
    def __str__(self):
        return self.msg