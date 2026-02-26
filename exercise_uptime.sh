#!/bin/bash
for X in $(seq 146 150); do
  echo "========10.0.5.$X========"
  ssh -i ~/ansiblekey root@10.0.5.$X "uptime" >> ~/python/9/uptime.txt 2>&1
  echo "" >> ~/python/9/uptime.txt
done

# In one command line: 
#for X in $(seq 171 176); do echo "========10.0.5.$X========" >> ~/python/9/uptime.txt; ssh -i ~/ansiblekey root@10.0.5.$X "uptime" >> ~/python/9/uptime.txt 2>&1; done