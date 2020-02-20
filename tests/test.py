from ctwavelet import LiftingScheme
import unittest


class TestLiftingScheme(unittest.TestCase):
    def test_one_signal_period(self):
        ls = LiftingScheme.LiftingScheme()
        ls.apply([8, 8, 8, 8])
        coeffs = ls.get_wavelet_coefficients()
        self.assertEqual(coeffs, [8.0, 0.0, 0.0, 0.0])

    def test_different_lenght_periods(self):
        ls = LiftingScheme.LiftingScheme()
        ls.apply([0, 1, 2, 3, 4, 3, 2, 1])
        coeffs = ls.get_wavelet_coefficients()
        self.assertEqual(coeffs, [2.0, -0.5, -1.0, 1.0, -0.5, -0.5, 0.5, 0.5])

    def test_inverse(self):
        ls = LiftingScheme.LiftingScheme()
        arr = [0, 1, 2, 3, 4, 3, 2, 1]
        ls.apply(arr)
        coeffs = ls.get_wavelet_coefficients()
        inverse = ls.inverse(coeffs)
        self.assertEqual(inverse, arr)

    def test_hpf(self):
        ls = LiftingScheme.LiftingScheme()
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([1.5, 3.5, 5.5, 7.5], ls._hpf(arr))

    def test_lpf(self):
        ls = LiftingScheme.LiftingScheme()
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([-0.5, -0.5, -0.5, -0.5], ls._lpf(arr))

    def test_long_ranges(self):
        ls = LiftingScheme.LiftingScheme()
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] * 2
        ls.apply(arr)
        coeffs = ls.get_wavelet_coefficients()


if __name__ == '__main__':
    unittest.main()
