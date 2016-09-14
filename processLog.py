#!/usr/bin/python
import sys
import datetime
import re
import os

output = open('/root/scripts/processLog.log', 'a')
output.write ('----------------------------------------------------------\n');
output.write (str (datetime.datetime.now()) + '\n')

# Get IP address embedded in a syslog message
def getIP (line):
    hits = []
    hits = re.findall ("SrcIP\: [\d\.]+", line)
    if len (hits) > 0:
        match = str (hits[0])
        if len (match) > 7:
            ip = match [7 : len (match)]
            return ip
        else:
            return "Error"
    else:
        return "No Match"

def isSQLInjection (line):
    hits = []
    hits = re.findall ("HTTP encoded SQL attack", line)
    if len (hits) > 0:
        return True
    else:
        return False

def isSQLAttack (line):
    hits = []
    hits = re.findall ("MySQL server Attack", line)
    if len (hits) > 0:
        return True
    else:
        return False

try:
    line = sys.stdin.readline()
    output.write (line)
except Exception as e:
    output.write (str (Exception))
    output.close
    sys.exit (0)

ip = str (getIP (line))
output.write (" - Extracted Src IP: " + ip + "\n")
if isSQLInjection (line):
    output.write (" - Incident type: SQL Code Injection\n")
    command = "/usr/bin/python /root/asa-demo/insert-be.py"
    output.write (" - Running command %s to insert backend FW+IPS\n" % command)
    os.system (command)
    command = "/root/scripts/SparkMsg.sh 'I have seen a SQL Code Injection attack in the Sirius application, I am inserting a firewall between the Web and the DB servers'"
    os.system (command)
elif isSQLAttack (line):
    output.write (" - Incident type: MySQL Server Attack\n")
    command = "/usr/bin/python /root/scripts/setcustomatt.py -s 192.168.0.30 -u root -p cisco123 -k Attacked -v True -i " + ip
    output.write (" - Running command /usr/bin/python /root/scripts/setcustomatt.py -s 192.168.0.30 -k Attacked -v True -i %s\n" % ip)
    os.system (command)
    command = "/root/scripts/SparkMsg.sh 'Server " + ip + " seems to be compromised, I am putting it in quarantine'"
    os.system (command)
else:
    output.write (" - Attack type not identified")
output.close()

