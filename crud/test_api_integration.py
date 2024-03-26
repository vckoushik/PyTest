'''
INTEGRATION TESTING USER AND MOVIES API's

'''
import requests
import pytest
import json

ENDPOINT= "http://127.0.0.1:8000/"
token =''
movieId =0
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

#check if api is not accessable if not authenticated
def test_movies_unauth():
    url = ENDPOINT+"api/v1/movies/"
    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        response = requests.get(url)
        response.raise_for_status()
    assert exc_info.value.response.status_code == 401

def test_user_register():
    url = ENDPOINT+"api/v1/auth/register/"
    payload={
        "username" : "test15",
        "password2" : "Test123*",
        "password" : "Test123*",
        "first_name": "test",
        "last_name": "15",
        "email":"test15@email.com"
    }

    response = requests.post(url,json=payload)
    assert response.status_code ==201
    data = response.json()
    print('User created')
    print(data)

def test_get_user_token():
    url  =  ENDPOINT+"api/v1/auth/token/"
    payload ={
        "username" : "test2",
        "password" : "Test123*"
    } 
    response = requests.post(url,json=payload)
    assert response.status_code ==200
    data = response.json()
    global token
    token = data['access']
    print(token)

 
def test_get_movies():
    url = ENDPOINT+"api/v1/movies/"
    global token
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    assert response.status_code ==200 
    data = response.json()
    print("List of movies")
    print(data['results'])

def test_create_movies():
    url = ENDPOINT+"api/v1/movies/"
    global token
    headers = {'Authorization': f'Bearer {token}'}
    payload={  
        "title":  "She Hulk Test1", 
        "genre":  "SuperHero", 
        "year":  2023, 
        "creator":  "admin"     
     }
    response = requests.post(url, headers=headers,json=payload)
    assert response.status_code ==201 
    
    data = response.json()
    print(data['id'])
    global movieId
    movieId = data['id']   
    print("Movie Created Successfully")
    print(movieId)
    
def test_update_movies():
    global movieId
    url = ENDPOINT+f"api/v1/movies/{movieId}/"
    global token
    headers = {'Authorization': f'Bearer {token}'}
    payload={  
        "title":  "Test", 
        "genre":  "Thirller", 
        "year":  2012, 
        "creator":  "admin"     
     }
    
    response = requests.put(url, headers=headers,json=payload)
    assert response.status_code ==200 
    data = response.json()
    print("Updated Movie")
    print(data)

def test_delete_movies():
    global movieId
    url = ENDPOINT+f"api/v1/movies/{movieId}/"
    global token
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(url, headers=headers)
    assert response.status_code ==204
    print(f"Movie Deleted : {movieId}")
    











