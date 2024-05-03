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
    
    response1 = session.post("http://localhost:3000/park", data={
        'plate': 'ABC123',
        'time': '1',
        'local_id': '6633abe018d68c005e9690d8'
    })

    return response1,session


def post_parking(a, plate,time,local_id):
    response = a.post("http://localhost:3000/park", data={
        'plate': plate,
        'time': time,
        'local_id': local_id
    })
    soup = BeautifulSoup(response.content, "html.parser")

    return soup
 
#response = post_parking(session, 'ABC123')
a,session = get_request()
b = session.post("http://localhost:3000/park", data={
    'plate': 'ABC123',
    'time': '1',
    'local_id': '6633abe018d68c005e9690d8'
})

print(b.content)
#soup = BeautifulSoup(a.content, "html.parser")
#print(soup)
