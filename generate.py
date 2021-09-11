from jinja2 import Template


with open("template.html", "r") as F:
    templatetext = F .read()

tempi = Template(templatetext)

outstring = tempi.render(wochen = [
    {"monat": "Januar", 
    "tage": [    
        {"name": "Montag", "table-ID": 1, "datum": "06.09."},
        {"name": "Dienstag", "table-ID": 2, "datum": "07.09."},
        {"name": "Mittwoch", "table-ID": 1, "datum": "08.09."}]}])

with open("renderedhtml.html", "w") as F:
    F.write(outstring)






