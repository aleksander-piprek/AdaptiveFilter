import numpy as np

def LMS(inputSignal, desiredSignal):
    # LMS parameters
    mu = 0.01  # Step size
    num_taps = 10  # Number of filter coefficients

    # Initialize filter weights (coefficients) to zero
    weights = np.zeros(num_taps)

    # Length of the input signal
    n_samples = len(inputSignal)

    # Initialize output and error signals
    output_signal = np.zeros(n_samples)
    error_signal = np.zeros(n_samples)

    # Main LMS algorithm loop
    for n in range(num_taps, n_samples):
        # Take a segment of the input signal (most recent samples)
        x = inputSignal[n - num_taps:n][::-1]  # Reverse for convolution

        # Compute the filter output
        y = np.dot(weights, x)
        output_signal[n] = y

        # Calculate the error
        e = desiredSignal[n] - y
        error_signal[n] = e

        # Update filter weights
        weights += 2 * mu * e * x

    return output_signal