import flet as ft

from clock.functions import Clock
from clock.dropdown import Dropdown
from clock.buttons import Button

def main(page: ft.Page):
    page.title = "Alarm Clock"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_submit_click():
        selected_hour = hour_dropdown.value
        selected_minute = minute_dropdown.value
        if selected_hour and selected_minute:
            alarm_time = f"{selected_hour}:{selected_minute}:00"
            clock.set_alarm(alarm_time)
            status_text.value = f"Your alarm is set to {alarm_time}"
        else:
            status_text.value = "Please select both hour and minute"
        page.update()

    submit_button = Button("Submit", on_click=on_submit_click)

    clock = Clock()
    hour_dropdown = Dropdown(clock.get_every_hour())
    minute_dropdown = Dropdown(clock.get_every_minute())
    status_text = ft.Text()

    page.add(
        ft.Column(
            [
                ft.Text(
                    clock.get_current_time(),
                    theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Please select your alarm time below:",
                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                ),
                ft.Row([hour_dropdown, minute_dropdown], alignment=ft.MainAxisAlignment.CENTER),
                submit_button,
                status_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.run(main)