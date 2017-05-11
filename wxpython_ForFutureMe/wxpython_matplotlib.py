
'''
Shows me how to draw an interactive matplotlib sinewave
'''
import wx
import numpy as np


#Plotting libraries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx



class Window(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Window, self).__init__(*args, **kw) 
        
        self.InitUI()
        self.Centre()
        self.Show(True)    

    def InitUI(self):   

        pnl = wx.Panel(self)
        
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        #Setting up plotting axes
        self.fig = plt.figure(figsize=(4,3))
        self.axes = self.fig.add_subplot(111)
        
        #Use plotCanvas in subsequent methods
        self.plotCanvas = FigureCanvas(pnl,id = -1,figure=self.fig)
        vbox1.Add(self.plotCanvas)
        
        
        
        #Defines slider for interaction
        sldLow,sldHigh = 1,5
        self.sld = wx.Slider(pnl, value=sldLow, minValue=sldLow, maxValue=sldHigh, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL)
        self.sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        
        #After slider is defined, initialize the drawing 
        self.plotCanvasDraw()
        hbox1.Add(self.sld,flag =wx.ALIGN_LEFT)
        
        #Defines static text for slider value
        self.txt = wx.StaticText(pnl, label='y = sin({}*t)'.format(str(sldLow)), pos=(20, 90))               
        hbox1.Add(self.txt,flag = wx.ALIGN_RIGHT)
        vbox1.Add(hbox1)
        
        
        #Closing button
        self.buttonClose = wx.Button(pnl, label="Close App",style=wx.ALIGN_CENTRE)
        self.buttonClose.Bind(wx.EVT_BUTTON, self.closeWindow)
        vbox1.Add(self.buttonClose)
        
        #vbox contains all of the hboxes, only need to SetSizer for vbox
        pnl.SetSizer(vbox1)
        
        self.SetSize((600,400))
        self.SetTitle('wx.Slider')
        
    def OnSliderScroll(self, e):
        #Gets slider values
        obj = e.GetEventObject()
        val = obj.GetValue()
        self.txt.SetLabel('y = sin({}*t)'.format(str(val)))
        #After getting slider value, use plot method
        self.plotCanvasDraw()
    def plotCanvasDraw(self):
        #Clears pervious plot
        self.axes.clear()
        
        #Does new plot
        k = self.sld.GetValue()
        t = np.arange(-3.0, 3.0, 0.05)
        s = np.sin(k* t)
        self.axes.plot(t, s)
        self.plotCanvas.draw()
        
    def closeWindow(self,e):
        self.Close(True) 
      
def main():
    
    app = wx.App()
    Window(None)
    app.MainLoop()    

if __name__ == '__main__':
    main()   