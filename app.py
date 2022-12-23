import datetime
import numpy as np

def dateWithBusDays(date: datetime.date, days:int = 0) -> datetime.date:
    if days < 0: return datetime.datetime.now()
    end = date + datetime.timedelta(days=days)
    d: int = np.busday_count(date, end, weekmask=[1,1,1,1,0,0,1])
    while days > d:
        end = end + datetime.timedelta(days=(days-int(d)))
        d: int = np.busday_count(date, end, weekmask=[1,1,1,1,0,0,1])
    return end