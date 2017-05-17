
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
        
        #Layout
        pnl = wx.Panel(self)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)        
        #Setting up plotting axes
        self.fig = plt.figure(figsize=(4,3))
        self.axes = self.fig.add_subplot(111,xlim = (-3,3),ylim = (-2,2))
        
        #Use plotCanvas in subsequent methods
        self.plotCanvas = FigureCanvas(pnl,id = -1,figure=self.fig)
        vbox1.Add(self.plotCanvas)
        
        #Defines static text for slider value
        self.txtk = wx.StaticText(pnl, label='k', pos=(20, 90))
        self.txtt = wx.StaticText(pnl, label='t', pos=(20, 90))               
        
        hbox1.Add(self.txtk,flag = wx.ALIGN_RIGHT)
        hbox2.Add(self.txtt,flag = wx.ALIGN_RIGHT)
        
        #Defines slider for interaction
        sldkLow,sldkHigh = 1,5
        sldtLow,sldtHigh = -20,20
        self.sldk = wx.Slider(pnl, value=sldkLow, minValue=sldkLow, maxValue=sldkHigh, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL)
        self.sldk.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        
        self.sldt = wx.Slider(pnl, value=sldtLow, minValue=sldtLow, maxValue=sldtHigh, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL)
        self.sldt.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        
        #After slider is defined, initialize the drawing 
        self.lines, = self.axes.plot([],[],lw = 3,c= 'k')
        self.plotCanvasDraw()
        
        hbox1.Add(self.sldk,flag = wx.ALIGN_LEFT)
        hbox2.Add(self.sldt,flag = wx.ALIGN_LEFT)
        
        
        
        vbox1.Add(hbox1)
        vbox1.Add(hbox2)
        
        #Closing button
        self.buttonClose = wx.Button(pnl, label="Exit",style=wx.ALIGN_CENTRE)
        self.buttonClose.Bind(wx.EVT_BUTTON, self.closeWindow)
        hbox3.Add(self.buttonClose)
        
        #Remove plot
        self.removeButton = wx.Button(pnl, label="Remove plot",style=wx.ALIGN_CENTRE)
        self.removeButton.Bind(wx.EVT_BUTTON, self.removePlot)
        hbox3.Add(self.removeButton)
        
        
        vbox1.Add(hbox3)
        
        
        
        #vbox contains all of the hboxes, only need to SetSizer for vbox
        pnl.SetSizer(vbox1)
        
        self.SetSize((600,400))
        self.SetTitle('wx.Slider')
        
    def OnSliderScroll(self, e):
        #Gets slider values
        
#        obj = e.GetEventObject()
#        val = obj.GetValue()
#        self.txtt.SetLabel('{}'.format(str(val)))
#        
        #After getting slider value, use plot method
        self.plotCanvasDraw()
        
    def plotCanvasDraw(self):
        #Clears pervious plot
        
        #Does new plot
        
        k = self.sldk.GetValue()
        t = self.sldt.GetValue()
        
        x = np.arange(-3.0, 3.0, 0.05)
        
        y = np.sin(k*x + t)

        self.lines.set_data(x,y)
            
        self.plotCanvas.draw()
        
    def removePlot(self):
#        self.fig.Axes().clear()
#        self.plotCanvas.draw()        
        pass
    
    def closeWindow(self,e):
        self.Close(True) 
      
def main():
    
    app = wx.App()
    Window(None)
    app.MainLoop()    
    exit()

if __name__ == '__main__':
    main()   