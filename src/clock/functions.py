import datetime

class Clock:
    def __init__(self):
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
        self._alarm_time = None

    def is_alarm_set(self) -> bool:
        return self._alarm_time is not None

    def set_alarm(self, alarm_time):
        if alarm_time != self.time:
            self._alarm_time = alarm_time
            return alarm_time
        raise ValueError("You cannot set the alarm to be the current time")

    @staticmethod
    def get_every_hour():
        return [f"{hour:02d}" for hour in range(24)]

    @staticmethod
    def get_every_minute():
        return [f"{minute:02d}" for minute in range(60)]
