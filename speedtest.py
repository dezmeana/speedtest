#! /usr/bin/python3
## Speed test python script from pimylifeup.com

import os
import re
import subprocess
import time

response = subprocess.Popen('/usr/bin/speedtest --simple --secure', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
ping = re.search('Ping:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload =  re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
#jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)

ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
#jitter = jitter.group(1)

try:
    f = open('./speedtest.csv', 'a+')
    if os.stat('/home/dezmeana/speedtest/speedtest.csv').st_size == 0:
          f.write('Date,Time,Ping (ms),Download (Mbps), Upload (Mbps)\r\n')
except:
    pass

f.write('{},{},{},{},{}\r\n'.format(time.strftime('%d/%m/%y'), time.strftime('%H:%M'),ping, download, upload))
