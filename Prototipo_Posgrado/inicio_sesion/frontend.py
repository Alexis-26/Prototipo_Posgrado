import reflex as rx
"""flotante se creó inicialmente para lograr que el texto se situara alrededor de las imágenes y no necesariamente debajo de ellas."""
""" establecer la distancia entre líneas de texto.  """
def index():
    return rx.box(
        rx.hstack(
            rx.container(
                rx.box(
                    rx.image(src="/logo_uabc.png", width="10%",margin_right="10px",style={"float":"left"}),
                    rx.text("UNIVERSIDAD AUTÓNOMA DE BAJA CALIFORNIA", size="6", style={"color":"white", "font-weight":"bold" ,"line_height": "100px"}),
                    margin_top="50px"
                    ),
                    bg="#00723f"
                    )
                    ),
    
        rx.box(
            rx.container(
                rx.box(
                    rx.text("INICIAR SESIÓN", size="4", align="center"),
                    rx.box(
                        rx.text("Correo Electronico", margin_top="5%"),
                        margin_left="20%"
                    ),
                    rx.box(
                        rx.center(rx.input(size="2", width="60%"))
                    ),
                    rx.spacer(),
                    rx.box(
                        rx.text("Contraseña", margin_top="5%"),
                        margin_left="20%"
                    ),
                    rx.box(
                        rx.center(rx.input(size="2", width="60%"))
                    ),
                    rx.box(
                        rx.center(
                            rx.button("Iniciar Sesion", bg="#00723f"),
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