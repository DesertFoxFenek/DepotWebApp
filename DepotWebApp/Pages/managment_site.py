import reflex as rx
from DepotWebApp.States.sidebar_state import SidebarState
from DepotWebApp.States.data_table_state import DataTableState

def sidebar():
    return rx.box(
        rx.vstack(
            rx.image(src="/favicon.ico", margin="0 auto"),
            rx.heading(
                SidebarState.depot_name,
                text_align="center",
                margin_bottom="1em",
            ),
            rx.spacer(),

            rx.text(SidebarState.depot_adress),
            rx.text(SidebarState.vehicles_num),
            rx.text(SidebarState.brigades_num),

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

@rx.page(route="/managment-site", title='Managment Site', on_load=[SidebarState.change_state_val, DataTableState.override_data])
def managment_site() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.box(
            rx.vstack(
                rx.spacer(),
                rx.data_table(
                    data=DataTableState.data,
                    columns=DataTableState.columns,
                    pagination=True,
                    search=True,
                    resizable=True,
                ),
            ),
            position="fixed",
            right="25px",
            top="100px",
            left="350px",
        ),
        sidebar(),
    )