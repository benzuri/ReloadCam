#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Cccamious(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpLZ7fKHIz9LC0ZqhqKdxpLzflNLhxsmUlZaVsKq859ib1sbYX6KbpA==')
        return realUrl

    def GetClines(self):
        print "Now getting Cccamious clines!"
        cccamiousClines = []
        cccamiousClines.append(self.__GetCccamiousCline())
        cccamiousClines = filter(None, cccamiousClines)
        if len(cccamiousClines) == 0: print "No Cccamious lines retrieved"
        return cccamiousClines

    def __GetCccamiousCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None
