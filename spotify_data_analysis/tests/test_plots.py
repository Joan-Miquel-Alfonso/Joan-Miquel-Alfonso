import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest
from plots import scatter, plot_maker, hist_maker, heat_map

# creem la classe TestPlot per fer els unittest
class TestPlot(unittest.TestCase):

    # comprovem que les gràfiques funcionen implementant els valors correctes
    def test_scatter_valid(self):
        dic1 = {1: 2, 2: 3, 3: 4}
        dic2 = {1: 4, 2: 6, 3: 12}
        scatter(dic1, dic2)

    def test_plot_valid(self):
        dictionary = {1: 2, 2: 3, 3: 4}
        plot_maker(dictionary, "x", "y")


if __name__ == "__main__":
    # fem funcionar el nostre unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPlot)
    unittest.TextTestRunner(verbosity=2).run(suite)
