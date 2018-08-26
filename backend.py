#! /usr/bin/python
from subprocess import PIPE
import sys,subprocess,os
args = sys.argv
args.insert(3,'-1')
args[0] = 'unbuffer /tmp/A2/prober'
x = (' '.join(args))
oids = args[4:]
fil = subprocess.Popen(x,stdout=PIPE,shell = True)
for i in iter(fil.stdout.readline, ""):
    for q in range(len(oids)):
        i= i.replace(" ","")
        i = i.replace("\n","")
        rates= i.split('|')
        timestamp = int(float(rates[0]))
        t = str(timestamp)
        rating = rates[1:]
        #print oids[q],t,timestamp,rating[q]
        os.system("curl -i -XPOST 'http://localhost:8086/write?db=A3&u=ats&p=atslabb00&precision=s' --data-binary 'rate,oid='%s' value=%f %d'" %(oids[q], float(rating[q]), int(t)))









