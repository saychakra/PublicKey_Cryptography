import sys
import time
from time import sleep

def loadScreen():
    for i in range(0, 101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
        sys.stdout.flush()
        sleep(0.05)
