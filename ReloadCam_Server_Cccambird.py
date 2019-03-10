#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Cccambird(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpH1wfOnc453Ex5SToJass7GgyNvckMeUlZShd3m1oNXU3w==')
        return realUrl

    def GetClines(self):
        print "Now getting Cccambird clines!"
        cccambirdClines = []
        cccambirdClines.append(self.__GetCccambirdCline())
        cccambirdClines = filter(None, cccambirdClines)
        if len(cccambirdClines) == 0: print "No Cccambird lines retrieved"
        return cccambirdClines

    def __GetCccambirdCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None
