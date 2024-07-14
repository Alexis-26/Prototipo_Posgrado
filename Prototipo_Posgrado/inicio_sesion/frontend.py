import reflex as rx
from Prototipo_Posgrado.inicio_sesion import backend
from Prototipo_Posgrado.inicio_sesion import style
"""flotante se creó inicialmente para lograr que el texto se situara alrededor de las imágenes y no necesariamente debajo de ellas."""
""" establecer la distancia entre líneas de texto.  """

def index():
    return rx.box(
        rx.hstack(
            rx.container(
                rx.box(
                    rx.image(src="/logo_uabc.png",style=style.style1 ),
                    rx.text("UNIVERSIDAD AUTÓNOMA DE BAJA CALIFORNIA", style=style.style2),
                    margin_top="50px"
                    ),
                    style=style.style2
                    )
                    ),
    
        rx.box(
            rx.container(
                rx.box(
                    rx.text("INICIAR SESIÓN", align="center",style=style.style3),
                    rx.box(
                        rx.text("Correo Electronico", margin_top="5%",style=style.style4),
                        margin_left="20%"

                    ),
                    rx.box(
                        rx.center(rx.input(style=style.style_input))
                    ),
                    rx.spacer(),
                    rx.box(
                        rx.text("Contraseña", margin_top="5%",style=style.style4),
                        margin_left="20%"
                    ),
                    rx.box(
                        rx.center(rx.input(size="2", width="60%"))
                    ),
                    rx.box(
                        rx.center(
                            rx.button("Iniciar sesión", style=style.style5),
                            margin_top="5%")
                    ),
                    width="100%",
                    margin_left="-60%"
                ),
            size="2",
            margin_top="5%",
            )
        ),
    )