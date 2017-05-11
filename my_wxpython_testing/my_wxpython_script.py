# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:15:15 2017

@author: John
asdftoger

"""
import wx
#wx.Frame: parent defines the frame that the widget in part of
class myFrame(wx.Frame):
    
    
    def __init__(self,parent,title):
        
        #Creates a frame for the UI
        wx.Frame.__init__(self,parent = parent,title=title,size = (300,300))
#       
 #creates text in the box
        self.i = 0        
 
        #Create a split frame
        self.splitFrame = wx.SplitterWindow(self)
        self.f1 = wx.Panel(self.splitFrame,style= wx.SUNKEN_BORDER)
        self.f2 = wx.Panel(self.splitFrame,style= wx.SUNKEN_BORDER)
        self.splitFrame.SplitHorizontally(self.f1,self.f2,100)
        
        #Static text to change
        self.t1 = wx.StaticText(self.f1,label = '0',style = wx.ALIGN_CENTER)
        
        
        #Create buttons,
        self.value1button = wx.Button(self.f1,label='One',size = (120,100),pos = (40,20))
        self.value2button = wx.Button(self.f2,-1,'We\'re team two',size = (120,100),pos = (40,20))
        
        #Sizer
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.t1, 1)
        self.sizer.Add(self.value1button)

        
#        #Creates button events on click
        self.value1button.Bind(wx.EVT_BUTTON,self.plusOne)
        self.f1.SetSizerAndFit(self.sizer)
        self.Show()
        
    def plusOne(self,dummy):
        self.i = self.i + 1
        self.t1.SetLabel(str(self.i) )
        self.sizer.Layout()
                
if __name__ == '__main__':
    app = wx.App(redirect = False)
    frame = myFrame(None,'This is a title')
    frame.Show()
    app.MainLoop()
    exit()