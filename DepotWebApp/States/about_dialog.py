import reflex as rx

class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)