# ReloadCam
[Basado en gavazquez/ReloadCam para Undro]

Script para refrescar las ccclines automaticamente 

[QPython: Python for Android v1.2.3]

Ejemplo de Main.py:
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----Se necesita ser ROOT y la app Qpython para ejecutar el script
#----Crear un nuevo proyecto en la carpeta /mnt/sdcard/com.hipipal.qpyplus/projects/NOMBRE
#----Copia dentro Main.py y ReloadCam.py

import sys
import subprocess
import ReloadCam

def Main():
   subprocess.call([sys.executable, ReloadCam.GetCurrentPath() + 'ReloadCam.py', '-s', 'Testious'])

if __name__ == "__main__":
   Main()
```
