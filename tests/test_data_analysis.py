import unittest
import pandas as pd
from src.data_analysis import getStat

class TestGetStat(unittest.TestCase):
    def setUp(self):
        # Create a small dataframe for testing
        data = {
            "GHI": [100, 150, 200],
            "DNI": [200, 250, 300],
            "DHI": [50, 75, 100],
            "ModA": [300, 350, 400],
            "ModB": [400, 450, 500],
            "Tamb": [25, 30, 35],
            "RH": [40, 45, 50],
            "WS": [10, 12, 14],
            "WSgust": [15, 17, 19],
            "WSstdev": [1, 1.5, 2],
            "WD": [90, 100, 110],
            "WDstdev": [5, 7, 9],
            "BP": [1010, 1020, 1030],
            "Cleaning": [1, 0, 1],
            "Precipitation": [0, 0.5, 1],
            "TModA": [50, 55, 60],
            "TModB": [60, 65, 70]
        }
        self.df = pd.DataFrame(data)

    def test_getStat(self):
        stats = getStat(self.df)
        self.assertIsInstance(stats, dict)
        self.assertEqual(stats["GHI"]["Mean"], "150.00")
        self.assertEqual(stats["GHI"]["Median"], "150.00")
        self.assertEqual(stats["GHI"]["Min"], "100.00")
        self.assertEqual(stats["GHI"]["Max"], "200.00")
        # Add more assertions for other columns as needed

if __name__ == '__main__':
    unittest.main()
