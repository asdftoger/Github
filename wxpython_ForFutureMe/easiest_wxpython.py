'''
The simplest possible wxpython script.
'''
import wx
class Frame(wx.Frame):
    def __init__(self, parent,title):
        #Parent: parent frame
        #Title; App title
        wx.Frame.__init__(self,parent = parent, title = title)
        self.Centre()
        #Like plt.show()
        self.Show(True)          
    def OnClose(self, e):
        self.Close(True)                  
        
def main():
    app = wx.App()
    Frame(None)
    app.MainLoop()    


if __name__ == '__main__':
    main()   