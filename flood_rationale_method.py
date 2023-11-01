#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def peak_runoff(C, i, A):
    """
    Calculate the peak runoff using the Rational Method.

    Parameters:
    - C: Runoff coefficient (dimensionless)
    - i: Rainfall intensity (mm/hr)
    - A: Catchment area (km^2)

    Returns:
    - Q: Peak runoff rate (m^3/s)
    """
    Q = C * i * A * 1000 / (60 * 60)  # Conversion factor for mm/hr and km^2 to m^3/s
    return Q

