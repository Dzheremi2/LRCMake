import flet as ft

def update_slider(page, value):
    page.controls[1].controls[0].controls[1].controls[1].content.value = value / 1000
    print("Slider: Current Value:", page.controls[1].controls[0].controls[1].controls[1].content.value, "MaxValue:", page.controls[1].controls[0].controls[1].controls[1].content.max)
    page.update()

def slider_init(page, max):
    page.controls[1].controls[0].controls[1].controls[1].content.max = max
    page.controls[1].controls[0].controls[1].controls[1].content.value = 0.0
    page.update()