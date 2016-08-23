import os
def list_all(pathdir):
    for x in os.listdir(pathdir):
        dir_new = os.path.join(pathdir,x)
        if os.path.isdir(dir_new):
            list_all(dir_new)
        elif '.h' in x:
            print(x)
list_all('/home/syj/aosp/abi')
