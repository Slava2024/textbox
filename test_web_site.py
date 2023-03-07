import unittest
from selenium import webdriver
from main import wait_of_element_located
from main import auth_user
from main import generate_random_string


class MyTestCase(unittest.TestCase):
	
	def test_text_box(self):
		driver = webdriver.Firefox()
		driver.get("https://demoqa.com/text-box/")
		
		user_name = generate_random_string(8)
		user_email = generate_random_string(5) + '@' + generate_random_string(5) + '.' + generate_random_string(2)
		current_address = generate_random_string(15)
		permanent_address = generate_random_string(45)
		
		auth_user(user_name, user_email, current_address, permanent_address, driver=driver)
		
		# Поиск и проверка
		self.assertEqual(user_name, wait_of_element_located(
			xpath='//*[@id=\"output\"]//*[@id=\"name\"]', driver=driver).text.split(":")[1])
		self.assertEqual(user_email, wait_of_element_located(
			xpath='//*[@id=\"output\"]//*[@id=\"email\"]', driver=driver).text.split(":")[1])
		self.assertEqual(current_address, wait_of_element_located(
			xpath='//*[@id=\"output\"]//*[@id=\"currentAddress\"]', driver=driver).text.split(":")[1])
		self.assertEqual(permanent_address, wait_of_element_located(
			xpath='//*[@id=\"output\"]//*[@id=\"permanentAddress\"]', driver=driver).text.split(":")[1])
	
		driver.close()


if __name__ == '__main__':
	unittest.main()
