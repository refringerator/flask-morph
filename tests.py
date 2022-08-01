import pytest
from hello import create_app

@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_rp(client):
   rv = client.get("/тест")
   assert "теста" == rv.data.decode('utf-8')


def test_dp(client):
   rv = client.get("/2/тест")
   assert "тестом" == rv.data.decode('utf-8')


def test_dp_plur(client):
   rv = client.get("/2/тест?plur")
   assert "тестами" == rv.data.decode('utf-8')

