import reflex as rx

class InputStateLogin(rx.State):
    text_login: str = 'Login'
    text_password: str = 'Hasło'

    def clear_text(self):
        self.text_login = ''
        self.text_password = ''