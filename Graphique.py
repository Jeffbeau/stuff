from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
from numpy import *
from numpy.fft import fft,ifft
from matplotlib.pyplot import figure


z_o   = linspace(-10,0,1000)
z_a   = linspace(0,10,1000)

del_a = 1
del_o = 2
U_a   = 1
V_a   = 1
U_o   = 0.5
V_o   = 0.5
f    = 1
del_U = U_a - U_o
del_V = V_a - V_o
Uo = []
Vo = []
Ua = []
Va = []
fxo = []
fyo = []
fxa = []
fya = []
for z in z_o:
    A = U_o + exp(z/del_o)*del_a/del_o*(1/(del_a/del_o + 1))*(del_U*cos(z/del_o)- del_V*sin(z/del_o))
    B = V_o + exp(z/del_o)*del_a/del_o*(1/(del_a/del_o + 1))*(del_U*sin(z/del_o)+del_V*cos(z/del_o))
    F = f/(2*del_o**2)*exp(z/del_o)*del_a/del_o*(1/(del_a/del_o + 1))*(del_U*(cos(z/del_o)/del_o-sin(z/del_o)/del_o)+del_V*(-cos(z/del_o)/del_o-sin(z/del_o)/del_o))
    G = f/(2*del_o**2)*exp(z/del_o)*del_a/del_o*(1/(del_a/del_o + 1))*(del_U*(cos(z/del_o)/del_o+sin(z/del_o)/del_o)+del_V*(cos(z / del_o)/del_o-sin(z/del_o)/del_o))

    Uo.append(A)
    Vo.append(B)
    fxo.append(F)
    fyo.append(G)

for z in z_a:
    C = U_a + exp(-z/del_a)*(-1/(del_a/del_o + 1))*(del_U*cos(z/del_a)+del_V*sin(z/del_a))
    D = V_a + exp(-z/del_a)*(-1/(del_a/del_o + 1))*(del_U*sin(z/del_a)-del_V*cos(z/del_a))
    H = f/(2*del_a**2)*exp(-z/del_a)*(-1/(del_a/del_o + 1))*(del_U*(-cos(z/del_a)/del_a-sin(z/del_a)/del_a)+del_V*(-cos(z/del_a)/del_a+sin(z/del_a)/del_a))
    J = f/(2*del_a**2)*exp(-z/del_a)*(-1/(del_a/del_o + 1))*(del_U*(cos(z/del_a)/del_a-sin(z/del_a)/del_a)+del_V*(-cos(z/del_a)/del_a - sin(z/del_a)/del_a))

    Ua.append(C)
    Va.append(D)
    fxa.append(H)
    fya.append(J)

figure(1)
line1 = plt.plot(Uo,z_o,label='U_ocean')
line2 = plt.plot(Ua,z_a,label='U_atmosphere')
line3 = plt.plot(Va,z_a,label='V_atmosphere')
line4 = plt.plot(Vo,z_o,label='V_ocean')
plt.title('Vitesse du vent et du courant en fonction de z')
plt.xlabel('Vitesse')
plt.ylabel('Profondeur')
plt.legend(loc='best')



plt.show()
figure(2)
line1 = plt.plot(fxo,z_o,label='U_ocean')
line2 = plt.plot(fxa,z_a,label='U_atmosphere')
line3 = plt.plot(fya,z_a,label='V_atmosphere')
line4 = plt.plot(fyo,z_o,label='V_ocean')
plt.title('flux du vent et du courant en fonction de z')
plt.xlabel('Vitesse')
plt.ylabel('Profondeur')
plt.legend(loc='best')



plt.show()
