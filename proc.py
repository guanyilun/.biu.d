import sys
import os

def kill():
    """kill through output of ps aux as i usually do"""
    lines = [l.rstrip() for l in sys.stdin.readlines()]
    for l in lines:
        pid = l.split()[1]
        try:
            int(pid)
        except:
            continue
        cmd = "kill -9 %s" % pid
        print(cmd)
        os.system(cmd)

