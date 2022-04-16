import requests
import unittest
import json
from faker import Faker
from random import randint 


fake = Faker() 

user_name = fake.user_name()
password = fake.password()
user_id = randint(1, 500)
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
phone = fake.phone_number()
user_status = randint(1, 2)
user_name_updated = fake.user_name()
password_updated = fake.password()
email_updated = fake.email()
phone_updated = fake.phone_number()

headers = {'Content-Type': 'application/json'}

class PostmanTests(unittest.TestCase):

	def test_1_get_login(self):
		payload = json.dumps({'username': user_name, 'password': password})
		response = requests.get('https://petstore.swagger.io/v2/user/login', headers = headers, params = payload)
		self.assertEqual(response.status_code, 200)
		

	def test_2_post_create_user(self):
		payload = json.dumps({'id': user_id, 'username': user_name, 'firstName': first_name, 'lastName': last_name, 'email': email, 'password': password, 'phone': phone, 'userStatus': user_status})
		response = requests.post('https://petstore.swagger.io/v2/user', headers = headers, data = payload)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.text)['message'], str(user_id))
		

	def test_3_get_check_creating(self):
		response = requests.get('https://petstore.swagger.io/v2/user/'+ user_name)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.text)['id'], user_id)
		self.assertEqual(json.loads(response.text)['username'], user_name)
		self.assertEqual(json.loads(response.text)['firstName'], first_name)
		self.assertEqual(json.loads(response.text)['lastName'], last_name)
		self.assertEqual(json.loads(response.text)['email'], email)
		self.assertEqual(json.loads(response.text)['password'], password)
		self.assertEqual(json.loads(response.text)['phone'], phone)
		self.assertEqual(json.loads(response.text)['userStatus'], user_status)
		


	def test_4_put_update_user(self):
		payload = json.dumps({'id': user_id, 'username': user_name_updated, 'firstName': first_name, 'lastName': last_name, 'email': email_updated, 'password': password_updated, 'phone': phone_updated, 'userStatus': user_status})
		response = requests.put('https://petstore.swagger.io/v2/user/'+ user_name_updated, headers = headers, data = payload)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.text)['message'], str(user_id))
		

	def test_5_get_check_updating(self):
		response = requests.get('https://petstore.swagger.io/v2/user/'+ user_name_updated)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.text)['id'], user_id)
		self.assertEqual(json.loads(response.text)['username'], user_name_updated)
		self.assertEqual(json.loads(response.text)['firstName'], first_name)
		self.assertEqual(json.loads(response.text)['lastName'], last_name)
		self.assertEqual(json.loads(response.text)['email'], email_updated)
		self.assertEqual(json.loads(response.text)['password'], password_updated)
		self.assertEqual(json.loads(response.text)['phone'], phone_updated)
		self.assertEqual(json.loads(response.text)['userStatus'], user_status) 
			

	def test_6_delete_user(self):
		response= requests.delete('https://petstore.swagger.io/v2/user/'+ user_name_updated)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.text)['message'], user_name_updated)
		

	def test_7_get_check_after_deletion(self):
		response = requests.get('https://petstore.swagger.io/v2/user/'+ user_name_updated)
		self.assertEqual(response.status_code, 404)
		self.assertEqual(json.loads(response.text)['message'], 'User not found')
			

		
if __name__ == '__main__':
	unittest.main()