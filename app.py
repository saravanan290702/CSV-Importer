import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'your-service-account-key.json', scope)
client = gspread.authorize(creds)

# Function to create an empty Google Sheet


def create_empty_sheet(sheet_name):
    new_sheet = client.create(sheet_name)
    return new_sheet

# Function to add a user with permission to view and edit the sheet


def add_user_permission(sheet, email):
    sheet.share(email, perm_type='user', role='writer')

# Main route to render the HTML form


@app.route('/')
def index():
    # Pass sheet_url and permission_message as None initially
    return render_template('index.html', sheet_url=None, permission_message=None)

# Route to handle the form submission for creating a sheet


@app.route('/create_sheet', methods=['POST'])
def create_sheet_route():
    sheet_name = request.form.get('sheet_name')
    new_sheet = create_empty_sheet(sheet_name)
    # Render template with the sheet URL
    return render_template('index.html', sheet_url=new_sheet.url, permission_message=None)

# Route to handle the form submission for adding user permissions


@app.route('/add_permission', methods=['POST'])
def add_permission_route():
    sheet_url = request.form.get('sheet_url')
    user_email = request.form.get('user_email')

    # Extract the sheet key from the URL
    sheet_key = sheet_url.split('/')[-1]

    # Get the sheet by key
    sheet = client.open_by_key(sheet_key)

    add_user_permission(sheet, user_email)
    permission_message = f"Permission added for {user_email} on {sheet.title}"
    # Render template with the permission message
    return render_template('index.html', sheet_url=sheet_url, permission_message=permission_message)


# Route to handle CSV upload and import
@app.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    success_message = None  # Initialize success_message to None
    if request.method == 'POST':
        # Get the Google Sheet ID or URL from the form
        spreadsheet_id = request.form['spreadsheet_id']

        # Open the specified Google Sheet
        sheet = client.open_by_key(spreadsheet_id)

        # Get the first worksheet
        worksheet = sheet.get_worksheet(0)

        # Import CSV data into the worksheet
        csv_file = request.files['csv_file']

        try:
            # Read and decode the CSV file using the appropriate encoding
            csv_contents = csv_file.read().decode('ISO-8859-1')

            # Split the CSV contents into rows
            csv_rows = csv_contents.split('\n')

            # Remove any empty rows
            csv_rows = [row for row in csv_rows if row.strip()]

            # Convert the CSV rows into a list of lists (rows and columns)
            csv_data = [row.split(',') for row in csv_rows]

            # Update the worksheet with the CSV data
            worksheet.update('A1', csv_data)

            success_message = "CSV file imported successfully."  # Set success_message

        except Exception as e:
            return redirect(url_for('error', error_message=str(e)))

    return render_template('index.html', sheet_url=None, permission_message=None, success_message=success_message)  # Pass success_message to the template



# Route for success message


@app.route('/success')
def success():
    return 'CSV file imported successfully.'

# Route for error message


@app.route('/error/<string:error_message>')
def error(error_message):
    return render_template('error.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)