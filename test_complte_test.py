import unittest
import complte_test
class test_complte_test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(complte_test.add(10,5),15)
if __name__=="__main__":
    unittest.main()