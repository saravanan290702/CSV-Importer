[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_IojtdoU)


## ✨ **Problem Statement: Crafting a CSV Importer for Google Sheets** ✨

**Context**:
Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file import.
Features.


## Developer's Section
### Requirements

1. Python 3.10
2. Visual Studio Code
  
### Libraries Required

```bash
pip install Flask
pip install gspread
pip install google-auth-oauthlib
pip install pandas
pip install google-auth
pip install google-auth-httplib2
pip install google-api-python-client
pip install oauth2client
```
### Getting Started
- Clone the repository to the local computer and unzip the folder.
- Open the folder in VS Code.
- Open the terminal and run The command ```bash pip install -r requirements.txt ``` to install the required packages.
- Now in the terminal type the command ```python app.py ``` to run the flask application.
- The application should be visible in the ```Running on http://127.0.0.1:5000``` running on the local host now open the link by pressing alt + right click on the Link

### What to do Next
- Now type in the name of the google sheet you want to create and press "Create Button", this should create a google sheet and give us a link to it.
- Copy this and paste it into the next section "Google Sheet URL:" and add a Email Id to provide the permission for the user to be able to view and edit the Google Sheet.
- Finally for importing a csv file to the google sheet copy the Google Sheet id, For example ```https://docs.google.com/spreadsheets/d/1U1B1xARTWXzmRrr_SnK7GuYTT08kqPj-ymdDpioD6Ts``` if this is the generated link then copy ```1U1B1xARTWXzmRrr_SnK7GuYTT08kqPj-ymdDpioD6Ts``` Which will be the google sheet id.
- Drag and drop the csv file which you wan to import to the google sheet, then press on the "upload csv".
- Congratulations You have successfully imported a csv file to a newly created google sheet or a existing google sheet.


### Video For Demonstration



