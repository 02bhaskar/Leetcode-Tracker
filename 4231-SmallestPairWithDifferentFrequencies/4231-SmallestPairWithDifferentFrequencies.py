# Last updated: 7/9/2026, 3:05:17 PM
class Solution:
    def minDistinctFreqPair(self, nums):
        freqency = {}
        for num in nums:
            if num in freqency:
                freqency[num] = freqency[num] + 1
            else:
                freqency[num] = 1
        values = []
        for key in freqency:
            values.append(key)
        n = len(values)
        for i in range(n):
            for j in range(0, n - i - 1):
                if values[j] > values[j + 1]:
                    temp = values[j]
                    values[j] = values[j + 1]
                    values[j + 1] = temp
        for i in range(len(values)):
            x = values[i]
            freqency_x = freqency[x]
            for j in range(i + 1, len(values)):
                y = values[j]
                freqency_y = freqency[y]
                if freqency_x != freqency_y:
                    return [x, y]
        return [-1, -1]