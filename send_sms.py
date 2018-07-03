from twilio.rest import Client
from credentials import account_sid, outh_token, my_cell, my_twilio

client = Client(account_sid, outh_token)

my_msg = ''.join(['Bloody hell!!\n' for i in range(9)])

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
