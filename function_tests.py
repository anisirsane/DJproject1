from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):                      #1
	def setUp(self):                                          #3
		self.browser=webdriver.Firefox()
	def tearDown(self):                                       #3
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):    #2
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do',self.browser.title)             #4
		self.fail('finish the test!')                         #5


if __name__== '__main__':                                     #6
	unittest.main()                          #7

#1######tests are organized into classes which inherit from 
           ######### unittest.testcase
#2######any method that its name starts with test 
           ########is concidered a test method, 
           ########and will be run by the test runner
#3######setUp and tearDown are special methods which get run 
           ####### before and after each test and they are 
           ####### used to start and close the browser
#4###### assertIn  instead of assert to make our assertions 
           ####### in unittest
#5######self.fail just fails no matter what , here were using it 
           ###### to produce the error msg given , set as a 
           ###### reminder to finish the test
#6###### this is how python checks if the script is 
           ###### run by the command line or by another script
