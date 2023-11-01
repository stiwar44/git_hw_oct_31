#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest # import the package for testing in python
from flood_rationale_method import peak_runoff  # import the function that is defined for flood prediction

class TestPeakRunoffFunction(unittest.TestCase):

    def test_peak_runoff_pass(self):
        # Test with known values
        self.assertAlmostEqual(peak_runoff(0.6, 50, 2), 16.666666666666668, places=5)

    def test_peak_runoff_fail(self):
        # Intentionally incorrect values for failure test
        self.assertAlmostEqual(peak_runoff(0.6, 50, 2), 16.7, places=5)

if __name__ == "__main__":
    unittest.main()

