from pybgmax.content import (
    BgMaxFile,
    Deposit,
    PaymentReference,
    PaymentSender,
    Payment,
    BgNo,
    PgNo,
)

from pybgmax.parser import parse

REFTYPE_BLANK = 0
REFTYPE_UNAVAILABLE = 1
REFTYPE_OCR = 2
REFTYPE_MULTI = 3
REFTYPE_REF = 4
REFTYPE_BAD = 5

CHANNEL_EBANK = 1
CHANNEL_LB = 2
CHANNEL_SLIP = 3
CHANNEL_AG = 4

def load(txt_file):
    data = None
    if isinstance(txt_file, str):
        with open(txt_file, 'r') as fp:
            data = fp.read().decode('ISO-8859-1')
    elif hasattr(txt_file, 'read'):
        data = txt_file.read()
        if isinstance(data, bytes):
            data = data.decode('utf-8')
    else:
        raise ValueError('txt_file must be file-like or path string')

    return parse(data)
