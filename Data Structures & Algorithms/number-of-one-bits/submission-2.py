class Solution:
    def hammingWeight(self, n: int) -> int:
        bin = format(n, 'b')
        return bin.count('1')
