from DepotWebApp.Services.user_service import User

class Data:
    vehicles: list
    lines: list
    brigades: list
    depot_info_s: str

    def get_data(self,depot_info):
        print(depot_info[0])
        Data.depot_info_s = depot_info
        
        self.ThisDepot = Depot(depot_info[0],depot_info[1],depot_info[2])
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
        self.UserDummy = User()

    def get_vehicles(self):
        self.temp_data = self.UserDummy.fetch_data_vehicle(self.DepotNumber)

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
        self.UserDummy = User()

    def get_lines(self):
        self.temp_data = self.UserDummy.fetch_data_timetables()
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
        self.depot_name = depot_name
        self.UserDummy = User()

    def get_brigades(self):
        self.temp_data = self.UserDummy.fetch_brigade_table(self.depot_name)       

        for row in self.temp_data:
            self.BrigadeData.append(row)

        Data.brigades = self.BrigadeData