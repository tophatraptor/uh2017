from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read, write
#import matplotlib.pyplot as plt


def plotSpec(y,Fs):
    n = len(y) 
    k = arange(n)
    T = n/Fs
    frq = k/T 
    frq = frq[range(n//2)] 

    Y = fft(y)/n 
    Y = Y[range(n//2)]
 
    plot(frq,abs(Y),'r') 
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')


Fs = 150

rate,data=read('pps.wav')
y=data[:,1]
timp=len(y)/150.
t=linspace(0,timp,len(y))

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpec(y,Fs)
show()

"""
rate,data = read('pps.wav')

y = data[:,1]
print(y)

F = fft(y) / (len(y))
print(F)
#plt.plot(y)
#plt.show()
"""
