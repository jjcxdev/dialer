import time
import csv
from twilio.rest import Client

# Set up Twilio client
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

phone_number = ""  # Phone number to call
my_number = ""
interval = 5  # Call interval in seconds
delay = 30  # Delay before TwiML is executed in seconds

while True:

    # Place call
    call = client.calls.create(
        to=phone_number,
        from_=my_number,
        # url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        twiml=f'<Response><Say>The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot. The shoe is on the other foot.</Say></Response>',
    )
    print(f"Calling {phone_number}...")

    # Sleep for specified interval
    time.sleep(interval)
