# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:36:29 2017

@author: John
asdftoger

"""
'''
This program plots the path of a follower attached to linkage b based on changing the lengths of linkages a and c
d is the ground link, abc follow clockwise from the left most joint
'''
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import cmath
def freudenstein(th_a):
    #Freudenstein equation gives us positions of follower
    K1 = d/a
    K4 = d/b
    K5 = (-a**2-b**2+c**2-d**2)/(2*a*b)
    D = np.cos(th_a) - K1 + K4*np.cos(th_a) + K5
    E = -2*np.sin(th_a)
    F = K1 + (K4-1)*np.cos(th_a) + K5
    disc = (E**2)-4*D*F 

    if MODE =='open':
        th_b = 2*np.arctan((-E - np.sqrt(disc) )/(2*D))
    else:
        th_b = 2*np.arctan((-E + np.sqrt(disc) )/(2*D))
    if not(np.greater_equal(disc,0).all()):
        #This extracts the th_a elements with discriminants > 0 and reruns the function.
        condition = np.greater_equal(disc,0)
        th_a = np.extract(condition, th_a)
        condition = np.less_equal(th_a, np.pi)
        th_a = np.extract(condition,th_a)
        freudenstein(th_a)
    
#    
    return th_b
    
def cost_function():
    #Use a quadratic cost function
    pass

#==============================================================================
# Change the following parameters for different follower shapes
#==============================================================================
#Save figure to PNG
savefig = True

#Keep follower linkage and ground linkage constant
b = 400
d = 500

#Change follower parameters
#Degrees
th_f = 40
#Length of follower from joint a-b to follower 
f = 200

#Linkage mode
ROTATION = 'cw'
MODE = 'open'

#na,nc define the number of linkage configurations to use
n1,n2 = 8,15

#Plot_Counter
cntr = 1
step = 300
#==============================================================================
# 
#==============================================================================

#linkages
a_linkages = np.linspace(100,200,n1)
c_linkages = np.linspace(300,700,n2)
#Rounding the decimals
a_linkages = np.round(a_linkages,1)
c_linkages = np.round(c_linkages,1)

#Tick labels, set to 0 to remove ticks
#label_size = int((n1+n2)/4)
#label_size = 0
#
#mpl.rcParams['xtick.labelsize'] = label_size 
#mpl.rcParams['ytick.labelsize'] = label_size 


for a in a_linkages:
    for c in c_linkages:
        
        
        th_a = np.linspace(0,2*np.pi,step)
        th_b = freudenstein(th_a)
        
        #e^jtheta1 gives R vectors
        phase1 = [cmath.exp(1j*i) for i in th_a]
        R1 = a*np.array(phase1)
        
        #FOllower angle wrt ground. th_f + th_b
        th_follower = th_f*np.pi/180 + th_b
        
        #Phase of follower 
        phasef = [cmath.exp(1j*i) for i in th_follower]
        Rf = R1+ f*np.array(phasef)
        xf,yf = np.real(Rf),np.imag(Rf)
        
        #plotting
        

        plt.subplot(n1,n2, cntr)
#        plt.title('{},{}'.format(a,c),size = 5)
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off') # labels along the bottom edge are off
        plt.tick_params(
            axis='y',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off') # labels along the bottom edge are off

        plt.plot(xf,yf)
#        plt.axis('off')
#        plt.tight_layout()
        cntr += 1
        
        pass
    pass

#SAves fugyre
if savefig:
    a1,a2 = a_linkages[0],a_linkages[-1]
    c1,c2 = c_linkages[0],c_linkages[-1]
    a1,a2 = int(a1),int(a2)
    c1,c2 = int(c1),int(c2)


    title = 'Follower_path_a_{}-{},c_{}-{}_b{}_d{}.png'.format(a1,a2,c1,c2,b,d)
    plt.savefig(title,dpi = 1000)
    
plt.show()
