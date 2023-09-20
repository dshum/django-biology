import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    url = reverse('articles:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_404(client):
    url = reverse('articles:404')
    response = client.get(url)
    assert response.status_code == 404
