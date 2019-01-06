from mail import *
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(1)

prepare_mail('smlep.pro@gmail.com', 5, 'fr')
