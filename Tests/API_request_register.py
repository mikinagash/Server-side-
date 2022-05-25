import requests
import random
class TestRegister:
    url = "https://trip-yoetz.herokuapp.com/auth/register"

    def test_register_correct(self):
        body = {"birthDate": "2000-11-11",
                "email": f"mikinagash@gmail.com{random.randint(1,100)}",
                "image": "111",
                "lastName": "nagash",
                "name": "miki",
                "password": "12345",
                 "confirm password":"12345"}
        x = requests.post(self.url,data=body)
        print(x.status_code)
        print(body.values())
        assert x.status_code == 200


    def test_register_with_exist_email (self):
        body = {"email": "miki@gmail.com", "password": "12345", "birthDate": "2000-11-11", "name": "miki", "lastName": "nagash"}
        x = requests.post(self.url, data=body)
        assert x.status_code == 400
        print(x.status_code)





