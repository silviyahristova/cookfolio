#test if the register page loads correctly
def test_register_page_loads(client):
    response = client.get('/register')

    assert response.status_code == 200
    assert b'Register' in response.data