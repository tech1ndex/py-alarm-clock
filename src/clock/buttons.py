import flet as ft

class Button(ft.Button):
    def __init__(self, text, on_click=None):
        super().__init__(text)
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.BLACK
        if on_click:
            self.on_click = lambda e: on_click()

