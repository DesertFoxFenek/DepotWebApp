import reflex as rx

def sidebar():
    return rx.box(
        rx.vstack(
            rx.image(src="/favicon.ico", margin="0 auto"),
            rx.heading(
                "Sidebar",
                text_align="center",
                margin_bottom="1em",
            ),
            rx.spacer(),
            
            rx.text('Pole1'),
            rx.text('Pole2'),
            rx.text('Pole3'),
            rx.text('Pole4'),

            width="250px",
            padding_x="2em",
            padding_y="1em",
        ),
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="500",
    )

@rx.page(route="/managment-site", title='Managment Site')
def managment_site() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        sidebar()
    )