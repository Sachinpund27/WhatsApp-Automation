from twilio .rest import Client
from datetime import datetime, timedelta
import time

account_sid = ''
auth_token = ''

client=Client(account_sid , auth_token)

def send_whatsapp_message (recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message send successfully! Message SID {message.sid}')
    except Exception as e:
        print('An error occurred')


name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient Whatsapp number with county code (e.g +91965..): ')
message_body =  input (f'enter the message you want to send to {name}: ')

date_str = input('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24hours format): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message scheduled to be send to {name} at {schedule_datetime}.')
    time.sleep(delay_seconds)#1000
    send_whatsapp_message(recipient_number, message_body )
