import reflex as rx
from reflex_calendar import calendar

def index():
    return rx.box(
        rx.hstack(
            rx.image(src="/logo_uabc.png", width="6%", margin_left="10px"),
            rx.box(
            rx.text("UNIVERSIDAD AUTONOMA DE BAJA CALIFORNIA", size="6", style={"color":"white", "font-weight":"bold"}),
            margin_top="30px",
            #bg="red"
            ),
            bg="#00723f"
        ), calendar(
            go_to_range_start_on_select=True,
            locale='en-US',
            min_date='2022-01-01',
            max_date='2023-12-31'
        )
    )
