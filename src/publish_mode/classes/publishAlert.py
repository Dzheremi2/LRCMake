import flet as ft

class publishAlert(ft.AlertDialog):
    def __init__(self, page, exit_status, exit_message):
        super().__init__()

        self.modal = True
        self.title = ft.Text(f"{exit_status}")
        self.content = ft.Text(f"{exit_message}")
        self.actions = [ft.TextButton("Ok", on_click=lambda _: page.close(self))]
        self.actions_alignment = ft.MainAxisAlignment.END
        