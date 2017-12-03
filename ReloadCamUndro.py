#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ReloadCam

def GetVersion():
   return 1

def ReloadCamUndro():
   import os
   # Read in the file
   with open(ReloadCam.cccamPath, 'r') as file :
      
      # Replace the target string 
      lines = [( '' + line.replace('C: ', 'C:').replace('|1|0', '').replace('DEFAULT:1', '#').replace('DEFAULT:0', '#').replace(' ', '|').rstrip('\n') + '|1|0' + "\n" ) for line in if not line.startswith('#'): open(ReloadCam.cccamPath) ]

   # Write the file out again
   with open(ReloadCam.cccamPath, 'w') as file: 
   
      #IKS
      if lines == 0:
         file.write('DEFAULT:1\n')
      #CCCAM
      file.writelines(lines)

   import time
   # Reinicio de Spring.apk (al salir de qpython cargará de nuevo listas, canales, ...)
   #os.system("adb shell am force-stop com.dvb.spring.home")
   # Se copia el archivo al sistema
   #os.system("adb push " + ReloadCam.cccamPath + " /data/data/com.dvb.spring.home/app_tmp/card_server.cfg")
   import shutil
   shutil.copy2(ReloadCam.cccamPath, ReloadCam.cccamBin)
   
   print "Saliendo ..."
   
   # Salimos de qpython
   time.sleep(1.1)
   os.system("adb shell am force-stop com.hipipal.qpyplus")
