from itertools import combinations
import unittest
from app import found_pairs_by_number

class Test(unittest.TestCase):
    def test_simple_list(self):
        self.assertListEqual(found_pairs_by_number([1,9,5,0,20,-4,12,16,7], 12), [(0,12) , (5,7), (16,-4)])

    def test_file_tests(self):
        with open("tests.txt", "r") as f:
            lines = [line.rstrip().split(" ") for line in f.readlines()]
        test_list = []
        for line in lines:
            map_list = list(map(int,line[0].split(",")))
            test_list.append((map_list, int(line[-1])))
        for test in test_list:
            possible_pairs = combinations(test[0],2)
            pairs = [ pair for pair in set(possible_pairs) if abs(sum(pair)) == test[-1]]
            self.assertListEqual(
                found_pairs_by_number(test[0], test[-1]), 
                pairs,
                msg= f"{pairs}"
                )

if __name__ == '__main__':
    unittest.main()