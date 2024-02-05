import reflex as rx


@rx.page(route="/managment-site", title='Managment Site')
def managment_site() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
    )