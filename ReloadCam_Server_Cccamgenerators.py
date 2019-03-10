#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Cccamgenerators(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpLZ7fKHIz9LC0ZiXoZm1osHh19-dxNOeYZqZsaa_09nb4ZDLlqZhpKux')
        return realUrl

    def GetClines(self):
        print "Now getting Cccamgenerators clines!"
        cccamgeneratorsClines = []
        cccamgeneratorsClines.append(self.__GetCccamgeneratorsCline())
        cccamgeneratorsClines = filter(None, cccamgeneratorsClines)
        if len(cccamgeneratorsClines) == 0: print "No Cccamgenerators lines retrieved"
        return cccamgeneratorsClines

    def __GetCccamgeneratorsCline(self):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
return None
