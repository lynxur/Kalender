import locale
import webbrowser
from typing import Dict, Iterable
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from jinja2 import Template

def get_next_sunday_date(input_date: date) -> date:
    return input_date + timedelta(days=(6 - input_date.weekday()))

def get_previous_monday_date(input_date: date) -> date:
    return input_date - timedelta(days=input_date.weekday())

def build_wochen_seite(input_date: date) -> Dict:
    # Create page dictionary
    seite = {
        "monat": get_next_sunday_date(input_date).strftime("%B"),
        "type": "Woche",
        "tage": [],
        }
    # Iterate over all days in the week
    for i, day in enumerate(date_iterator(input_date, timedelta(days=1), 7)):
        # Create a nested dict for each day
        seite['tage'].append(
            {
                "name": day.strftime("%A"),
                "table-ID": i % 2 + 1,
                "datum": day.strftime("%d.%m."),
            }
        )
    # Append blank "day" for notes to get to an even number on the page
    seite['tage'].append({"name": "Notizen", "table-ID": 2, "datum": ""})
    return seite

def build_monats_ueberblick(input_date: date) -> Dict:
    wochen = []

    current_date = get_previous_monday_date(input_date)
    real_end_date = get_next_sunday_date(input_date + relativedelta(months=1))

    while current_date <= real_end_date:
        tage = []
        for j in range(7):
            tage.append(current_date.strftime("%d"))
            current_date += timedelta(days=1)
        wochen.append(tage)

    return {
            "monat": get_next_sunday_date(input_date).strftime("%B"),
            "type": "Uebersicht",
            "wochen": wochen,
        }

def date_iterator(start_date: date, step: timedelta, num:int) -> Iterable[date]:
    return (start_date + n * step for n in range(num))


# Set region for corret date formating depending on the region
locale.setlocale(locale.LC_TIME, "de_DE")

# Open the template file
with open("template.html", "rb") as F:
    templatetext = F.read().decode("utf-8")

# Create jinja2 template object from the template file content
tempi = Template(templatetext)

# Year parameter, todo argparse
year = 2022

# Create date objects
start_date = date(year, 1, 1)
end_date = date(year, 12, 31)

# Modify start and end date that they begin with a monday and end with a sunday
real_end_date = get_next_sunday_date(end_date)
current_date = get_previous_monday_date(start_date)

# Create all pages of the calendar while iterating through the weeks
seiten = []
while current_date <= real_end_date:
    # Add Monatsübersicht
    if len(seiten) == 0 or seiten[-1]["monat"] != get_next_sunday_date(current_date).strftime("%B"):
       seiten.append(build_monats_ueberblick(current_date)) 
    # Add Wochenseite
    seiten.append(build_wochen_seite(current_date))  
    # Increment to the next week
    current_date += timedelta(days=7)

# Render the dict and list struckture via jinja2 and the loaded template
outstring = tempi.render(seiten = seiten)

# Save the rendered html to the output file
with open("renderedhtml.html", "wb") as F:
    F.write(outstring.encode('utf-8'))

# Open the output file with the webbrowser
webbrowser.open("renderedhtml.html")
