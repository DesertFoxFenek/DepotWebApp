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
        self.vehicle_timetable = TableGen.create_table()

        ManagerData.vehicle_timetable = self.vehicle_timetable

        return ManagerData.vehicle_timetable
    
    def redirect_table(self): return ManagerData.vehicle_timetable