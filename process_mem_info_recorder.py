#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
import subprocess
import sys
import re
import platform
from time import gmtime, strftime

class MemInfo:
     patternProcess = re.compile(r'\*\* MEMINFO in pid (\d+) \[(\S+)] \*\*')
     patternTotalPSS = re.compile(r'TOTAL:\s+(\d+)')
     
     pid = 0
     processName = ''
     datetime = ''
     totalPSS = 0
     
     def __init__(self, dump):
         self.dump = dump
         self._parse()

     def _parse(self):
        match = self.patternProcess.search(self.dump)
        if match:
            self.pid = match.group(1)
            self.processName = match.group(2)
        match = self.patternTotalPSS.search(self.dump)  
        if match:
            self.totalPSS = match.group(1)

def dumpsys_process_meminfo(process):
#     os.system('adb shell dumpsys meminfo "' + process)
    proc = subprocess.Popen(args='adb shell dumpsys meminfo "' + process + '"', stdout=subprocess.PIPE, stderr=sys.stderr, shell=True)
    out = proc.communicate()[0]
    return MemInfo(dump=out.decode(encoding='windows-1252'))                      

def re_exe(process, dir, historyFileName, abstractFileName, interval=60):
    if not os.path.exists(dir):
        os.makedirs(dir)
        
    with open(dir + "\\" + abstractFileName, "a") as write_abstract_file:
        with open(dir + "\\" + historyFileName, "a") as write_history_file:
            try:
                while True:
                    datetime = strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                    memInfo = dumpsys_process_meminfo(process)
                    
                    if memInfo.dump == '':
                        break
                    elif memInfo.dump.startswith('No process found for:') :
                        raise RuntimeError()
                    
                    memInfo.datetime = datetime
                    write_history_file.write('\n')
                    write_history_file.write(datetime)
                    write_history_file.write(memInfo.dump)
                    write_history_file.flush()
                    
                    write_abstract_file.write(str(memInfo.pid) + "," + memInfo.processName + "," + datetime + "," + str(memInfo.totalPSS))
                    write_abstract_file.write('\n')
                    write_abstract_file.flush()
                    
                    print(memInfo.dump)
#                     print('\n\nPress CTRL+C to break loop:')
                    time.sleep(interval)
            except RuntimeError:
                print(memInfo.dump)
            except KeyboardInterrupt:
                pass

if __name__ == "__main__":
    usr = os.path.expanduser('~')
    platform = platform.system()
    desktop = ''
    
    if platform == 'Windows':
        desktop = r'\Desktop';
        
    out_path = usr + desktop + r"\PythonAndroidMonitor"
    out_mem_history_file = "mem_history.txt"
    out_mem_abstract_file = "mem_abstract.CSV"
    dir = strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    
    process = input("Please input the process name:")
    interval = 0
    
    while not interval:
        try:
            interval = int(input('Please input the catch interval(second, value should >= 10):'))
            if interval < 10:
                raise Exception
        except ValueError:
            interval = 0
            print("Please input integer!")
        except Exception:
            interval = 0
            print("Value should >= 10!")
            
    re_exe(process=process, dir=out_path + "\\" + dir, historyFileName=out_mem_history_file, abstractFileName=out_mem_abstract_file, interval=interval)
