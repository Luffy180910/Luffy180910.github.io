# %%
a=-1+1j
import matplotlib.pyplot as plt

from matplotlib import colors
from numpy import *


# %%
def mi(p,n):
    if(n==0):
        return
    plt.plot(real(p),imag(p),'1')
    plt.plot(real(p+a**n),imag(p+a**n),'1')
    mi(p,n-1)
    mi(p+a**n,n-1)

# %%
mi(0,10)

plt.ylabel('Imaginary')
plt.xlabel('Real')

plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.show

# %%



