# Kalender

# Installation

```bash
pip3 install -r requirements.txt
```

# Usage

The Kalender is rendered using a Python script and a html template. The rendered html gets converted to a pdf file afterwards. This can be done manually or in a automatic headless way. To change things like the region settings or the year, have a look at the help page of the template rendering script:

```bash
python3 generate.py -h
```

## Manual

Run the Python script to render the template.
```bash
python3 generate.py
```

Use print the html file in the opening browser. Ideally, deactivate borders, activate background images, set page type to A4 and deactivate page numbers and footer/header in the print settings.

You can print the file on paper or to an pdf file. The later also features working in document links for faster navigation.


## Headless

To render the pdf file headless, run the following commands:

```bash
python3 generate.py --no-browser
chromium --headless --disable-gpu --print-to-pdf renderedhtml.html --no-margins --run-all-compositor-stages-before-draw --print-to-pdf-no-header
```

Note: You can sublement `chromium` with `google-chrome` if you like.
