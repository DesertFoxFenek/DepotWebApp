from DepotWebApp.Services.data_service import Data

class Tables:
    vehicles_assigned = []
    vehicles_unassigned = []

    def create_table(self):
        DataObj = Data()
        vehicles = DataObj.vehicles
        lines = DataObj.lines
        brigades = DataObj.brigades

        Tables.vehicles_assigned = []

        for brigade in brigades:
            brigade_id, brigade_number, line_number, vehicle_id, start_time = brigade
            vehicle_info = next((vehicle for vehicle in vehicles if vehicle.Id == vehicle_id), None)
            line_info = next((line for line in lines if line[0] == line_number), None)
            
            if vehicle_info and line_info:
                _, start_place, end_place, turn_around_time, *rest = line_info
                combined_row = {
                    'vehicle_id': vehicle_id,
                    'name': vehicle_info.Name,
                    'model': vehicle_info.Model,
                    'line_number': line_number,
                    'brigade_number': brigade_number,
                    'start_place': start_place,
                    'end_place': end_place,
                    'turn_around_time': turn_around_time,
                    'start_time': start_time,
                }
                Tables.vehicles_assigned.append(combined_row)

        assigned_vehicle_ids = [brigade[3] for brigade in brigades]
        Tables.vehicles_unassigned = [vehicle for vehicle in vehicles if vehicle.Id not in assigned_vehicle_ids]

        return Tables.vehicles_assigned
    