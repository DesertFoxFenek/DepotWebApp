import reflex as rx
from DepotWebApp.Services.data_service import Data

class ManagerData(rx.State):
    vehicle_timetable: list
    free_vehicles: list

    #_backend: ThisDepot = Data()

    def get_mng_data(self,depot_info):
        ThisDepot = Data()
        ThisDepot.get_data(depot_info)
        print(ThisDepot.vehicles)
        print(ThisDepot.lines)
        print(ThisDepot.brigades)