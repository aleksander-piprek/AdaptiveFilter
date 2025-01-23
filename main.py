import numpy as np
from LMS import LMS
import matplotlib.pyplot as plt

def main():
    desiredSignal_x = np.arange(0, 10*np.pi, 0.01)
    desiredSignal = np.sin(desiredSignal_x)

    noiseSignal = np.random.normal(0, 1, len(desiredSignal_x))
    inputSignal_x = np.arange(0, 10*np.pi, 0.01)
    inputSignal = np.sin(inputSignal_x) + noiseSignal

    outputSignal = LMS(inputSignal, desiredSignal)

    plt.subplot(3,1,1)
    plt.plot(inputSignal)
    plt.subplot(3,1,2)
    plt.plot(desiredSignal)
    plt.subplot(3,1,3)
    plt.plot(outputSignal)
    plt.show()

if __name__ == "__main__":
    main()