#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Cccamgate(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpH1wfNXIz9DOy5KmmGKmsHzVyM_QzpGll6aocbG14g==')
        return realUrl

    def GetClines(self):
        print "Now getting Cccamgate clines!"
        cccamgateClines = []
        cccamgateClines.append(self.__GetCccamgateCline())
        cccamgateClines = filter(None, cccamgateClines)
        if len(cccamgateClines) == 0: print "No Cccamgate lines retrieved"
        return cccamgateClines

    def __GetCccamgateCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None
