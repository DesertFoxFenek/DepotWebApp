from DepotWebApp.States.login_state import LoginState
from DepotWebApp.Services.user_service import User
import reflex as rx

class Data:
    vehicles = []
    lines = []
    brigades = []

    def get_data(self):
        self.ThisDepot = Depot(LoginState.depot[0],LoginState.depot[1],LoginState.depot[2])
        self.ThisDepot.get_vehicles()

        self.ThisLines = OperativeLines(self.ThisDepot.DepotType)
        self.ThisLines.get_lines()

        self.ThisBrigades = ImportedBrigade(self.ThisDepot.DepotName)
        self.ThisBrigades.get_brigades()


class Depot:
    def __init__(self, DepotNumber, DepotName, DepotType):
        self.DepotNumber = DepotNumber
        self.DepotName = DepotName
        self.DepotType = DepotType
        self.VehicleList = []

    def get_vehicles(self):
        self.temp_data = LoginState.User.fetch_data_vehicle(self.DepotNumber)

        for row in self.temp_data:
            self.VehicleList.append(Vehicle(row[0],row[1],row[2]))

        Data.vehicles = self.VehicleList

class Vehicle:
    def __init__(self,Id, Name, Model):
        self.Id = Id
        self.Name = Name
        self.Model = Model

class OperativeLines:
    def __init__(self, depot_type):
        self.LineList = []
        self.depot_type = depot_type

    def get_lines(self):
        self.temp_data = LoginState.User.fetch_data_timetables()

        self.LineList = [row for row in self.temp_data if row[4] == self.depot_type]

        Data.lines = self.LineList

class Line:
    def __init__(self, number, start_place, finish_place, turn_around_time, type):
        self.number = number
        self.start_place = start_place
        self.finish_place = finish_place
        self.turn_around_time = turn_around_time
        self.type = type

class ImportedBrigade:
    def __init__(self, depot_name):
        self.BrigadeData = []
        self.depot_name - depot_name

    def get_brigades(self):
        self.temp_data = LoginState.User.fetch_brigade_table(self.depot_name)       

        for row in self.temp_data:
            self.BrigadeData.append(row)

        Data.brigades = self.BrigadeData