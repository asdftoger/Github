'''
This script shows how to embed a matplotlib plot inside a wx frame
'''

import wx
import numpy as np


#Plotting libraries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx


class MainWindow(wx.Frame):
    def __init__(self, parent=None,title=''):
        wx.Frame.__init__(self,parent = parent, title = title,size  = (600,400))   
        
        #i is the counted number
        self.i = 0
        
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.p1 = wx.Panel(self)
        self.p2 = wx.Panel(self)
        
        #Closing button
        self.buttonClose = wx.Button(self.p2, label="Close App",style=wx.ALIGN_CENTRE)
        self.buttonClose.Bind(wx.EVT_BUTTON, self.closeWindow)
          
        
        
        
    
#        Plotting
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111)
        #parent = self.f1 puts the figure inside the frame  
        self.plotCanvas = FigureCanvas(parent = self.p1,id = -1,figure=self.fig)
        self.sinePlot()
        
        self.hbox1.Add(self.p1, 1, wx.ALL, 20)
        self.p1.SetSizer(self.hbox1)
        
        self.hbox1.Add(self.p2, 1, wx.ALL, 20)
        self.p1.SetSizer(self.hbox1)
        
        #Like plt.show()
        self.Centre()
        self.Show()
        
    def sinePlot(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.scatter(t, s)

    def closeWindow(self,e):
        self.Close(True)    
        
#        self.f1.sinePlot()
def main():
    app = wx.App()
    
    MainWindow(None,'__main__')
    app.MainLoop()

        
if __name__== '__main__':
        
    main()