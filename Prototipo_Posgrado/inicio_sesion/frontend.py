import reflex as rx

def index():
    return rx.box(
        rx.hstack(
            rx.image(src="/logo_uabc.png", width="6%", margin_left="10px"),
            rx.box(
            rx.text("UNIVERSIDAD AUTONOMA DE BAJA CALIFORNIA", size="6", style={"color":"white", "font-weight":"bold"}),
            margin_top="50px",
            #bg="red"
            ),
            bg="#00723f"
        ),
        rx.box(
            rx.container(
                rx.box(
                    rx.text("INICIA SESION", size="4", align="center"),
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
                ),
            size="2",
            margin_top="5%"
            )
        ),
    )