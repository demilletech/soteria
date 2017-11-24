from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64

'''
publickey   = CharField(max_length=1000, unique=True)
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
'''


def create_certificate(pem_data, is_bytes=False):
    if not is_bytes:
        #pem_data = pem_data.replace('\n', "")
        #pem_data = pem_data.replace('-----END CERTIFICATE-----', "")
        #pem_data = pem_data.replace('-----BEGIN CERTIFICATE-----', "")
        #pem_data = pem_data.replace(' ', "")
        #pem_data = base64.b64decode(pem_data)
        #pem_data = str.encode(pem_data)
        pem_data = bytes(pem_data, 'ASCII')
        
    cert = x509.load_pem_x509_certificate(pem_data, default_backend())
    fingerprint = cert.fingerprint(hashes.SHA256())
    subject = cert.subject
    notbefore = cert.not_valid_before
    notafter = cert.not_valid_after
    issuer = cert.issuer
    sigalg = cert.signature_hash_algorithm
    signature = cert.signature
    extensions = cert.extensions
    return {"fingerprint" : str(fingerprint), "subject" : str(subject), "notbefore" : str(notbefore), "notafter" : str(notafter),
    "issuer" : str(issuer), "sigalg" : str(sigalg), "signature" : str(signature), "extensions" : str(extensions)}