import math
import functools


class LiftingScheme:
    def __init__(self):
        self.result_arr = []
        self.array = []

    def _hpf(self, arr):
        result = []
        for i in range(0, len(arr), 2):
            result.append(sum(arr[i:i + 2]) / 2)
        return result

    def _lpf(self, arr):
        result = []
        for i in range(0, len(arr), 2):
            t_arr = arr[i:i + 2]
            result.append((t_arr[0] - t_arr[1]) / 2)
        return result

    def _apply(self, arr):
        self.result_arr.append(arr)
        if len(arr) == 1:
            return arr
        a = self._apply(self._hpf(arr))
        b = self._apply(self._lpf(arr))
        return a, b

    def apply(self, arr):
        self.result_arr = []
        self.array = arr
        return self._apply(arr)

    def get_wavelet_coefficients(self):
        c = []
        size = 1
        d = False
        for element in self.result_arr:
            if len(element) == size:
                if d == False:
                    d = True
                else:
                    size *= 2
                for item in element:
                    c.append(item)
        return c

    def __parse_coeffs(self, array):
        last = []
        index = 1
        last.append([array[0]])
        for item in range(int(math.log2(len(array)))):
            last.append(array[index:index + 2 ** item])
            index = index + 2 ** item
        return last

    def __reduce(self, arr1, arr2):
        reduced = []
        for i in range(len(arr1)):
            a_sum = arr1[i] + arr2[i]
            a_dfif = arr1[i] - arr2[i]
            reduced.append(a_sum)
            reduced.append(a_dfif)
        return reduced

    def inverse(self, array):
        parsed_coeffs = self.__parse_coeffs(array)
        return functools.reduce(self.__reduce, parsed_coeffs)
