class SmartThermostat:
    def __init__(self, current_temp):
        self.__current_temp = current_temp
    
    def get_temp(self):
        return self.__current_temp
    
    def set_temp(self, new_temp):
        if 16 <= new_temp <= 30: 
            self.__current_temp = new_temp
        return None

thermo = SmartThermostat(20)
thermo.set_temp(25)
thermo.set_temp(35) # This should be ignored
print(thermo.get_temp())