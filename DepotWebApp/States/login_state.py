import reflex as rx
from DepotWebApp.Services.user_service import User

class LoginState(rx.State):
    login: str
    password: str
    output: str
    depots: list

    def get_auth(self):
        ThisUser = User()
        self.output = ThisUser.login_user(self.login,self.password)
        if self.output == 1:
            LoginState.depots = ThisUser.depots
            
            return rx.redirect("/depot-select-page")
        else:
            return rx.window_alert("Błędna nazwa użytkownika lub hasło. W przypadku dłuzszego oczekiwania i wyskoczenia błędu kliknij zaloguj jeszcze raz. Najprędzej doszło do timeout'a połączenia z bazą.")

    def log_out(self):
        self.reset()
        return rx.redirect("/")