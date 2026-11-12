from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


class pHsensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"
    def __str__(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class Tempsensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5°C"
    def __str__(self):
        return "[Temperature Sensor] Reading: 24.5°C"

ph_sensor = pHsensor()
temp_sensor = Tempsensor()
print("\n-----Laboratory Inventory System-----\n")
print(ph_sensor)
print(temp_sensor)
print("----------------------------------------")
