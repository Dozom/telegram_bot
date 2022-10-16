from twilio.rest import Client
import Constants as keys

def sendSms(number, msg):
    """ This function sends an sms to a user """
    client = Client(keys.ACCOUNT_SSID, keys.AUTH_TOKEN)
    message = client.messages \
                    .create(
                        body=msg,
                        from_='+13023053262',
                        to=number
                    )
    print("sms enviat")

def sendSmsToMultipleUsers(phones,msg):
    """ This function sends an sms to multiple users """
    for phone in phones:
        client = Client(keys.ACCOUNT_SSID, keys.AUTH_TOKEN)
        message = client.messages \
                        .create(
                            body=msg,
                            from_='+13023053262',
                            to=phone
                        )
        print("sms enviat")
