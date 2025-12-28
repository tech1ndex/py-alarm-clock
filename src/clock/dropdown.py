import flet as ft


class Dropdown(ft.DropdownM2):
    def __init__(self, options, width=100):
        dropdown_options = [ft.dropdownm2.Option(option) for option in options]
        super().__init__(width=width, options=dropdown_options)

