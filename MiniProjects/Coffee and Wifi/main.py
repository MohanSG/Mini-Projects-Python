from csv import DictWriter
from random import choices
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from requests import URLRequired
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL(require_tld=True, message="Invalid URL Format")])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired()], choices=[("☕", "☕"),
                                                                                            ("☕☕", "☕☕"),
                                                                                            ("☕☕☕", "☕☕☕"),
                                                                                            ("☕☕☕☕", "☕☕☕☕"),
                                                                                            ("☕☕☕☕☕", "☕☕☕☕☕")])

    wifi_rating = SelectField('Wifi Rating', validators=[DataRequired()], choices=[("✘", "✘"),
                                                                                        ("💪", "💪"),
                                                                                        ("💪💪", "💪💪"),
                                                                                        ("💪💪💪", "💪💪💪"),
                                                                                        ("💪💪💪💪", "💪💪💪💪"),
                                                                                        ("💪💪💪💪💪", "💪💪💪💪💪")])

    power_rating = SelectField('Power Rating', validators=[DataRequired()], choices=[("🔌", "🔌"),
                                                                                           ("🔌🔌", "🔌🔌"),
                                                                                           ("🔌🔌🔌", "🔌🔌🔌"),
                                                                                           ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
                                                                                           ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    print(form)
    if form.validate_on_submit():
        data = request.form
        fields = ['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power']
        new_row = {'Cafe Name': data['cafe'],
                   'Location' : data['location_url'],
                   'Open' : data['open_time'],
                   'Close' : data['closing_time'],
                   'Coffee' : data['coffee_rating'],
                   'Wifi' : data['wifi_rating'],
                   'Power' : data['power_rating']}
        print(data)
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:

            writer = DictWriter(csv_file, fieldnames=fields)
            writer.writerow(new_row)

        return redirect('/cafes')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
