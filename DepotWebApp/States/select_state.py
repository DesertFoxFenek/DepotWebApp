import reflex as rx
from typing import List
from DepotWebApp.States.login_state import LoginState

class SelectState(rx.State):
    option: str = 'Wybierz pozycje'
    options: List[str] = ["Zajezdnia Borek", "Zajezdnia Olbin", "Zajezdnia Gaj", "Zajezdnia Obornicka"]

    def go_to_mng(self):
        
        LoginState.convert_depots(str(SelectState.option))
        
        return rx.redirect("/managment-site")