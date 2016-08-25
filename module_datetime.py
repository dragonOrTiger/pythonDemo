###################################################################################################################################################
#datetime是模块，datetime模块还包含一个datetime类
#通过from datetime inport datetime导入的才是datetime这个类
#如果仅导入import datetime,则必须引用全名datetime.datetime
#datetime.now()返回当前日期和时间，其类型是datetime
from datetime import datetime
now = datetime.now()
print(now)
####################################################################################################################################################
#要指定某个日期和时间，我们直接用参数构造一个datetime
dt = datetime(2015,4,19,12,20)
print(dt)
#在计算机中，时间实际上是用数字表示的。我们把1970年一月1日00:00:00 UTC+00:00时区的时刻为epoch time,记为0(1970年以前的时间timestamp为负数)，当前时间就是相对于epoch time的秒数，称为timestamp.
#可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也就完全确定的。这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）
####################################################################################################################################################
print(dt.timestamp())
#注意Ｐython的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
#某些编程语言(如Java或JavaScript)的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
#要把timestam转换为，使用datetime提供的fromtimestamp()方法
t = 1429417200.0
print(datetime.fromtimestamp(t))
#注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换实在timestamp和本地时间做转换
print(datetime.utcfromtimestamp(t))
#timestamp也可以直接被转换到UTC标准呢时区的时间
####################################################################################################################################################
#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现。需要一个日期和时间的格式化字符串
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)
#注意转换后的datetime是没有时区信息的。
#####################################################################################################################################################如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str,转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
print(now.strftime('%Y-%m-%d %A %H:%M:%S'))
####################################################################################################################################################
#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime.加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import timedelta
print(now+timedelta(hours=10))
print(now+timedelta(days=10))
print(now+timedelta(days=2,hours=12))
####################################################################################################################################################
#本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间是指UTC+0:00时区的时间
#一个datetime类型有一个时区属性tzinfo,但是默认为Ｎone,所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))#创建时区UTC+8:00
print(now.replace(tzinfo=tz_utc_8))#强制设置为UTC+8:00
#如果系统时区恰好是UTC+8:00,那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区
####################################################################################################################################################
#我们可以通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)#拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))#转换为北京时间
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))#转换为东京时间
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))#转换为东京时间
print(tokyo_dt2)
#时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
#利用带时区的datetime，通过astimezone()方法，可以转换到任意时区
#注意：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换。

#datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
