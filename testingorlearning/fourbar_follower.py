
# coding: utf-8

# Created by Brandon Lay
# asdftoger@gmail.com
# 
# 
#This program is an inverse kinematics program that uses a cost function to match the follower of best fit

import matplotlib.pyplot as plt
import numpy as np
import cmath



a,b,c,d = 230,350,300,400


#Change follower parameters
#Degrees
Angle = 40
Angle_cg = Angle-20

#Relative magnitude, NOT ABSOLUTE LENGTH
Len = 0.5
Len_cg = 0.4


ROTATION = 'cw'
MODE = 'open'

#Lengths of the linkages, 
#a,b,c,d represent linkages starting from left fixed and going clockwise
#makes sure that the grashoff condition is satisfied
#Since linkage a is the driving linkage, b+c must be greater than a+d

#the angle that the linkages make wrt xaxis of the fixed points a,d
#step controls how fast the linkage drives
step = 0.01
if ROTATION == 'cw':
    th_a = np.arange(2*np.pi,0,-step*np.pi)
else:
    th_a = np.arange(0,2*np.pi,step*np.pi)

#Degrees, used for drawing arcs
th_a_d = th_a * 180/np.pi
len(th_a)



#Freudenstein equation

K1 = d/a
K2 = d/c
K3 = (a**2-b**2+c**2+d**2)/(2*a*c)
A = np.cos(th_a) - K1 - K2*np.cos(th_a) + K3
B = -2*np.sin(th_a)
C = K1 - (K2+1)*np.cos(th_a) + K3

#Grashoff condition
disc = (B**2)-4*A*C 

#If any negative elements, the linkage is non-grashoff. 
if not(np.greater_equal(disc,0).all()):

    condition = np.greater_equal(disc,0)
    th_a = np.extract(condition, th_a)
    condition = np.less_equal(th_a, np.pi)
    th_a = np.extract(condition,th_a)
    th_a
    #Repeat the pattern as many times specified

    #np.flipud flips left to right
    #np.r_ concatenate lengthwise
    #np.tile repeats
    th_a = np.tile(np.r_[th_a,np.flipud(th_a)],repeat)

    #Redoing Freudenstein equation

    K1 = d/a
    K2 = d/c
    K3 = (a**2-b**2+c**2+d**2)/(2*a*c)
    A = np.cos(th_a) - K1 - K2*np.cos(th_a) + K3
    B = -2*np.sin(th_a)
    C = K1 - (K2+1)*np.cos(th_a) + K3

    #Grashoff condition
    disc = (B**2)-4*A*C 

    #Which elements are greater than 0? some are expected negative for non-grashoff
    # np.greater_equal(disc,0)


if MODE =='open':
    th_c = 2*np.arctan((-B - np.sqrt(disc) )/(2*A))
else:
    th_c = 2*np.arctan((-B + np.sqrt(disc) )/(2*A))
    

#Degrees, used for drawing arcs
th_c_d = th_c * 180/np.pi
th_d = -np.pi*np.ones(len(th_c))


phase1 = [cmath.exp(1j*i) for i in th_a]
phase3 = [cmath.exp(1j*i) for i in th_c]
phase4 = [cmath.exp(1j*i) for i in th_d]



R1 = a*np.array(phase1)
R3 = c*np.array(phase3)
R4 = -d*np.array(phase4)



x1,y1 = np.zeros(len(R1)),np.zeros(len(R1))
x2,y2 = np.real(R1),np.imag(R1)
x3,y3 = np.real(R3+R4),np.imag(R3+R4)
x4,y4 = np.real(R4),np.imag(R4) 


# In[173]:

th_b = np.arctan2((y3-y2),(x3-x2))
# th_b = (th_b + 2*np.pi ) % 2*np.pi

phase2 = [cmath.exp(1j*i) for i in th_b]
R2 = b*np.array(phase2)




# In[175]:


#Creating angle of the follower wrt ground

f_d = Angle*np.pi/180*np.ones(len(th_a))
f_d += th_b

f_dCG = Angle_cg*np.pi/180*np.ones(len(th_a))
f_dCG += th_b
#Follower size
f = Len*b
fCG = Len_cg*b


# In[176]:

#Phase of follower 
phasef = [cmath.exp(1j*i) for i in f_d]
Rf = R1+ f*(np.array(phasef))
xf,yf = np.real(Rf),np.imag(Rf)

#Phase of follower centre of gravity
phasef_CG = [cmath.exp(1j*i) for i in f_dCG]
Rf_CG = R1+ fCG*(np.array(phasef_CG))
xfg,yfg = np.real(Rf_CG),np.imag(Rf_CG)

