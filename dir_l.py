import os
import time
def dir_l(pathdir):
    for i in os.listdir(pathdir):
        complete_dir = os.path.join(pathdir,i)
        pow = oct(os.stat(complete_dir).st_mode)[-3]
        ti = os.stat(complete_dir).st_mtime
        Itime = time.localtime(ti)
        timeStr = time.strftime('%Y-%m-%d %H:%M:%S',Itime)
        size = os.path.getsize(complete_dir)
        print(pow,'\t','%-10s' % size,'\t',timeStr,'\t',i)
pathdir = input('input dir:')
dir_l(pathdir)
