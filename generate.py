import locale
from datetime import date, time, timedelta
from jinja2 import Template

# Setze Region für Sprache
locale.setlocale(locale.LC_TIME, "de_DE")

with open("template.html", "rb") as F:
    templatetext = F.read().decode("utf-8")

tempi = Template(templatetext)

year = 2022

start_date = date(year, 1, 1)

real_start_date = start_date - timedelta(days=start_date.weekday())
current_date = real_start_date

end_date = date(year, 12, 31)

real_end_date = end_date + timedelta(days=(6 - end_date.weekday()))

dates = []

while current_date <= real_end_date:
    dates.append(current_date)
    current_date += timedelta(days=1)    

anz_wochenseiten = len(dates) // 7

seiten = []
for wdx in range(anz_wochenseiten):
    
    # Monatsübersicht
    if len(seiten) == 0 or \
            seiten[-1]["monat"] != dates[wdx * 7 + 6].strftime("%B"):
        
        wochen = []
        for i in range(4):
            tage = []
            for j in range(7):
                tage.append((dates[wdx * 7]+timedelta(days = i * 7 + j)).strftime("%d"))
            wochen.append(tage)


        seiten.append(
            {
                "monat": dates[wdx * 7 + 6].strftime("%B"),
                "type": "Uebersicht",
                "wochen": wochen,
            }
        )

    #Wochenseite
    seite = {
        "monat": dates[wdx * 7 + 6].strftime("%B"),
        "type": "Woche",
        "tage": [],
        }
    for tdx in range(7):
        day = dates[(wdx * 7) + tdx]
        seite['tage'].append(
            {
                "name": day.strftime("%A"),
                "table-ID": tdx % 2 + 1,
                "datum": day.strftime("%d.%m."),
            }
        )
    seite['tage'].append(
            {
                "name": "Notizen",
                "table-ID": 2,
                "datum": "",
            }
        )
    seiten.append(seite)  

outstring = tempi.render(seiten = seiten)

with open("renderedhtml.html", "wb") as F:
    F.write(outstring.encode('utf-8'))






