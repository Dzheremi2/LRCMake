import flet as ft
from ...variables import variables

class dataBlock(ft.Row):
    def __init__(self, file_picker):
        super().__init__()

        self.controls = [
            ft.ListTile(
                leading = ft.Image(
                    src="note.png",
                    border_radius=ft.border_radius.all(6),
                    width=50,
                    height=50
                ),
                title=ft.Text(f"{'Select track' if variables.metadata == {} else variables.metadata['track']}"),
                subtitle=ft.Text(f"{'Click to select file' if variables.metadata == {} else variables.metadata['artist']}"),
                trailing=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Text(f"{'00:00' if variables.metadata == {} else variables.metadata['duration']}", font_family="Google Sans", size=20),
                        ft.Text(f"{'000' if variables.metadata == {} else variables.metadata['duration_s']}", font_family="Google Sans", size=12)
                    ],
                    spacing=1
                ),
                on_click=lambda _: file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.AUDIO)
            )
        ]
        self.wrap = True