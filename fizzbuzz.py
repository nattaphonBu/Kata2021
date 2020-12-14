import unittest


def fizz_buzz_calculater(number):
    if number == 0 or number < 0:
        return number
    elif number % 15 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

class FizzBuzzTest(unittest.TestCase):
    
    def test_input_1_should_return_1(self):
        actual = fizz_buzz_calculater(1)
        expected = 1
        
        self.assertEqual(actual, expected)
        
    def test_input_0_should_return_0(self):
        actual = fizz_buzz_calculater(0)
        expected = 0
        
        self.assertEqual(actual, expected)
        
    def test_input_2_should_return_2(self):
        actual = fizz_buzz_calculater(2)
        expected = 2
        
        self.assertEqual(actual, expected)
        
    def test_input_3_should_return_fizz(self):
        actual = fizz_buzz_calculater(3)
        expected = "fizz"
        
        self.assertEqual(actual, expected)
        
    def test_input_6_should_return_fizz(self):
        actual = fizz_buzz_calculater(6)
        expected = "fizz"
        
        self.assertEqual(actual, expected)
        
    def test_input_5_should_return_buzz(self):
        actual = fizz_buzz_calculater(5)
        expected = "buzz"
        
        self.assertEqual(actual, expected)
        
    def test_input_10_should_return_buzz(self):
        actual = fizz_buzz_calculater(10)
        expected = "buzz"
        
        self.assertEqual(actual, expected)
        
    def test_input_15_should_return_fizzbuzz(self):
        actual = fizz_buzz_calculater(15)
        expected = "fizzbuzz"
        
        self.assertEqual(actual, expected)
        
    def test_input_30_should_return_fizzbuzz(self):
        actual = fizz_buzz_calculater(30)
        expected = "fizzbuzz"
        
        self.assertEqual(actual, expected)
        
    def test_input_minus_1_shoule_return_minus_1(self):
        actual = fizz_buzz_calculater(-1)
        expected = -1
        
        self.assertEqual(actual, expected)
        
    def test_input_minus_3_should_return_minus_3(self):
        actual = fizz_buzz_calculater(-3)
        expected = -3
        
        self.assertEqual(actual, expected)
        

unittest.main()