import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S') 
    m = re.match(r'^UTC([+|-]\d{1,2}):00$',tz_str)
    tz = timezone(timedelta(hours=int(m.group(1))))
    dt_tz = dt.replace(tzinfo=tz)
    dt_0 = dt_tz.astimezone(timezone.utc)
    return dt_0.timestamp()
print(to_timestamp('2015-6-1 08:10:30','UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30','UTC-09:00'))
