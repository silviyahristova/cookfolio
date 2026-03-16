#first test to check if the home page loads successfully
def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200