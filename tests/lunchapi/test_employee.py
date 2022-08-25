import pytest
from rest_framework.test import APIClient

from restaurant import models

client = APIClient()

user_credentials = dict(email='test@gmail.com', password='TestTest10')


@pytest.mark.django_db
def test_register_employee():
    payload = user_credentials

    response = client.post('/api/v1/employee/', payload)

    data = response.data

    assert response.status_code == 201
    assert 'password' not in data


@pytest.mark.django_db
def test_jwt():
    payload = user_credentials

    client.post('/api/v1/employee/', payload)

    response = client.post('/api/v1/token/', payload)

    data = response.data
    assert data['access'] and data['refresh']
