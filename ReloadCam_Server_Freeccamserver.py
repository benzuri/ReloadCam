#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Freeccamserver(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpH1wfNjX0dTEx5Kfppm1t7Lkk8_ezpOXpJiZcqiy5pea38nU')
        return realUrl

    def GetClines(self):
        print "Now getting Freeccamserver clines!"
        freeccamserverClines = []
        freeccamserverClines.append(self.__GetFreeccamserverClinesCline())
        freeccamserverClines = filter(None, freeccamserverClines)
        if len(freeccamserverClines) == 0: print "No Freeccamserver lines retrieved"
        return freeccamserverClines

    def __GetFreeccamserverClinesCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
return None
