import os
from twilio.rest import Client
#Your Account Sid and Auth Token from twilio.com/console
#and set the environment variables.See http://twil.io/secure
account_sid = 'AC022a414e9daa617a405141603f0f3733'
auth_token = '4129d6a5b83e8219cbc3a71fa43ec08c'
client = Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    print(user_code,phone_number)
    message=client.messages.create(
                                 body=f'\nAssalom alaykum, sizning tasdiqlash kodingiz: {user_code}',
                                 from_='+19106657763',
                                 to=f'{phone_number}')
    print(message.sid)
