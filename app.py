import unittest
from main import calculate_pit 

class TestPITCalculation(unittest.TestCase):
    
    def test_income_5_million(self):
        # Gross 5,000,000 VND with 0 dependents -> Tax should be 0
        self.assertEqual(calculate_pit(5000000, 0), 0.0)
        
    def test_income_20_million(self):
        # Gross 20,000,000 VND with 0 dependents
        # Deductions = 15,500,000 -> Taxable = 4,500,000 (Bracket 1)
        # Tax = 4,500,000 * 5% = 225,000
        self.assertEqual(calculate_pit(20000000, 0), 225000.0)

    def test_high_income_with_dependents(self):
        # Gross 50,000,000 VND with 1 dependent
        # Deductions = 15,500,000 + 6,200,000 = 21,700,000
        # Taxable = 28,300,000 (Bracket 2)
        # Tax = (28,300,000 * 10%) - 500,000 = 2,330,000
        self.assertEqual(calculate_pit(50000000, 1), 2330000.0)

if __name__ == '__main__':
    unittest.main()
