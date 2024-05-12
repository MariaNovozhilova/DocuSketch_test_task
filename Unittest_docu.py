import unittest
import os
from Test_task import draw_plots


class MyTestCase(unittest.TestCase):
    def test_plot(self):
        draw_plots('{"max":{"0":8.5629388885,"1":52.6054373308}}', 'max')

        self.assertTrue(os.path.exists('plots'))
        self.assertTrue((os.listdir('plots')))

if __name__ == '__main__':
    unittest.main()