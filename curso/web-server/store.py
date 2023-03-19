import requests

#Es una buena practica tener un archivo de Python donde solamente se
# guarden las urls que se vayan a llamar y hacer import de las
# variables o constantes de ese archivo. Es más fácil tener todo en 1 solo lugar
api_url_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(api_url_categories)
    print(r.status_code)
    print('...')

    print(r.text)
    print('...')

    print(type(r.text))
    print('...')

    categories = r.json()
    for category in categories:
        print(category['name'])