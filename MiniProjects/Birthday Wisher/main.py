import smtplib
import datetime as dt
import random
import pandas
PASS = ''
def send_email(contents):
    my_email = "mohansg12@gmail.com"
    with (smtplib.SMTP("smtp.gmail.com", 587)) as connection:
        connection.starttls()
        connection.login(user=my_email, password=PASS)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="m.ghataurey21@gmail.com",
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv", "r") as data_file:
    data = pandas.read_csv(data_file)
    data_dict = data.to_dict(orient="records")

    for sibling in data_dict:
        sibling_birthday = dt.datetime(sibling["year"], sibling["month"], sibling["day"])
        if sibling_birthday.date() == dt.datetime.now().date():
            number = random.randint(1,3)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            with open(f"letter_templates/letter_{number}.txt", "r") as letter_file:
                letter_contents = letter_file.read()
                letter_contents = letter_contents.replace("[NAME]", sibling["name"])
# 4. Send the letter generated in step 3 to that person's email address.
                send_email(letter_contents)