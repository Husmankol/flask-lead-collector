from flask import Flask, request, render_template_string, redirect
import csv
import os

app = Flask(__name__)

# CSV file to store leads
LEADS_FILE = 'leads.csv'

# Ensure CSV file exists
if not os.path.exists(LEADS_FILE):
    with open(LEADS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])

# HTML form template
FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Husman Leads Collector</title>
</head>
<body>
    <h2>Join our list!</h2>
    <form method="POST">
      Name: <input name="name" required><br>
      Email: <input name="email" type="email" required><br>
      <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Thank you page
THANK_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Thank You!</title>
</head>
<body>
    <h2>Thank you for joining our list!</h2>
    <p>You are now subscribed. 🎉</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if name and email:
            # Save to CSV
            with open(LEADS_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, email])
            # Show thank you page
            return render_template_string(THANK_HTML)
    # Show form page
    return render_template_string(FORM_HTML)

@app.route('/leads')
def view_leads():
    # Show all collected leads in a simple HTML table
    leads = []
    with open(LEADS_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        leads = list(reader)

    table_html = "<h2>Collected Leads</h2><table border='1'><tr><th>Name</th><th>Email</th></tr>"
    for lead in leads:
        table_html += f"<tr><td>{lead[0]}</td><td>{lead[1]}</td></tr>"
    table_html += "</table>"
    return table_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

