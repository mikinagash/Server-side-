import requests


class TestLogin:
        url = "https://trip-yoetz.herokuapp.com/auth/login"

        def test_login_with_invalid_details(self):
                 body = {'email': "mik@fsg", 'password': "177777723"}
                 x = requests.post(self.url ,data= body)
                 assert x.status_code == 400
                 print (x.status_code)

        def test_login_inorrect_email(self):
                body = {'email': "mik", 'password': "17777772"}
                x = requests.post(self.url, data=body)
                assert x.status_code == 400
                print(x.status_code)


        def test_login_with_empty_password(self):
                body = {'email': "mik", 'password': ""}
                x = requests.post(self.url, data=body)
                assert x.status_code == 400
                print(x.status_code)


        def test_login_correct(self):
            body = {"email":"miki@gmail.com","password":"12345"}
            x = requests.post(self.url,data= body)
            assert x.status_code == 200
            print(x.status_code)

        def test_login_with_empty_fields(self):
            body = {"email":"","password":""}
            x = requests.post(self.url,data=body)
            assert x.status_code == 400
            print(x.status_code)










