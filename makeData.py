import datetime

f = open('data.csv', 'w')
s = 60*60*24*7

now = datetime.datetime.now()
before = datetime.timedelta(seconds=s)
start = now - before
print(now)
print(start)

sec1 = datetime.timedelta(seconds=1)
for x in range(s*2):
    #print(start.strftime('%Y-%m-%d %H:%M:%S'))
    f.write(start.strftime('%Y-%m-%d %H:%M:%S') + ', 1\n')
    f.write(start.strftime('%Y-%m-%d %H:%M:%S') + ', 1\n')
    if start.hour > 10 and start.hour < 21:
        f.write(start.strftime('%Y-%m-%d %H:%M:%S') + ', 1\n')
        f.write(start.strftime('%Y-%m-%d %H:%M:%S') + ', 1\n')
    start = start + sec1

