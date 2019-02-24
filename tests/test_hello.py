import pytest
import context

from app.hello import app

def test_empty():
    with app.test_client() as c:
        response = c.get('/')
        assert response.data == b'<b>Hello!</b>'
        assert response.status_code == 200
