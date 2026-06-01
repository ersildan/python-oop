class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if isinstance(hours, int) and 0 < hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)

time = HourClock(7)
print(time.hours)

time.hours = 9
print(time.hours)
time.hours = 15     # ValueError: Некорректное время
HourClock('pizza')  # ValueError: Некорректное время