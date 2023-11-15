# Створіть базовий клас Clock, який містить атрибути
# години та хвилини. Від цього базового класу
# успадковуйте два класи: AnalogClock та DigitalClock.
# Клас AnalogClock повинен мати метод display_time,
# який виводить поточний час у форматі
# "години:хвилини". Клас DigitalClock повинен мати
# метод display_time, який виводить поточний час у
# цифровому форматі "гг:хх".
# Створіть об'єкти кожного класу та виведіть
# поточний час за допомогою методу display_time.

from datetime import datetime

class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @staticmethod
    def display_time():
        now = datetime.now()
        formatted_time = now.strftime("%H:%M")
        print(formatted_time)

class AnalogClock(Clock):
    
    def convert_time(self):
        Clock.display_time()

class DigitalClock(Clock):
    def convert_time(self):
        
        total_minutes = self.hours * 60 + self.minutes
        adjusted_hours = total_minutes // 60
        adjusted_minutes = total_minutes % 60

        days = adjusted_hours // 24
        final_hours = adjusted_hours % 24

        if days > 0:
            print(f"{days} days {final_hours:02d}:{adjusted_minutes:02d}")
        else:
            print(f"{final_hours:02d}:{adjusted_minutes:02d}")
        

analog_clock = AnalogClock(1,1)
digital_clock = DigitalClock(99999, 45)
analog_clock.display_time()
digital_clock.convert_time()
