import numpy as np
import matplotlib.pyplot as plt

"""
Adaptive filter using the Least Mean Squares (LMS) algorithm.

Parameters:
    desired_signal (numpy array): The desired output signal.
    input_signal (numpy array): The input signal to the filter.
    mu (float): The step size for the LMS algorithm (controls convergence speed and stability).
    num_taps (int): The number of filter coefficients (taps).

Returns:
    numpy array: The output signal of the adaptive filter.
    numpy array: The error signal (difference between desired and output signals).
    numpy array: The final filter coefficients.
"""
def adaptive_filter_lms(desired_signal, input_signal, mu, num_taps):
    weights = np.zeros(num_taps)
    n_samples = len(input_signal)

    output_signal = np.zeros(n_samples)
    error_signal = np.zeros(n_samples)

    for n in range(num_taps, n_samples):
        x = input_signal[n - num_taps:n][::-1]

        y = np.dot(weights, x)
        output_signal[n] = y

        e = desired_signal[n] - y
        error_signal[n] = e

        weights += 2 * mu * e * x

    return output_signal, error_signal, weights

if __name__ == "__main__":
    np.random.seed(42)
    n_samples = 500
    t = np.linspace(0, 1, n_samples)
    input_signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.normal(size=n_samples)

    desired_signal = np.sin(2 * np.pi * 5 * t)

    mu = 0.01 
    num_taps = 10 
    output_signal, error_signal, final_weights = adaptive_filter_lms(
        desired_signal, input_signal, mu, num_taps)

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(t, desired_signal, label="Desired Signal", linestyle="dashed")
    plt.plot(t, input_signal, label="Input Signal")
    plt.title("Input and Desired Signals")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, output_signal, label="Output Signal")
    plt.title("Output Signal")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, error_signal, label="Error Signal")
    plt.title("Error Signal")
    plt.legend()

    plt.tight_layout()
    plt.show()
