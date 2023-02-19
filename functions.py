from constants import *

def V01(r):
    x=r/rm
    return e * (sympy.exp(-2 * b * (x - 1)) - 2 * sympy.exp(-b * (x - 1)))
def V02(r):
    x=r/rm
    return e*(b1+b2*(x-x1)+(x-x2)*(b3+(x-x1)*b4))
def V03(r):
    return -C0/r**6
def V2(r):
    return A2*sympy.exp(-alpha*r)-a2*C0/(r**6)
def V4(r):
    return A4*sympy.exp(-alpha*r)
def P2(x):
    return 0.5*(3*x**2-1)
def P4(x):
    return 1/8*(35*x**4-30*x**2+3)

def V10(r,th):
    return (V01(r)+V2(r)*P2(th)+V4(r)*P4(th))
def V20(r,th):
    return (V02(r)+V2(r)*P2(th)+V4(r)*P4(th))
def V30(r,th):
    return (V03(r)+V2(r)*P2(th)+V4(r)*P4(th))


def SamplePoint(min,max):
    return (min**3+np.random.random()*(max**3-min**3))**(1/3)
def SampleAngle(min,max):
    return min+np.random.random()*(max-min)

def H(V,Pr,PR,R,th):
    return Pr**2/(2*muO2)+PR**2/(2*muxeO2)+V(R,th)

def W(Prlim,PRlim,Rlim,thlim):
    return 4*pi*rO2**2*\
           2*pi/3*(Rlim[1]**3-Rlim[0]**3)*(thlim[1]-thlim[0])*\
           pi*Prlim[1]**2*\
           4/3*pi*PRlim[1]**3

def dihotomy(f,a,b,N=300):
    n=0
    while n!=N:
        n=n+1
        while True:
            try:
                if f.subs(x,a)*f.subs(x,(a+b)/2)<=0:
                    b=(a+b)/2
                else:
                    a=(a+b)/2
                break
            except TypeError: a=a+10**(-4)
    return (a+b)/2


def Zint(rmax):
    Rlim = [0.8482049*rm, rmax]
    thlim = [-1, 1]
    Prlim=[0,1]
    PRlim = [0, 1]
    R=SamplePoint(Rlim[0],Rlim[1])  #самплинг R
    if R/rm<=x1:
        V=V10
    elif R/rm>x2:
        V=V30
    else:
        V=V20
    thlim[1]=dihotomy(V(R,x),0,1)    #подбор пределов для th
    thlim[0]=-thlim[1]
    th=SampleAngle(thlim[0],thlim[1])   #самплинг th
    Prlim[1]=(2*muO2*(-V(R,th)))**0.5
    Pr=SamplePoint(Prlim[0],Prlim[1])
    PRlim[1]=(2*muxeO2*(-V(R,th)-Pr**2/(2*muO2)))**0.5
    PR = SamplePoint(PRlim[0], PRlim[1])
    fg=sympy.exp(-1/(T)*H(V,Pr,PR,R,th))
    wg=W(Prlim,PRlim,Rlim,thlim)
    return [fg,wg]