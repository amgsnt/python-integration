import pytest
import context

from chat.hello import app

def test_empty():
    with app.test_client() as c:
        response = c.get('/')
        assert response.data == b'<b>Bia linda da minha vida!</b>'
        assert response.status_code == 200
