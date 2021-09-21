# Kalender

A simple minimalistic calender for paper or pdf usage. There is an overview for each month with all its dates and a page for each week with extra space for notes. 

![Unbenannt](https://user-images.githubusercontent.com/82907637/134244889-3042d7e7-c5a4-4d10-9218-422018c173b8.png)

## Download
To simply get the pdf for your language simply download the [latest release](https://github.com/lynxur/Kalender/releases/latest).

## Installation

To install the nessesary dependencies type:

```bash
pip3 install -r requirements.txt
```

## Usage

The Kalender is rendered using a Python script and a html template. The rendered html gets converted to a pdf file afterwards. This can be done manually or in a automatic headless way. To change things like the region settings or the year, have a look at the help page of the template rendering script:

```bash
python3 generate.py -h
```

### Manual

Run the Python script to render the template.
```bash
python3 generate.py
```


Use print the html file in the opening browser. Ideally, deactivate borders, activate background images, set page type to A4 and deactivate page numbers and footer/header in the print settings.

You can print the file on paper or to a pdf file. The later also features working in document links for faster navigation.


### Headless

To render the pdf file headless, run the following commands:

```bash
python3 generate.py --no-browser
chromium --headless --disable-gpu --print-to-pdf renderedhtml.html --no-margins --run-all-compositor-stages-before-draw --print-to-pdf-no-header
```

Note: You can sublement `chromium` with `google-chrome` if you like.
