import numpy as np

def LMS(inputSignal, desiredSignal):
    mu = 0.001 
    num_taps = 25 

    weights = np.zeros(num_taps)

    n_samples = len(inputSignal)

    output_signal = np.zeros(n_samples)
    error_signal = np.zeros(n_samples)

    for n in range(num_taps, n_samples):
        x = inputSignal[n - num_taps:n][::-1]

        y = np.dot(weights, x)
        output_signal[n] = y

        e = desiredSignal[n] - y
        error_signal[n] = e

        weights += 2 * mu * e * x

    return output_signal