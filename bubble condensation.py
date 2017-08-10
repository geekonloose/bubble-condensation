
from matplotlib import pyplot as plt


V0 = 3.14 #given H/D ratio is 1, Radius is 3.14
Lf = 1530E3 # Latent Heat of vaporisation
rhos = (1150*1000)/(3.14*6.75**2*13.5) #density of sodium at 500
mu = 243.0 # Dynamic viscocity at 500C
nu = mu/rhos #kinetic viscosity
Tsodium = 773 #temperature of sodium K
Tfsat = 3500 #boiling temperature of fuel
k = 90.6038-0.048523*(Tsodium-273)
beta = 2.8867E4
Pr = 0.0046
Rad = ((V0*3)/(3.14*4))**(1/3.0)
L=Rad/3.0   # characteristic length
T = 3500 # temperature at which rho to be found
rho = 10970 # density of fuel


h = 1E6


## Calculation for the rho at temperature T



## Initilisation of list variables

pr = [] # pressure of the bubble
mf = [8250.0] # mass of fuel vapor in kg
vf = [3.14,3.14] # volume vapor bolume
rf = [] # radius of fuel vapor bubble
dmf = [] # dm/dt
sum_mf = 0
time = [i for i in range(0,2)]


for i in time:
#    print('i',i)

#    vf.append(mf[i]/rho)
    rf.append((3*vf[i]/(4*3.14))**(1.0/3))
    dmf.append((4*3.14*rf[i]**2*h*(Tfsat-Tsodium))/Lf)
    sum_mf = sum_mf + dmf[i]
    mf.append(mf[0] - sum_mf)



# print(pr)

plt.plot(time,mf[0:-1],color='red',label='mass of fuel')
plt.xlabel('time (seconds)',color='b',fontsize='14')
plt.ylabel('mass of fuel (kg)',color='b',fontsize='14')
plt.legend(fontsize='15')
plt.axis([0,0.5,0,9000])
plt.grid()
plt.show()
plt.savefig('final')
#calculation for velocity

g=9.8
d= 2*rf[i]
rho = 8250/3.14 #mass of fuel/volume of fuel
vb = (0.14425*g**(5.0/6.0) *(rhos/mu)**(2.0/3.0) * d**(3/2.0))

print('vb\t{:0.3e}'.format(vb))