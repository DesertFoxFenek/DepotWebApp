import reflex as rx
from DepotWebApp.Services.data_service import Data

class SidebarState(rx.State):
    depot_name: str = ''
    depot_adress: str = ''
    vehicles_num: str = ''
    brigades_num: str = ''

    def change_state_val(self):
        self.depot_name = Data.depot_info_s[1]
        self.depot_adress = 'Adres: ' + str(Data.depot_info_s[3])
        self.vehicles_num = 'Pojazdy: ' + str(len(Data.vehicles))
        self.brigades_num = 'Brygady: ' + str(len(Data.brigades))