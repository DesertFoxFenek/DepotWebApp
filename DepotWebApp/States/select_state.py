import reflex as rx
from typing import List
from DepotWebApp.States.login_state import LoginState
from DepotWebApp.Services.data_parser import DataParser
from DepotWebApp.States.manager_state import ManagerData
from DepotWebApp.States.data_table_state import DataTableState


class SelectState(rx.State):
    option: str = 'Wybierz pozycje'
    options: List[str] = ["Zajezdnia Borek", "Zajezdnia Olbin", "Zajezdnia Gaj", "Zajezdnia Obornicka"]
    depot: list
    vehicle_timetable: list
    #menu wyboru do przebudowy

    def go_to_mng(self,option):
        print(option)
        DP = DataParser()
        SelectState.depot = DP.get_depot(option,LoginState.depots)
        MD = ManagerData()
        MD.get_mng_data(SelectState.depot)
        DTU = DataTableState()
        DTU.get_data(MD.vehicle_timetable)

        return rx.redirect("/managment-site")