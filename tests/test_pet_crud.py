def test_create_and_validate_schema(client, new_pet):
    response = client.get(f'/pet/{new_pet['id']}')
    assert response.status_code == 200
    client.validate(response, 'pet_schema.json')