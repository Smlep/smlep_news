from mail import prepare_mail
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(1)

prepare_mail("test@gmail.com", 5, "fr")
