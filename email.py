import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL="safenestmecia@outlook.com"
TO_EMAIL = "vipraneedstomail@gmail.com"
PASSWORD = getpass.getpass("Enter password:  ")

MESSAGE = """Subject: HELP NEEDED

Hi, I am Vipra

I need HELP!!!

"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code}{response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code}{response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code}{response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit