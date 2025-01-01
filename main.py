import pywhatkit as kit 
import datetime

now = datetime.datetime.now()

phone_number = input("+254791431287")
message = input("Hello, this is a test message")

kit.sendwhatmsg(phone_number, message, now.hour, now.minute + 1)
print("Message sent successfully")