from ctwavelet import LiftingScheme
import unittest

class TestLiftingScheme(unittest.TestCase):

    def test_one_signal_period(self):
        ls = LiftingScheme.LiftingScheme()
        ls.apply([8,8,8,8])
        coeffs = ls.get_wavelet_coefficients()
        self.assertEqual(coeffs, [8.0, 0.0, 0.0, 0.0])
    
    def test_different_lenght_periods(self):
        ls = LiftingScheme.LiftingScheme()
        ls.apply([0,1,2,3,4,3,2,1])
        coeffs = ls.get_wavelet_coefficients()
        self.assertEqual(coeffs, [2.0,-0.5,-1.0,1.0,-0.5,-0.5, 0.5, 0.5])

    def test_get_coeff_pos(self):
        ls = LiftingScheme.LiftingScheme()
        positions = ls.get_coeff_positions([0,1,2,3,4,3,2,1])
        self.assertEqual(positions,[3,4,5,8])

    def test_inverse(self):
        ls = LiftingScheme.LiftingScheme()
        arr = [0,1,2,3,4,3,2,1]
        ls.apply(arr)
        coeffs = ls.get_wavelet_coefficients()
        inverse = ls.inverse(coeffs)
        self.assertEqual(inverse, arr)

if __name__ == '__main__':
    unittest.main()