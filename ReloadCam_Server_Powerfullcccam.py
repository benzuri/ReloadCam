#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Powerfullcccam(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpH1wfOLU49TTyqaen5empK7fk8_ezpOhoaqZtafC3tGb1sbYX6KbpA==')
        return realUrl

    def GetClines(self):
        print "Now getting Powerfullcccam clines!"
        powerfullcccamClines = []
        powerfullcccamClines.append(self.__GetPowerfullcccamCline())
        powerfullcccamClines = filter(None, powerfullcccamClines)
        if len(powerfullcccamClines) == 0: print "No Powerfullcccam lines retrieved"
        return powerfullcccamClines

    def __GetPowerfullcccamCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None
