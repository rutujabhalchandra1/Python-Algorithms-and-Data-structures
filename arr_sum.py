import unittest
def find_pairs(arr, sum):
    for i in range(0,len(arr)-1):
        if (sum - arr[i]) in arr:
            return (arr[i], sum - arr[i])
        else:
            print('No pairs found')



class Test(unittest.TestCase):
    def test_1(self):
        arr = [1,2,3,4]
        sum = 7
        ans = find_pairs(arr,sum)
        expected = (3,4)
        self.assertEqual(expected, ans)



unittest.main()