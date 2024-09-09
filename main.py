import flet as ft

# Main Music Variable
now_playing = None

#Main Function
def main(page: ft.Page):
    #App Theming
    page.theme = page.dark_theme = ft.Theme(use_material3=True, color_scheme_seed="green")
    page.fonts = {
        "Google Sans": "https://raw.githubusercontent.com/hprobotic/Google-Sans-Font/master/GoogleSans-Regular.ttf",
    }
    # Top AppBar 
    appbar = ft.AppBar(
        title=ft.Text("LRCMake"),
        bgcolor=ft.colors.ON_PRIMARY,
        title_text_style=ft.TextStyle(font_family="Google Sans", size=20, weight=ft.FontWeight.W_400),
        actions=[
            ft.IconButton(ft.icons.RESTART_ALT)
        ]
    )

# TODO: Logic based on string splitting
    def report_inside(args):
        print((lyricField.value).splitlines())

    # Plain lyric field
    lyricField = ft.TextField(
        label="Input Lyrics Text Here",
        border_color=ft.colors.SECONDARY,
        multiline=True,
        icon=ft.icons.TEXT_SNIPPET,
        value="",
        on_change=report_inside
    )

    # Convert lyrics to separated strings FAB
    proceedLyrcis = ft.FloatingActionButton(
        icon=ft.icons.CHECK_CIRCLE_OUTLINE_OUTLINED,
        text="Start Sync",
        enable_feedback=True
    )

    # Song Controls Interface
    currTrackItem = []
    currTrackItem.append(
        ft.Column(
            controls = [
                    # Info and play button
                    ft.ListTile(
                    leading=ft.Icon(ft.icons.AUDIOTRACK),
                    title=ft.Text(f"{'Select file' if now_playing == None else now_playing['artist']}", font_family="Google Sans", size=17),
                    subtitle=ft.Text(f"{'Click' if now_playing == None else now_playing['track']}"),
                    trailing=ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, bgcolor=ft.colors.PRIMARY_CONTAINER)
                ),
                # Duration controls
                ft.Row(
                    [
                        ft.Text(
                            f"{'00:00' if now_playing == None else now_playing['duration']}",
                            font_family="Google Sans",
                            size=17
                        ),
                        ft.Container(
                            content=ft.Slider(
                                max=100 if now_playing == None else now_playing['duration'] / 1000
                            ), expand=True
                        )
                    ]
                )
            ]
        )
    )
    now_playing_row = ft.Row(controls=currTrackItem, wrap=True)

    #Building interface
    page.add(appbar)
    page.add(now_playing_row)
    page.add(lyricField)
    page.add(proceedLyrcis)


ft.app(target=main, assets_dir="assets")
