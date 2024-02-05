import reflex as rx
from rxconfig import config
from DepotWebApp.States.login_state import LoginState


@rx.page(route="/", title='DepotWebApp')
def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Witaj. Proszę zaloguj się i wybierz zajezdnie.", font_size="2em"),
            rx.input(
                placeholder='Login',
                on_blur=LoginState.set_login,
                width='50',
                height='10',
            ),
            rx.input(
                type_='password',
                placeholder='Hasło',
                on_blur=LoginState.set_password,
                width='50',
                height='10',
            ),
            rx.button(
                'Zaloguj',
                on_click=LoginState.get_auth,
            ),

            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )