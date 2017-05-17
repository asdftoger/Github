
# coding: utf-8

# README Future me
# 
# This notebook is a barebones animation notebook.
# Use this to plot beats, interference between two waves with similar frequencies and wavelengths

# In[19]:

#Standard libraries
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')


# In[20]:

#Setting up graph

fig = plt.figure()
ax = fig.add_subplot(111,autoscale_on= False,
                     xlim = (-np.pi,np.pi),ylim = (-3,3))


# In[21]:

#Setting up sine-wave

#This initializes the line object to x= [],y=[]

#IMPORT DISTINCTION IN PYTHON
#Try it fuure me if you don't believe me.
#line, --- means type(line) == matplolib
#line --- on the otherhand means type(line) == list

line, = ax.plot([],[],lw = 1,c= 'k')


# In[22]:

#the variable i denotes the value changing each frame of the animation

#Initializes the animation
def initialize_animation():
    line.set_data([],[])
    #line, returns a tuple, NOT matplotlib object
    return line,


# !!!Change the following parameters to produce different wave effects!!!
# 
# Packet wavelength ~ dk/k
# 
# Packet oscillation ~ k
# 
# Wave speed ~ dw/w
# 
# Packet speed ~ w

# In[1]:


k,dk,w,dw =  -3,0.3,-1,0.01



# In[ ]:




# In[24]:

#Number of linespace spacings
length = 250
x = np.linspace(-np.pi,np.pi,length)

#The frame generation function
def animate(t):    
    global length,x
    global k,dk,w,dw
    #omega is used for omega*t distance offset
    y1 = np.sin(2*np.pi*((k+dk)*x + (w + dw)*t))
    y2 = np.sin(2*np.pi*((k-dk)*x + (w - dw)*t))
    y = y1+y2
    line.set_data(x,y)
    return line,


# In[25]:

#Animation plotting libraries
import matplotlib.animation as animation


# In[26]:

#Genrating the animation

ani = animation.FuncAnimation(fig, animate, np.arange(1,len(x)), interval=30, blit=True, init_func=initialize_animation)

plt.show()

# In[27]:


#To save animation, comment out the sys.exit()
import sys
sys.exit()
    
#Save animation
Writer = animation.writers['ffmpeg']
writer = Writer(fps = 30,extra_args=['-vcodec', 'libx264'])
dpi = 100

ani.save('beats_animation.mp4', writer = writer,dpi = dpi)

