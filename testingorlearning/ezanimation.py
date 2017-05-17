# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:03:47 2017

@author: John
asdftoger

"""
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

class my_animation():
    
    def __init__(self):
        
        #Get animation values, for mins and maxes
        self.data = self.animating_function()
        
        #Draw axes limits
        self.fig = plt.figure()
        
        temp = self.data[0]
        xmin = np.amin([np.amin(mini) for mini in temp])
        xmax = np.amax([np.amax(mini) for mini in temp])
        temp = self.data[1]
        ymin = np.amin([np.amin(mini) for mini in temp])
        ymax = np.amax([np.amax(mini) for mini in temp])
        
        bord = 1
        self.axes = plt.axes(xlim=(xmin-bord, xmax+bord), 
                             ylim=(ymin-bord, ymax+bord))
        #Generate the lines data
        self.lines, = self.axes.plot([],[],lw = 5,c = 'k')
        
        #Generate animation
        self.gen_animation()
        pass
    
    def initialize_animation(self):
        self.lines.set_data([],[])
        #line, returns a tuple, NOT matplotlib object
        return self.lines,
    def animating_function(self):
        #Returns x:data[0], y:data[1]
        x = np.linspace(0,5)
        y = np.sin(x)        
        data = np.array([x,y])

        return data
        
    def update(self,t):
        self.lines.set_data(self.data[::,t])
        
    
    
    def gen_animation(self):
        animation.FuncAnimation(self.fig, self.update, len(self.data[0]), fargs=None,
                                   interval=50, blit=False,init_func=initialize_animation)
        plt.show()
        
a = my_animation()  