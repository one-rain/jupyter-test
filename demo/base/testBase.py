# coding=utf-8
# print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from notebook.auth import passwd


def myprint(msg):
    print("  ")
    print("============== %s ==============" % msg)
    print("  ")


def create_password():
    myprint('password')
    print(passwd('Beyond520'))


create_password()
