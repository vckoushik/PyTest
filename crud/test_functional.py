'''
FUNCTIONAL TESTING - Movies Filter

'''
import requests
import pytest
ENDPOINT= "http://127.0.0.1:8000/"
token =''
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

def test_filter_movie_by_name():
    global token
    url = ENDPOINT+f"api/v1/movies/"
    headers =  {'Authorization': f'Bearer {token}'}
    params = {'title': 'Antman'}
    response = requests.get(url, headers=headers,params=params)
    assert response.status_code ==200
    print('test_filter_movie_by_name')
    print(response.json())

def test_filter_movie_by_year():
    global token
    url = ENDPOINT+f"api/v1/movies/"
    headers =  {'Authorization': f'Bearer {token}'}
    params = {'year__gt':2009,'year__lt':2022}
    response = requests.get(url, headers=headers,params=params)
    assert response.status_code ==200
    print('test_filter_movie_by_year')
    print(response.json())

def test_filter_movie_by_genre():
    global token
    url = ENDPOINT+f"api/v1/movies/"
    headers =  {'Authorization': f'Bearer {token}'}
    params = {'genre':'SuperHero'}
    response = requests.get(url, headers=headers,params=params)
    assert response.status_code ==200
    print('test_filter_movie_by_genre')
    print(response.json())

def test_filter_movie_by_creator_name():
    global token
    url = ENDPOINT+f"api/v1/movies/"
    headers =  {'Authorization': f'Bearer {token}'}
    params = {'creator__username':'test2'}
    response = requests.get(url, headers=headers,params=params)
    assert response.status_code ==200
    print('test_filter_movie_by_creator_name')
    print(response.json())


def test_filter_movie_multiple_params():
    global token
    url = ENDPOINT+f"api/v1/movies/"
    headers =  {'Authorization': f'Bearer {token}'}
    #params = {'title': 'Antman','year__gt':2009,'year__lt':2022,'genre':'SuperHero','creator__username':'test1'}
    params = {'title': 'Antman','year__gt':2009,'year__lt':2022,'genre':'Action'}
    
    response = requests.get(url, headers=headers,params=params)
    assert response.status_code ==200
    print('test_filter_movie_by_multiple_params')
    print(response.json())