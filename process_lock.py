#多线程和多进程最大的不同在于：
#多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响；
#而多线程中，所有变量都由所有线程共享。
#所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容改乱了
import time,threading
#假定这是你的银行存款
balance = 0
lock = threading.Lock()
#先存后取，结果应该为0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
'''
def run_thread(n):
    for i in range(100000):
        change_it(n)
我们定义一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1,t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算
balance = balance + n
也分两步：
1.计算balance+n,存入临时变量中；
2.将临时变量的值赋给balance
究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了
两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名奇妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
'''
#如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it(),只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
#锁的好处：确保了某段关键代码只能由一个线程从头到尾完整地执行
#锁的坏处：1.阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行；2.由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
