from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import RegisterAPI, LoginAPI, UserApi,UserRandomApi


class TestRegister(SimpleTestCase):

    def test_register_post(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterAPI)


class TestUser(SimpleTestCase):
    def test_user(self,id=None):
        if id:
          url = reverse('getid',id=id)
          self.assertEquals(resolve(url).func.view_class, UserApi)
    
        url = reverse('getall')
        self.assertEquals(resolve(url).func.view_class, UserApi)

class TestUseRandom(SimpleTestCase):
     def test_user_random(self):
      
        url = reverse('get_random')
        self.assertEquals(resolve(url).func.view_class, UserRandomApi)

class TestLoginAPI(SimpleTestCase):
     def test_user_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginAPI)