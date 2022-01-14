import re
from gsheets import Sheets
from datetime import datetime
import os


CURRENT_YEAR = datetime.now().year

class schedule:
    """[summary]
    """

    def __init__(self, url) -> None:
        self.sheets = Sheets.from_files('credentials.json', 'storage.json')
        self.schedule = self.sheets.get(url)
        self.personnal_schedule = None
    
    def define_schedule(self, name):

        type_of_schedule = ['SAM', 'BAR', 'ACCUEIL']
        poste = ['SERVEUR', 'BARMAN', 'AIDE-BAR', 'ACCUEIL', 'COORDONATEUR', 'SUITEUR']
        current_poste = None
        personnal_schedule = {}

        for schedule in type_of_schedule:
            
            
            id = self.schedule.find(schedule).id
            schedule_to_check = self.schedule[id]

            current_poste = self.change_poste(schedule)
            
            self.schedule_to_dict(schedule_to_check, poste, current_poste, name, personnal_schedule)



               
                  
        self.personnal_schedule = personnal_schedule
        

    def change_poste(self, schedule):

        current_poste = None
        if schedule == 'SAM':
            current_poste = 'SERVEUR'
        elif schedule == 'BAR':
            current_poste = 'BARMAN'
        elif schedule == 'ACCUEIL':
            current_poste = 'ACCUEIL'
        return current_poste
    





    def schedule_to_dict(self, schedule, poste, current_poste, name, personnal_schedule):
        date_row = None
        current_date = None
        for row in range(1,60):
            for col in range(8):
                try:

                    
                    content = schedule.at(row=row, col=col)
                    
                    if col == 0:
                        if content == "TEMPS PLEIN":
                            date_row = row

                        if content in poste:
                            current_poste = content
                        elif content.lower() != name.lower():
                            break
                    else:
                        if content:
                            content_changed = content
                            content_changed  = ''.join(i for i in content_changed  if i in "1234567890;:")
                            content_changed  = content_changed .split(";")
                            content_changed  = [x for x in content_changed  if x]
                            if content_changed :
                                for shift in content_changed :
                                    
                                    shift = shift.split(":")
                                    shift.append(0)
                                    if int(shift[0]) < 7:
                                        date = datetime.strptime(f'{(schedule.at(row=date_row, col=col).replace("-","/") )} {int(shift[0]) + 12}:{shift[1]}', '%Y/%m/%d %H:%M')
                                    else:
                                        date = datetime.strptime(f'{(schedule.at(row=date_row, col=col).replace("-","/") )} {shift[0]}:{shift[1]}', '%Y/%m/%d %H:%M')
                                    if current_poste not in personnal_schedule.keys():
                                        personnal_schedule[f"{current_poste}"] = []
                                    personnal_schedule[f"{current_poste}"].append([date, content])

                                
                
        
        
                        
                except Exception as E:
                    #print(E)
                    pass









if __name__ == "__main__":
    Current_schedule = schedule(os.getenv('SHEETS'))
    Current_schedule.define_schedule('JÉRÉMIE')
    print(Current_schedule.personnal_schedule)
    