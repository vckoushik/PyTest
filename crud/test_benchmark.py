
import requests
import pytest
ENDPOINT= "http://127.0.0.1:8000/"
token =''

def test_can_call_endpoint(benchmark):
    result = benchmark(requests.get,ENDPOINT)
    assert result.status_code ==200

def test_get_user_token(benchmark):
    url  =  ENDPOINT+"api/v1/auth/token/"
    payload ={
        "username" : "test2",
        "password" : "Test123*"
    } 
    response = benchmark(requests.post,url,json=payload)
    #response = requests.post(url,json=payload)
    assert response.status_code ==200
    data = response.json()
    global token
    token = data['access']
    
def test_can_call_endpoint(benchmark):
    result = benchmark(requests.get,ENDPOINT)
    assert result.status_code ==200

def test_filter_movie_by_name(benchmark):
    global token
    url = ENDPOINT+f"api/v1/movies/"
    headers =  {'Authorization': f'Bearer {token}'}
    params = {'title': 'Antman'}
    result = benchmark(requests.get,url, headers=headers,params=params)
    assert result.status_code ==200

def test_get_movies(benchmark):
    url = ENDPOINT+"api/v1/movies/"
    global token
    headers = {'Authorization': f'Bearer {token}'}
   
    result = benchmark(requests.get,url, headers=headers)
    assert result.status_code ==200

