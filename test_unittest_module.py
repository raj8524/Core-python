import unittest
import unittest_module
import requests
from unittest.mock import patch


"""
#--------------algebric opeartion---------

class Test_unittest_module(unittest.TestCase):
    # def test_add(self):   #function should start with test (add from unitest_module)
    #     result=unittest_module.add(10,5)
    #     self.assertEqual(result,15)

    def test_add(self):  # function should start with test (add from unitest_module)

        self.assertEqual(unittest_module.add(10, 5), 15)
        self.assertEqual(unittest_module.add(-1,1),0)
        self.assertEqual(unittest_module.add(-1, -1),-2)

    def test_subtract(self):  # function should start with test (add from unitest_module)

        self.assertEqual(unittest_module.subtract(10, 5),5)
        self.assertEqual(unittest_module.subtract(-1,1),-2)
        self.assertEqual(unittest_module.subtract(-1, -1),0)

    def test_multiply(self):  # function should start with test (add from unitest_module)

        self.assertEqual(unittest_module.multiply(10, 5),50)
        self.assertEqual(unittest_module.multiply(-1,1),-1)
        self.assertEqual(unittest_module.multiply(-1, -1),1)

    def test_divide(self):  # function should start with test (add from unitest_module)

        self.assertEqual(unittest_module.divide(10, 5), 2)
        self.assertEqual(unittest_module.divide(-1,1),-1)
        self.assertEqual(unittest_module.divide(-1, -1),1)

        with self.assertRaises(ValueError):    #raising error
            unittest_module.divide(10,0)

#python3 -m unittest test_unittest_module.py                          run from cmd of file location
if __name__=='__main__':   #  this is required if u want to run from pycharm
    unittest.main()

#-----------employee-set--------
from unittest_module import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()


#-------------employee class.. to avoid repeated passing of elements

from unittest_module import Employee
class TestEmployee(unittest.TestCase):

    ###### setUpClass and tearDownClass ######

    @classmethod      #this can be used when there is db and u want to be connected,terminated after the tests.
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):  # this avoids writing multiple times passing same arguments in every testcase.this will be added begining of every test
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self): # this will be added at the end of every test
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')
    
    
if __name__ == '__main__':
    unittest.main()

"""

























