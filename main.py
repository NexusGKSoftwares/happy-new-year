import pywhatkit as kit
from datetime import datetime

# Get the current time
now = datetime.now()

# Prompt the user for the phone number and message
phone_number = input("Enter the phone number with the country code (e.g., +254791431287): ")
message = input("Enter the message to send: ")

# Send the WhatsApp message
try:
    kit.sendwhatmsg(phone_number, message, now.hour, now.minute + 1)
    print("Message sent successfully")
except Exception as e:
    print(f"An error occurred: {e}")
