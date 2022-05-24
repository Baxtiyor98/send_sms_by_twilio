from twilio.rest import Client
account_sid = '' # Account SID
auth_token = '' # Auth Token
client = Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    message=client.messages.create(
                                 body=f'Assalom alaykum, sizning tasdiqlash kodingiz: {user_code}',
                                 from_='+19106657763',
                                 to=f'{phone_number}')
    print(message.sid)
