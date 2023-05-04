from battery.battery import Battery
from utils import add_years_to_date

class Spindler_Battery(Battery):
    def __init__(self,current_date,last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced = add_years_to_date(self.last_service_date,2)
        if date_which_battery_should_be_serviced < self.current_date:
            return True
        else:
            return False