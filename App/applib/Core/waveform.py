import numpy as np

from .constants import SAMPLE_RATE, TIME

T = TIME

t = np.linspace(0, T, int(T * SAMPLE_RATE), False)

sldr_list = [0 for _ in range(20)]

# returns the waveform from slider information
def variabledef(fund_freq) -> np.ndarray:

    harmonic_amp = [np.sin((i+2) * fund_freq * t * 2 * np.pi) for i in range(20)]

    resultant = np.sin(fund_freq * t * 2 * np.pi)

    for i, e in enumerate(sldr_list):
        resultant += e * harmonic_amp[i]

    return resultant

def freqassignfunc(num, value):
    sldr_list[(int(num) - 2)] = float(value)

def return_sldr_list():
    return sldr_list