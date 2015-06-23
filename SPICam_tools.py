# Needed packages
import numpy as np

'''
EXPOSURE TIME CALCULATOR FOR SPICAM IN ugriz
Takes in the magnitude, the desired signal-to-noise ratio
and the airmass of the target and returns an array of the
needed exposure time in the SPICam u' g' r' i' z' (SDSS) 
filters.  Based on the values and forumlae given on the APO
SPICam webpage.
'''

def exposuretime(m, snr, airmass):
    # c constant in ugriz
    c = np.array([21.38, 24.92, 24.93, 24.72, 23.43])
    
    # k constants in ugriz
    k = np.array([0.48, 0.19, 0.11, 0.04, 0.06])
    
    # flux calculation
    flux = 10.**( (m - c + k*(airmass-1))/(-2.5) )
    
    # simple flux counting SNR is assumed, so will simply return
    return (snr**2)/flux

