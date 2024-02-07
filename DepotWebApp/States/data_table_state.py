import reflex as rx
import pandas as pd

#from typing import Any, List

class DataTableState(rx.State):

    # Define the columns for the data editor
    columns: list[str] = ["Numer","Nazwa","Model","Linia","Brygada","Przystanek Startowy","Przystanek Końcowy","Czas przejazdu", "Wyjazd"]

    # Assuming data is provided or fetched from somewhere
    data: list

    def get_data(self, data):
        self.df = pd.DataFrame(data)
        self.temp = self.df.values.tolist()

        DataTableState.data = self.temp
        self.data = self.temp

    def override_data(self):
        self.data = DataTableState.data