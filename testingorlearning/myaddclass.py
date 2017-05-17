import wx

class MainWindow(wx.Frame):
    def __init__(self, parent,title):
        wx.Frame.__init__(self,parent = parent, title = title,size  = (600,400))   
        
        #i is the counted number
        self.i = 0
        
        #Define splitting frame
        self.splitFrame = wx.SplitterWindow(self) 
        self.f1 = wx.Panel(self.splitFrame,style= wx.SUNKEN_BORDER)
        self.f2 = wx.Panel(self.splitFrame,style= wx.SUNKEN_BORDER)
        self.splitFrame.SplitHorizontally(self.f1,self.f2,100)
        
        #Adding button
        self.button1 = wx.Button(self.f1, label="Add one")
        self.button1.Bind(wx.EVT_BUTTON, self.addOne)
        
        #Closing button
        self.buttonClose = self.button1 = wx.Button(self.f2, label="Close App",style=wx.ALIGN_CENTRE)
        self.buttonClose.Bind(wx.EVT_BUTTON, self.closeWindow)
        
        #Text to change
        self.label = wx.StaticText(self.f1, label=str(self.i), style=wx.ALIGN_CENTRE)
        
        #Like plt.show()
        self.Show()
    
    def addOne(self, e):
        self.i = self.i + 1
        self.label.SetLabel(str(self.i))
        
    def closeWindow(self,e):
        self.Close(True)    
        
        
def main():
    app = wx.App()
    
    MainWindow(None,'AddmeApp')
    app.MainLoop()

        
if __name__== '__main__':
        
    main()