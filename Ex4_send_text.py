#sending message to your phone, using twilio

from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = " {account id} "
auth_token  = " {token} "
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Testing from kiking",
    to=" {} ",    # Replace with your phone number
    from_=" {} ") # Replace with your Twilio number
print message.sid
