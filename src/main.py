import flet as ft
import asyncio
from datetime import datetime

from clock.functions import Clock
from clock.dropdown import Dropdown
from clock.buttons import Button


def main(page: ft.Page):
    page.title = "Alarm Clock"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    clock = Clock()
    hour_dropdown = Dropdown(clock.get_every_hour())
    minute_dropdown = Dropdown(clock.get_every_minute())
    status_text = ft.Text()

    running = {"value": True}

    current_time_text = ft.Text(
        datetime.now().strftime("%H:%M:%S"),
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
    )

    def on_submit_click(_):
        selected_hour = hour_dropdown.value
        selected_minute = minute_dropdown.value
        if selected_hour and selected_minute:
            alarm_time = f"{selected_hour}:{selected_minute}:00"
            clock.set_alarm(alarm_time)
            status_text.value = f"Your alarm is set to {alarm_time}"
        else:
            status_text.value = "Please select both hour and minute"
        page.update()

    def on_disconnect(_):
        running["value"] = False

    page.on_disconnect = on_disconnect

    submit_button = Button("Submit", on_click=on_submit_click)

    page.add(
        ft.Column(
            [current_time_text],
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

    async def update_time_loop():
        while running["value"]:
            await asyncio.sleep(1)
            current_time_text.value = datetime.now().strftime("%H:%M:%S")
            page.update()

    page.run_task(update_time_loop)


ft.run(main)