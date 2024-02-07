import reflex as rx
from DepotWebApp.States.select_state import SelectState

@rx.page(route="/depot-select-page", title='Depot Selection')
def depot_select_page() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading(SelectState.option),
            rx.center(
                rx.select(
                    SelectState.options,
                    on_change=SelectState.set_option,
                    width='50',
                    height='10',
                    margin='auto',
                ),
            ),
            rx.button(
                'Potwierdz',
                on_click=SelectState.go_to_mng(SelectState.option),
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",   
        ),
    )