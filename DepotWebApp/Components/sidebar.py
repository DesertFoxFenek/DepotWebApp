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
            rx.menu(...),
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