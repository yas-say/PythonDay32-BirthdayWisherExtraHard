##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
print(now.date())

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for _ in data_dict:
    year = _['year']
    month = _['month']
    day = _['day']

    if month < 10:
        month = f"0{month}"

    if day < 10:
        day = f"0{day}"

    formatted_date = f"{year}-{month}-{day}"
    print(formatted_date)

    if str(now.date()) == formatted_date:
        print("here")
        bday_name = _['name']
        bday_email = _['email']

        mail_number = random.randint(1,3)
        mail = f"./letter_templates/letter_{mail_number}.txt"

        with open(mail) as file:
            content = file.read()

        mod_content = content.replace("[NAME]",bday_name)
        print(mod_content)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="sonbonton420@gmail.com", password="yfauhpizpdniudyn")
            connection.sendmail(from_addr="sonbonton420@gmail.com", to_addrs="yasowant@live.com", msg=f"Subject:Happy Birthday \n\n test")

# 4. Send the letter generated in step 3 to that person's email address.




