import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #Crear una instancia de la app

@app.get('/')   #Agregar un decorador / Ruta
def get_list():
    return [1,2,3,20,50]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola, soy una página</h1>
    <p>soy un párrafo</p>
    """

def run():
    store.get_categories()

if __name__=='__main__':
    run()