from schedule import schedule
from ios_calendar import ios_calendar
import os




if __name__ == "__main__":
    Current_schedule = schedule(os.getenv('SHEETS'))
    Current_schedule.define_schedule('JÉRÉMIE')
    personnal_schedule = Current_schedule.personnal_schedule
    my_calendar = ios_calendar(os.getenv('CALENDAR'), personnal_schedule )
    
    my_calendar.skim_through_dict()


