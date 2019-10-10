import math
import functools

class LiftingScheme:
    def __init__(self):
        self.result_arr = []
        self.array = []

    def _hpf(self, arr):
        result = []
        for i in range(0,len(arr),2):
            result.append(sum(arr[i:i+2])/2)
        return result

    def _lpf(self, arr):
        result = []
        for i in range(0,len(arr),2):
            t_arr = arr[i:i+2]
            result.append((t_arr[0]-t_arr[1])/2)
        return result

    def _apply(self, arr, branch="n", count = 0):
        self.result_arr.append(arr)
        if len(arr) == 1:
            return arr
        count = count + 1
        a = self._apply(self._hpf(arr),"h"*count,count)
        b = self._apply(self._lpf(arr),"l"*count,count)
        return a,b

    def apply(self,arr):
        self.result_arr = []
        self.array = arr
        branch="n"
        count = 0
        return self._apply(arr, branch, count)

    def get_wavelet_coefficients(self):
        coeffs = []
        positions = self.get_coeff_positions(self.array)
        for pos in positions:
            coeffs.append(self.result_arr[pos])

        last_coeffs = []
        for coeff in coeffs:
            if type(coeff) == type([]):
                for sub_coeff in coeff:
                    last_coeffs.append(sub_coeff)
            else:
                last_coeffs.append(coeff)
        
        return last_coeffs
    
    def get_coeff_positions(self,array):
        seed = int(math.log2(len(array)))
        cumdif = []
        positions = []
        for i in range(seed+1):
            cumdif.append(i*(i-1)+(i+1))
        
        positions.append(seed)
        for i in range(seed):
            positions.append(seed + cumdif[i])
        
        return positions

    
    def __parse_coeffs(self,array):
        last = []
        for item in range(int(math.log2(len(array)))):
            if item == 0:
                last.append([array[item]])
            else:
                last.append(array[item:2*item])
        last.append(array[2*item:])
    
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
        return functools.reduce(self.__reduce,parsed_coeffs)