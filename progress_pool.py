#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')
'''
Parent process 7326.
Waiting for all subprocess done...
Run task 0 (7327)...
Run task 1 (7328)...
Run task 2 (7329)...
Run task 3 (7330)...
Task 3 runs 0.41 seconds.
Run task 4 (7330)...
Task 2 runs 1.92 seconds.
Task 4 runs 1.83 seconds.
Task 0 runs 2.69 seconds.
Task 1 runs 2.98 seconds.
All subprocess done
'''
#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#请注意输出的结果，task0,1,2,3是立刻执行的，而task4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4,因此，做多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
#由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
