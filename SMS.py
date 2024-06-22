from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Your phone number
twilio_phone_number = '+917088642875'
# The phone number you want to send the SMS to
to_phone_number = '+919760552706'

# The message you want to send
message_body = 'Hello, this is a test message from Manoj Kuamr'

message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=to_phone_number
)

print(f"Message sent! SID: {message.sid}")
