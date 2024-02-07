import reflex as rx
from DepotWebApp.States.sidebar_state import SidebarState
from DepotWebApp.States.data_table_state import DataTableState
from DepotWebApp.States.about_dialog import AlertDialogState
from DepotWebApp.States.login_state import LoginState

def sidebar():
    return rx.box(
        rx.vstack(
            rx.image(src="/logo.ico", width="auto", height="auto", margin="0 auto"),

            rx.spacer(),

            rx.heading(
                SidebarState.depot_name,
                text_align="center",
                margin_bottom="1em",
            ),
            rx.spacer(),

            rx.text(SidebarState.depot_adress),
            rx.text(SidebarState.vehicles_num),
            rx.text(SidebarState.brigades_num),

            rx.spacer(),

            rx.button("O stronie",
                      on_click=AlertDialogState.change,
                      bottom='70px',
                      position='fixed'),

            rx.button('Wyloguj',
                      on_click=LoginState.log_out,
                      bottom='20px',
                      position='fixed'),

            rx.alert_dialog(
                rx.alert_dialog_overlay(
                    rx.alert_dialog_content(
                        rx.alert_dialog_header('O stronie'),
                        rx.alert_dialog_body('Strona stworzona przy wykorzystaniu biblioteki reflex połączoną z bazą danych w serwise Azure. Stan pojazdów/linii/brygad/czasów i innych wartości nie pokrywa się z realnymi. Dane z grudnia 2023 roku.'),
                        rx.alert_dialog_body('Projekt jest wariancją rozwojową konsolowej wersji utworzonej na potrzeby zajęć. ',
                                             rx.link(
                                                 'Wersja konsolowa',
                                                 href='https://github.com/DesertFoxFenek/DepotApp',
                                                 color="rgb(107,99,246)",
                                                 is_external=True,
                                             ),
                                             ),
                        rx.alert_dialog_body('Autor: ',
                                             rx.link(
                                                 'Desert_Fox_Fenek',
                                                 href='https://github.com/DesertFoxFenek',
                                                 color="rgb(107,99,246)",
                                                 is_external=True,
                                             ),),
                        rx.alert_dialog_body('Wersja: 0.2.24.02WE'), #wydanie.wersja.rok.miesiac.rodzaj WE=web/CA=konsola
                        rx.alert_dialog_footer(
                            rx.button('Zamknij',
                                      on_click=AlertDialogState.change),
                        ),
                    ),
                ),
                is_open=AlertDialogState.show
            ),

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
                    smooth_scroll_y = True,
                ),
            ),
            font_size="10px",
            position="fixed",
            right="25px",
            top="100px",
            left="350px",
        ),
        sidebar(),
    )