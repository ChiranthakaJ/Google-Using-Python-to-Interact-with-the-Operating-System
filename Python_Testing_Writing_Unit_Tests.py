#We've now looked at the principles behind automatic testing. We know that by having automatic tests, we can run them as many times as necessary to make sure that our code does what we want it to do. So how we do this in Python? We need to write some code that runs a test and verifies the output. This way, we can get our computer to do the work for us. To demonstrate the testing workflow, we'll create unit tests for the rearrange_name function from the previous video.

#As we touched on earlier, automatic tests are usually written alongside the code that we want to test. What this means in practice is creating a separate Python file with the test. The convention is to call the script with the same name of the module that it's testing and appending the suffix _test. So for our rearrange module, we'll create the rearrange_test.py file.

#We'll test the rearrange_name function of the rearrange module. So let's import that function the way we did before in the interpreter.

#Okay, we're ready to start writing the tests. To help us with that, Python provides a module called unittest. Thanks Python. This module includes a number of classes and methods that let us easily create unit tests for our code. The first thing we'll do is import the unit test module we'll need for testing.

#The unit test module provides a test case class with a bunch of testing methods ready to use. To access this functionality, we create our own class by inherits from test case, thus inheriting all those testing methods. So we're going to write our own test rearrange class that inherits from test case. Do you remember what the syntax for that was? We need to include the class that we want to inherit from in the parentheses.

#We called our test class, TestRearrange, and indicated that it should inherit functionality from the TestCase class located in the unit test module. Any methods we define in our TestRearrange class that start with the prefix test will automatically become tests that can be run by the testing framework. So we're ready to write our first test case. What's it going to be? In our last video, we manually tested one simple case. Let's turn that manual test into an automatic test that verifies that basic names are formatted correctly.

#With this method which we've called test_basic, we kick off by setting up our expected inputs and outputs. We then use the assertEqual method provided to us by the test case class we inherited from to verify that what we expected is exactly what we got. The assertEqual method basically says both of my arguments are equal. If that statement's true, then the test passes. If it's false, the test fails and an error is printed to the screen when the test is run. Okay, we've got our first unit test. So how can we run it? In the main part of our program, we'll call the unittest.main() function, which will run the test for us.

#All right, we're ready to run the test. We'll do that by executing the file that we just created. Let's make our script executable and then run it.

#The complete solution is as the below.

#!/usr/bin/env python3

# Writing Unit Tests in Python
# from keyword imports a function from a script in the python3 interpreter
# the function can be called without having to write the module name each time we want to call it

from rearrange import rearrange_name
# unittest module includes classes and methods for creating unit tests
import unittest

# Include the class that we want to inherit from in the parentheses
# TestRearrange class inherits from TestCase
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    
    # test for an edge case 
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

# Runs the test
unittest.main()

#Looks good. The output is pretty descriptive, printing out some information about how long a group of tests or test suite took to run. As well as the number of tests, and whether or not, they passed. Just like that, we've tested our first function. It's pretty cool, right? I know there was a lot going on here. If the code is confusing, complex, or didn't really sink in yet, that's okay. Take the time to practice on your own and review the content until it feels natural. Coming up, we'll test even more cases.