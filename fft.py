from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import pylab
import numpy
import matplotlib.image as mpimg


numpy.set_printoptions(threshold=numpy.nan)
rate,data = read('ds.wav')
spectrum, freqs, t, im = plt.specgram(data[:,1], NFFT=200, Fs=44100, noverlap=100)


i = 1
numpy.savetxt('./ds-heat/t.txt', t)
numpy.savetxt('./ds-heat/freqs.txt', freqs)
for row in spectrum:
    name = './ds-heat/heat' + str(i) + '.txt'
    numpy.savetxt(name, row)
    i += 1


maxes = numpy.amax(spectrum, axis=0)
inds = numpy.argmax(spectrum, axis=0)
numpy.savetxt('./maxes.txt', maxes)
numpy.savetxt('./inds.txt', inds)


maxes = numpy.amax(spectrum, axis=0)
inds = numpy.argmax(spectrum, axis=0)
numpy.savetxt('./maxes.txt', maxes)
numpy.savetxt('./inds.txt', inds)
plt.show()
plt.savefig('heat.png')
