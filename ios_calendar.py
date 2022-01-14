from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
import os
import datetime


class ios_calendar:

    def __init__(self, username, shifts) -> None:
        self.calendars = GoogleCalendar(credentials_path='D:\CODE\Schedule St-Hub to IOS\.credentials\credentials.json')
        self.shifts = shifts
        pass
    
    def add_shift(self, shift, poste):

        name = f"{poste} | {shift[1]}"
        hours_to_add = datetime.timedelta(hours = 3)
        start = shift[0]
        end = start + hours_to_add
        event = Event(name,start=start, end=end)
        self.calendars.add_event(event)
    
    def skim_through_dict(self):
        dict_keys = self.shifts.keys()
        for key in dict_keys:
            poste_shifts = self.shifts[key]
            for shift in poste_shifts:
                self.add_shift(shift, key)
        

    



if __name__ == "__main__":
    shifts = {'SERVEUR': [[datetime.datetime(2021, 7, 2, 17, 15), '5:15x']
    , [datetime.datetime(2021, 7, 3, 11, 30), '11:30**;4:45PP']
    , [datetime.datetime(2021, 7, 3, 16, 45), '11:30**;4:45PP']
    , [datetime.datetime(2021, 7, 4, 11, 30), '11:30**;4:45PP']
    , [datetime.datetime(2021, 7, 4, 16, 45), '11:30**;4:45PP']] 
    ,'ACCUEIL': [[datetime.datetime(2021, 7, 2, 11, 30), '11:30x']]}
    my_calendar = ios_calendar(os.getenv('CALENDAR'), shifts )
    my_calendar.add_shift([datetime.datetime(2021, 7, 2, 17, 15), '5:15x'],'SERVEUR')
    my_calendar.skim_through_dict()
