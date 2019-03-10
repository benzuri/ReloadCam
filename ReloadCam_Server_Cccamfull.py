#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines
#Creado por Dagger

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 2

#Filename must start with Server, classname and argument must be the same!
class Cccamfull(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt("maanpLZ7fKHIz9LC0V6YqKCvb7Dh0pvV08mWlZaXpK574s3c")
        return realUrl

    def GetClines(self):
        print "Now getting Cccamfull clines!"
        cccamfullClines = []
        cccamfullClines.append(self.__GetCccamfullCline())
        cccamfullClines = filter(None, cccamfullClines)
        if len(cccamfullClines) == 0: print "No Cccamfull lines retrieved"
        return cccamfullClines

    def __GetCccamfullCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None
