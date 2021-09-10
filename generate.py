
with open("kalender.html", "r") as F:
    htmltext = F .read()

htmltext = htmltext.replace("[[MONAT]]", "JANUAR")

with open("kalender_1.html", "w") as F:
    F.write(htmltext)






