# StHub-Schedule

One of the few thing I did not like about my job at St-Hubert was 
how old school it used to be. The schedule for the week was always
printed out and pinned on a board at my workplace. If I wanted it on 
my phone, I had to manually enter my shifts into my calendar. I 
decided to change that with the help of python and the google API.
Since the schedule was printed out on a google sheets. I asked my
boss for the link to it. Then the program uses the Google API to 
skim through the google sheets, finds my name and the correct date 
of the week and finds all the days I am working that current week. 
It then uses the Google Calendar API to create corresponding events
for when I work. Here is an example: 

![Alt text](schedule.PNG?raw=true "Example")