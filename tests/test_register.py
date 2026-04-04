#test if the register page loads correctly
def test_register_page_loads(client):
    response = client.get('/register')

    assert response.status_code == 200
    assert b'Register' in response.data

#test for empty fields
def test_register_empty_fields(client):
    response = client.post('/register', data={
        'username': '',
        'email': '',
        'password': '',
        'confirm_password': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'All fields are required.' in response.data