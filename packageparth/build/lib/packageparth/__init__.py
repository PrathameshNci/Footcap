import random
import datetime


def generate(a,b):
    now = datetime.datetime.now()
    date1 = now.strftime("%Y%m%d%H%M%S")
    date1 = int(date1)
    r=random.randint(a,b)
    return int(str(date1)+str(r))