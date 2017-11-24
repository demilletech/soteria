from peewee import *
from playhouse.db_url import connect

soteriadb = connect('mysql://soteria:5Xfit*gCc8o@q6Z12j@db1.stm.inf.demilletech.net:3306/soteria')

class Certificate(Model):
    cid         = IntegerField(unique=True, primary_key=True)
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
    fingerprint = CharField(max_length=1000)
    keyusage    = CharField(max_length=1000)
    keylength   = CharField(max_length=1000)
    keyalg      = CharField(max_length=1000)
    sigalg      = CharField(max_length=1000)
    signature   = CharField(max_length=1000)
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
    i_cid       = IntegerField()

    class Meta:
        database = soteriadb

    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        return str(r)

    def get(i_cid=None, cdate=None, c=None, st=None, l=None, o=None, ou=None, cn=None, ea=None, keylength=None, sigalg=None):
        return Certificate.select(Certificate.i_cid == i_cid, Certificate.cdate == cdate,
                                Certificate.c == c, Certificate.st == st, Certificate.l == l,
                                Certificate.o == o, Certificate.ou == ou, Certificate.cn == cn,
                                Certificate.ea == ea, Certificate.keylength == keylength,
                                Certificate.sigalg == sigalg)


def init():
    soteriadb.connect()
    soteriadb.create_tables([Certificate], safe=True)
