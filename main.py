import datetime as dt
import pandas
import random
import smtplib
today = dt.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data.row["month"], data.row["day"]): data_row for (index, data_row) in data.iterrows()}

my_email = "Put your email here"
# make sure put app passwords https://support.google.com/mail/answer/185833?hl=en to see more details
password = "Put your password here"

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME", birthday_person["name"])

    with smtplib.SMTP("stmp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday! \n\n{contents}"
        )
