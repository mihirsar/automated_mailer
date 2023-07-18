import smtplib
import datetime as dt
import random
import pandas

app_password = "APP PASSWORD"
my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"


# obtained today's date etc
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )
# if day_of_week == 5:
#
#     with open("quotes.txt") as q_file:
#         all_quotes = q_file.readlines()
#         quote = random.choice(all_quotes)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=app_password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="mihirsardesai03452@gmail.com",
#                             msg=f"Subject:Monday Motivation\n\n{quote}")


# date_of_birth = dt.datetime(year= , month= , day=)



