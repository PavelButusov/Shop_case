import pytest

#from django.shortcuts import get_object_or_404
#from django.contrib.auth.models import User

from django.test import TestCase
from django.contrib.auth.models import User
from root_app.models import Product, BasketedProduct


def create_test_user():
    u1 = User.objects.create_user(username='vasya',
                                  password='12345678',
                                  email='Test@gmail.com')
    return u1


class TwoProductsTestCase(TestCase):
    def setUp(self):
        Product.objects.create(title='title_1')
        Product.objects.create(title='title_2')

    @pytest.mark.django_db
    def test_card_valid(self):
        response = self.client.get('/card/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/card/2/')
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db
    def test_card_invalid(self):
        response = self.client.get('/card/3/')
        self.assertEqual(response.status_code, 404)

    @pytest.mark.django_db
    def test_to_basket_valid(self):
        u1 = create_test_user()
        self.client.force_login(u1)
        response = self.client.get('/to_basket/1/')
        self.assertEqual(response.status_code, 302) # redirect

    @pytest.mark.django_db
    def test_to_basket_invalid(self):
        u1 = create_test_user()
        self.client.force_login(u1)
        response = self.client.get('/to_basket/3/')
        self.assertEqual(response.status_code, 404)

    @pytest.mark.django_db
    def test_cleanup_basket(self):
        u1 = create_test_user()
        self.client.force_login(u1)
        response = self.client.get('/cleanup_basket/')
        self.assertEqual(response.status_code, 302) # redirect





@pytest.mark.django_db
def test_index(client):
    response = client.get('/')
    assert response.status_code == 302 # redirect
    #u1 = create_test_user()


@pytest.mark.django_db
def test_admin(client):
    response = client.get('/admin/')
    status = response.status_code
    assert (response.status_code == 302) or (reasponse.status_code == 200)
    

#@pytest.mark.django_db
#def test_login(client):
#    pass
    

#@pytest.mark.django_db
#def test_login(client):
#    pass
    

@pytest.mark.django_db
def test_catalogue(client):
    response = client.get('/catalogue/')
    assert response.status_code == 200 # ready
    

@pytest.mark.django_db
def test_basket(client):
    response = client.get('/basket/')
    assert response.status_code == 200 # ready


