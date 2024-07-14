"""
Importar la libreria y funciones relacionadas con el frontend de cada pagina,
Este archivo es el main de todo el sistema.
"""
import reflex as rx
from Prototipo_Posgrado.inicio_sesion import frontend
from Prototipo_Posgrado.inicio_sesion import backend

app = rx.App()
app.add_page(frontend.index)




