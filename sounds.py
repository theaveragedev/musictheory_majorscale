import numpy as np 
import matplotlib.pyplot as plt 

# We take the frequencies of all the notes of the C major scale and make it a numpy array
c_major = np.array([261.63,293.66,329.63,349.23,392.00,440,493.88, 523.25])

# Divide the array with the fundamental frequency or the Tonic note to get the ratio of frequencies
ratio = c_major/261.63

print(ratio)

# DEfine the constant
pi = 3.14

# Create the time sequence
time = np.arange(0, 2*pi + 0.1, 0.1)

# Generate the notes with a simple sine wave which is the purest signal in terms of frequency
# A sine wave will have energy spike only in one frquency and zero everywhere else. Hence ideal for demostration of the musical theory
# Actual instruments have harmonics or "timbre" characteristic to it's sound
fundamental = np.sin(time)
second = np. sin(ratio[1]*time)
third = np.sin(ratio[2]*time)
fourth = np.sin(ratio[3]*time)
fifth = np.sin(ratio[4]*time)
sixth = np.sin(ratio[5]*time)
seventh = np.sin(ratio[6]*time)
octave = np.sin(2*time)


# Plot the wave on a graph and observe the pattern
plt.plot(time, fundamental, 'r-', label = 'sa')
plt.plot(time, second, 'g-', label = 're')
plt.plot(time, third, 'b-', label = 'ga')
plt.plot(time, fourth, 'c-', label = 'ma')
plt.plot(time, fifth, 'y-', label = 'pa')
plt.plot(time, sixth, 'k-', label = 'dha')
plt.plot(time, seventh, 'm-', label = 'ni')
plt.plot(time, octave, 'k.', label = 'sa+')

plt.grid()
plt.legend()
plt.show()
plt.savefig('major_scale_plot.png')

# Sa, Ga, Pa are consonance as these notes are integral multiples of the fundamental frequency (sa)
# Re, Ma, Dha and Ni are dissonant as they are not integral multiples and will create irregular waveforms when superimposed
# Just like in physics the choice of our reference frame decides the physical parameters 
# in music our choice of the fundamental frequency sets the feel of every other note with respect to it. 
# "And she's buying a stairway to heaven :)"