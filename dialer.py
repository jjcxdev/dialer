import time
import csv
from twilio.rest import Client

# Set up Twilio client
account_sid = "AC26575c358683591230883662ece06cb0"
auth_token = "7ac2df20159aaa73b13b5676a6334711"
client = Client(account_sid, auth_token)

phone_number = "14164558684"  # Phone number to call
interval = 30  # Call interval in seconds

while True:
    # Place call
    call = client.calls.create(
        to=phone_number,
        from_="+16693382345",
        url="http://example.com/recorded_message.mp3"
    )
    print(f"Calling {phone_number}...")

    # Sleep for specified interval
    time.sleep(interval)
