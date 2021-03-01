##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
MY_EMAIL = "mypython.botmail@gmail.com"
MY_PSWD = "CCLYRDOCTOR2002"
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
today = (dt.datetime.now().month, dt.datetime.now().day)
# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as content:
        birthday_person = birthdays_dict[today]
        letter = content.read()
        final_letter = letter.replace("[NAME]", f"{birthday_person['name']}")
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL,MY_PSWD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthday_person['email'],
        msg=f"Subject:Happy Birthday!\n\n"
            f"{final_letter}")
# 4. Send the letter generated in step 3 to that person's email address. HINT 1: Gmail(smtp.gmail.com),
# Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com) HINT 2: Remember to call
# .starttls() HINT 3: Remember to login to your email service with email/password. Make sure your security setting is
# set to allow less secure apps. HINT 4: The message should have the Subject: Happy Birthday then after \n\n The
# Message Body.
