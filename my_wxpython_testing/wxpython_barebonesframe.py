#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self,*args,**kw)
        
        #Defines frame for UI
        pnl = wx.Panel(self)
        #Defines button and close event
        cbtn = wx.Button(pnl, label='Close', pos=(20, 30))
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)
        #Parameters
        
        self.SetSize((250, 200))
        self.SetTitle('wx.Button')
        self.Centre()
        self.Show(True)          
        
    def OnClose(self, e):
        
        self.Close(True)                  
        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()   