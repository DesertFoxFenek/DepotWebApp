
class DataParser:

    def __init__(self): None

    def get_depot(self, depot, depot_list):

        for i in range(len(depot_list)):
            self.temp = depot_list[i]
            if self.temp[1]== depot:

                return self.temp