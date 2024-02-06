import reflex as rx
from DepotWebApp.Services.data_service import Data
from DepotWebApp.Services.table_creator import Tables

class ManagerData(rx.State):
    vehicle_timetable: list
    free_vehicles: list

    def get_mng_data(self,depot_info):
        ThisDepot = Data()
        ThisDepot.get_data(depot_info)

        TableGen = Tables()
        ManagerData.vehicle_timetable, ManagerData.free_vehicles = TableGen.create_table()

        print(ManagerData.vehicle_timetable, ManagerData.free_vehicles)