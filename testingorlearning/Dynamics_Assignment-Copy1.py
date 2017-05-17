
# coding: utf-8

# In[29]:

import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt

#My notation used in this entire assignment
X = imread('DSC_0208.JPG')
plt.imshow(X)
plt.show()


# In[30]:

#Link lengths
l2,l3,l4,l1 = 0.08,0.21,0.18,0.23
#Masses
m2,m3,m4 = 0.18,7.00,16.00
#Assumed given moments of inertia are around the centre of mass of the respective links
I2,I3,I4 = 0.04,0.09,0.04
#Angles of centre of masses, wrt the associated linkages 
d2,d3,d4 = 35,65,40
#Distances of centre of masses
rg2,rg3,rg4= 0.02,0.08,0.05

#Applied torques
T3,T4= 5,8
#Vectors of applied forces
#Distances of applied forces wrt CG
rp3,rp4=0.2,0.2
#Applied forces magnitudes
fp3,fp4 = 45,80
#Angles of applied forces wrt the CG
dfp3,dfp4=50,60
drp3,drp4=60,30

#Angles of linkages
#All angles are converted to radians as numpy likes radians not degrees
ID = '7665245'
th2 = int(ID[-2:])
dth2 = -25
ddth2 = 25
th1 = 20

print(th2)


# In[31]:

th2 = th2 - th1
th1 = np.deg2rad(th1)
th2 = np.deg2rad(th2)


# 
# Use fruedenstein equations for fourbar linkages to find th3,th4 

# In[32]:

MODE = 'open'#Open configuration assumed

K1 = l1/l2
K2 = l1/l4
K3 = (l2**2-l3**2+l4**2+l1**2)/(2*l2*l4)
A = np.cos(th2) - K1 - K2*np.cos(th2) + K3
B = -2*np.sin(th2)
C = K1 - (K2+1)*np.cos(th2) + K3
disc = (B**2)-4*A*C 
if MODE =='open':
    th4 = 2*np.arctan((-B - np.sqrt(disc) )/(2*A))
else:
    th4 = 2*np.arctan((-B + np.sqrt(disc) )/(2*A))


# In[33]:

K4 = l1/l3
K5 = (-l2**2-l3**2+l4**2-l1**2)/(2*l2*l3)
D = np.cos(th2) - K1 + K4*np.cos(th2) + K5
E = -2*np.sin(th2)
F = K1 + (K4-1)*np.cos(th2) + K5
disc = (E**2)-4*D*F 
if MODE =='open':
    th3 = 2*np.arctan((-E - np.sqrt(disc) )/(2*D))
else:
    th3 = 2*np.arctan((-E + np.sqrt(disc) )/(2*D))


# #Add th1 back into all other angles
# th2 += th1
# th3 += th1
# th4 += th1
# #print th1,th2... in degrees
# print(np.rad2deg([th1,th2,th3,th4]))

# In[34]:

from numpy import sin as sin
from numpy import cos as cos
from numpy import pi as pi

dth3 = l2*dth2*sin(th4-th2)/(l3*np.sin(th3-th4))
dth4 = l2*dth2*sin(th2-th3)/(l4*np.sin(th4-th3))

#Angular velocities of linkages
print('th3 {}'.format(dth3),'\n','th4 {}'.format(dth4))


# In[35]:

A = l4*sin(th4)
B = l3*sin(th3)
C = l2*ddth2*sin(th2)+l2*cos(th2)*dth2**2 + l3*cos(th3)*dth3**2 - l4 * cos(th4)*dth4**2
D = l4*cos(th4)
E = l3*cos(th3)
F = l2*ddth2*cos(th2)-l2*sin(th2)*dth2**2 - l3*sin(th3)*dth3**2 + l4 * sin(th4)*dth4**2
ddth3 = (C*D-A*F)/(A*E-B*D)
ddth4 = (C*E-B*F)/(A*E-B*D)
print(ddth3,'\n',ddth4)


# #Angular acceleration
# 
# #TODO: Needs to be calculated
# 
# A = np.array([
#         [-b*sin(th3),c*sin(th4)],
#         [b*cos(th3),-c*cos(th4)]
#     ])
# 
# B = np.array([cos(th3),sin(th3)])*dthb**2 + np.array([cos(th4),sin(th4)])*dthc**2 + np.array([cos(th2),sin(th2)]) * dtha**2
# - np.array([-sin(th2),cos(th2)])*ddtha
# 
# ddthb,ddthc = np.linalg.inv(A) @ B
# #Angular acceleration of linkages
# ddthb,ddthc

# In[28]:

#Convert all angles to radians
d2,d3,d4 = np.deg2rad(np.array([d2,d3,d4]))
dfp3,dfp4,drp3,drp4 = np.deg2rad(np.array([dfp3,dfp4,drp3,drp4]))


# In[11]:

def param2vec(angle,distance):
    compx = distance * np.cos(angle)
    compy = distance * np.sin(angle)
    return np.array([compx,compy])


# In[12]:

X=imread('FBDa.jpeg')
plt.imshow(X)
plt.show()


# In[13]:

#linkage a
Rga_1 = param2vec(d2+th2, ga)
R2_1 = param2vec(th2,a)
R2_ga = R2_1 - Rga_1


# In[14]:

X=imread('FBDb.jpeg')
plt.imshow(X)
plt.show()


# In[25]:

#linkage b
Rgb_2 = param2vec(ag3+th3,gb)
R3_2 = param2vec(th3,b)
R3_gb = R3_2-Rgb_2
#Applied forces on b
Rpb_gb = param2vec(aRpb+th3,Rpb)
Fpb = param2vec(aFpb,fpb)
#Cross product
Tpb = np.cross(Rpb_gb,Fpb)
Tpb


# In[34]:

R0 = Rgb_2 + Rpc
R = np.linalg.norm(R0)
Rangle = np.arctan(R0[1]/R0[0])


# In[35]:

print(R)
print(np.rad2deg(Rangle))


# In[16]:

X=imread('FBDc.jpeg')
plt.imshow(X)
plt.show()


# In[17]:

#linkage c
Rgc_4 = param2vec(ag4+th4,gc)
R3_4 = param2vec(th4,c)
R3_gc = R3_4 - Rgc_4
#Applied forces on c
Rpc_gc = param2vec(aRpc+th4,Rpc)
Fpc = param2vec(aFpc,fpc)
#Cross product
Tpc = np.cross(Rpc_gc,Fpc)
Tpc


# In[18]:

#Linear acceleration
#TODO: Needs to be calculated

def acceleration(r,omega,alpha):
    a1 = -r * omega**2
    a2 = np.cross([0,0,alpha],np.r_[r,0])
    #remove k vector from a2 as it will be 0
    acceleration = a1+a2[0:1]
    return acceleration
#linkage a an c expect eulerian + centripetal only as the linkage lengths do not change
#linkage b adds acceleration of point 2
ddg2 = acceleration(Rga_1,dth2,ddth2)
ddg3 = acceleration(Rgb_2,dth3,ddth3) + acceleration(R2_1,dtha,ddtha) 
ddg4 = acceleration(Rgc_4,dth4,ddth4)

ddga,ddgb,ddgc


# In[19]:

#Unknowns are as follows:

#[Fdax,Fday,Fbax,Fbay,Fbcx,Fbcy,Fdcx,Fdcy,Ta]
#In fourbar language [F12x,F12y,F32x,F32y,F43x,F43y,F]

#Which are all alligned along +x or +y or +z
#Ta is the input torque!
#9 unknowns, nine rows, 9 equations
#6 f=ma,3 t=Ia
#Assumed all accelerations are positive, +x or +y
#Assumed all angular accelerations are ccw, +z

Lmatrix = np.array(
    [
        [1,0,1,0,0,0,0,0,0],
        [0,1,0,1,0,0,0,0,0],
        [Rga_1[1],-Rga_1[0],-R2_ga[1],R2_ga[0],0,0,0,0,1],
        [0,0,-1,0,-1,0,0,0,0],
        [0,0,0,-1,0,-1,0,0,0],
        [0,0,-Rgb_2[1],Rgb_2[0],R3_gb[1],-R3_gb[0],0,0,0],   
        [0,0,0,0,1,0,1,0,0],
        [0,0,0,0,0,1,0,1,0],
        [0,0,0,0,-R3_gc[1],R3_gc[0],R3_gc[1],-R3_gc[0],0],   

    ]
    )

#Prettier printing of Lmatrix
import pandas as pd
pd.DataFrame(Lmatrix)


# Rmatrix contains the knowns

# In[20]:

Rmatrix = np.array(
    [
    [
        ma*ddga[0],
        ma*ddga[1],
        Ia*ddtha,
        mb*ddgb[0]-Fpb[0],
        mb*ddgb[1]-Fpb[1],
        Ib*ddthb-Tpb-Tb,
        mc*ddgc[0]-Fpc[0],
        mc*ddgc[1]-Fpc[1],
        Ic*ddthc-Tpc-Tc,
    ]
    ]
        ).T


# In[24]:

pd.DataFrame(Rmatrix)


# In[22]:

Lmatrixinv = np.linalg.inv(Lmatrix)
pd.DataFrame(Lmatrixinv)


# In[23]:

#Final answer to:
#[Fdax,Fday,Fbax,Fbay,Fbcx,Fbcy,Fdcx,Fdcy,Ta]

pd.DataFrame(Lmatrixinv @ Rmatrix)

