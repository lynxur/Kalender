# Kalender

# Installation

```bash
pip3 install -r requirements.txt
```

# Rendering

## Manual

Run the Python script to render the template.
```bash
python3 generate.py
```

Use print the html file in the opening browser. Ideally, deactivate borders, activate background images, set page type to A5 and deactivate page numbers and footer/header in the print settings.

You can print the file on paper or to an pdf file. The later also features working in document links for faster navigation.


## Headless

To render the pdf file headless, run the following commands:

```bash
python3 generate.py --no-browser
chromium --headless --disable-gpu --print-to-pdf renderedhtml.html --no-margins --run-all-compositor-stages-before-draw --print-to-pdf-no-header
```

Note: You can sublement `chromium` with `google-chrome` if you like.