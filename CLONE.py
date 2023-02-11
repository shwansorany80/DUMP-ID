#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf CLONE.so CLONE32.so')
except:
    pass
os.system('rm -rf CLONE.so CLONE32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('CLONE.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/eex/blob/main/CLONE.cpython-311.so?raw=true -o CLONE.so') 
        __import__("CLONE").Main_()
    else:
        __import__("CLONE").Main_()

elif bit == '32bit':
    if not os.path.isfile('CLONE32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/eex/blob/main/CLONE32.cpython-311.so?raw=true -o CLONE32.so') 
        __import__("CLONE32").Main_()
    else:
        __import__("CLONE32").Main_()
