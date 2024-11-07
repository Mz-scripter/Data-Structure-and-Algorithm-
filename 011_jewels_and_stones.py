import unittest


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count


class TestJewelsAndStones(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_case(self):
        self.assertEqual(self.solution.numJewelsInStones('aA', 'aAAbbbb'), 3)
    
    def test_no_jewels(self):
        self.assertEqual(self.solution.numJewelsInStones('z', 'ZZ'), 0)
    
    def test_empty_string(self):
        self.assertEqual(self.solution.numJewelsInStones('', ''), 0)


if __name__ == '__main__':
    unittest.main()