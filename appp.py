from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
<form method="POST">
  Name: <input name="name"><br>
  Email: <input name="email"><br>
  <button type="submit">Submit</button>
</form>
'''

leads = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        leads.append({'name': name, 'email': email})
        return f"Thanks {name}, your lead is collected!"
    return render_template_string(html_form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


