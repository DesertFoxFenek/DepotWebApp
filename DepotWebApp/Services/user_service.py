import pyodbc

class User:

    login = ''
    password =''
    depots = []

    def __init__(self):
        #parametry polaczenia csii ze localhost
        self.server = 'tcp:depot-app-db-server.database.windows.net,1433;'
        self.database = 'DepotAppDB'
        self.depots = []
        self.depot_num = None

    def login_user(self, g_login, g_password):
        self.login = g_login
        self.password = g_password

        try:
            self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.login};PWD={self.password};TrustServerCertificate=yes;Trusted_Connection=no'
            self.connection = pyodbc.connect(self.conn_str)
            self.cursor = self.connection.cursor()
            self.querry = f'SELECT * FROM WroclawDepots'
            self.cursor.execute(self.querry)
            self.data = self.cursor.fetchall()
            self.connection.close()

            for row in self.data: self.depots.append(row)

            User.depots = self.depots
            User.login = self.login
            User.password = self.password

            return 1

        except Exception as ex:
            print(ex)
            return 0
        
    def get_dep_number(self, number): self.depot_num = number

    def fetch_data_vehicle(self,SelectedDepotType):
        if SelectedDepotType == 1: SQLDepotType = 1
        elif SelectedDepotType == 2: SQLDepotType = 2
        elif SelectedDepotType == 3 : SQLDepotType = 3
        elif SelectedDepotType == 4 : SQLDepotType = 4
        else: return None

        self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.login};PWD={self.password};TrustServerCertificate=yes;Trusted_Connection=no'
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        self.querry = f'SELECT * FROM VehiclesTable WHERE Depot = {SQLDepotType}'
        #self.querry = f'SELECT * FROM master.dbo.VehiclesTable'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data
    
    def fetch_data_timetables(self):
        self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.login};PWD={self.password};TrustServerCertificate=yes;Trusted_Connection=no'
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        #self.querry = f'SELECT * FROM TimetableDB WHERE Type LIKE {depot_type}'
        self.querry = f'SELECT * FROM TimetableDB'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data
    
    def fetch_brigade_table(self, depot):
        self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.login};PWD={self.password};TrustServerCertificate=yes;Trusted_Connection=no'
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        self.depot_table = depot+'DepotBrigadeTable'
        self.querry = f'SELECT * FROM {self.depot_table}'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data