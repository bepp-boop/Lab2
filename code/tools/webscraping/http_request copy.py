import requests
from bs4 import BeautifulSoup

def request_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def post_request():
    
    response = requests.post("http://localhost:3000/signup", data={
    'username': 'ABC',
    'plate': 'ABC123',
    'password': '123',
    'password2': '123'
})
    soup = BeautifulSoup(response.content, "html.parser")
    
    return soup.find('div', class_='alert-danger')


def get_request():
    session = requests.Session()

    response = session.post("http://localhost:3000/login", data={
        'username': 'Test',    
        'password': '123',

    })

    return response

def post_parking(plate,time,local_id):
    response = a.post("http://localhost:3000/park", data={
        'plate': plate,
        'time': time,
        'location': local_id
    },cookies={{"connect.sid":"s:JxExmGLCfBduEsO33aiZelF9ZCQegmZk.g/0X9x6940ewa6jqXUFFXKedn7XZRIkeUnVXyqOIC8s"}
})
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find('div', class_='alert-danger')

print(post_request())
