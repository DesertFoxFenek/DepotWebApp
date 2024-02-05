import reflex as rx
from typing import List
from DepotWebApp.States.login_state import LoginState
from DepotWebApp.Services.data_parser import DataParser
from DepotWebApp.States.manager_state import ManagerData

class SelectState(rx.State):
    option: str = 'Wybierz pozycje'
    options: List[str] = ["Zajezdnia Borek", "Zajezdnia Olbin", "Zajezdnia Gaj", "Zajezdnia Obornicka"]
    depot: list
    #menu wyboru do przebudowy
    def go_to_mng(self):

        DP = DataParser()
        SelectState.depot = DP.get_depot("Zajezdnia Gaj",LoginState.depots) #nie dostaje state'a
        MD = ManagerData()
        MD.get_mng_data(SelectState.depot)

        return rx.redirect("/managment-site")