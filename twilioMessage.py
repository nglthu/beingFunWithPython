from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "xxxxx" # Your Account SID from www.twilio.com/console
auth_token  = "xxxxx"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    # Make the call
    call = client.calls.create(to="+64xxx",  # Any phone number
         from_="+64xxx", # Must be a valid Twilio number
         url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    print(call.sid)
except TwilioRestException as e:
    print(e)

