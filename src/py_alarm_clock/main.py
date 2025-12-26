import time
import datetime


def set_alarm(alarm_time: str):
    print(f"Setting alarm for {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")

        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("What time would you like to set for your alarm (HH:MM:SS)?")
    set_alarm(alarm_time)
