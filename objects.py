from peewee import *
from playhouse.db_url import connect

soteriadb = connect(connect('mysql://soteria:passwd@db1.stm.inf.demilletech.net:33066/soteria'))

class Certificate(Model):
    cid         = IntegerField(unique=True, primary_key=True, sequence=True)
    publickey   = CharField(max_length=1000, unique=True)
    privatekey  = CharField(max_length=1000, unique=True)
    cdate       = DateField()
    c           = CharField(max_length=1000)
    st          = CharField(max_length=1000)
    l           = CharField(max_length=1000)
    o           = CharField(max_length=1000)
    ou          = CharField(max_length=1000)
    cn          = CharField(max_length=1000)
    ea          = CharField(max_length=1000)
    constraints = CharField(max_length=1000)
    keyusage    = CharField(max_length=1000)
    keylength   = CharField(max_length=1000)
    keyalg      = CharField(max_length=1000)
    sigalg      = CharField(max_length=1000)
    serial      = IntegerField()
    notbefore   = DateField()
    notafter    = DateField()
    x509ski     = CharField(max_length=1000)
    x509aki     = CharField(max_length=1000)
    x509san     = CharField(max_length=1000)
    i_c         = CharField(max_length=1000)
    i_st        = CharField(max_length=1000)
    i_l         = CharField(max_length=1000)
    i_o         = CharField(max_length=1000)
    i_ou        = CharField(max_length=1000)
    i_cn        = CharField(max_length=1000)
    i_ea        = CharField(max_length=1000)

    authority   = ForeignKeyField(ZClass, related_name='students')

    class Meta:
        database = soteriadb

class Authority(Certificate):
    pass