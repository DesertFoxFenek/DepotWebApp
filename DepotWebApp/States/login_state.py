import reflex as rx
from DepotWebApp.Services.user_service import User
from typing import List

class LoginState(rx.State):
    login: str
    password: str
    output: int
    depot = []
    depots = []
    def get_auth(self):
        ThisUser = User()
        self.output = ThisUser.login_user(self.login,self.password)
        if self.output == 1:
            LoginState.depots = ThisUser.depots
            print(LoginState.depots)
            return rx.redirect("/depot-select-page")
        else:
            return rx.window_alert("Błędna nazwa użytkownika lub hasło")
            
    def convert_depots(self,depot): #do ogarniecia
        for i in range(len(LoginState.depots)):
            self.temp = LoginState.depots[i]
            if self.temp[1]== depot:
                LoginState.set_depot = self.temp
                print(LoginState.depot)