#-*- coding: utf-8 -*-
from ctypes import resize
#from telegram import ReplyKeyboardMarkup to try something with keyboard in future versions
from telegram.ext import *
import Constants as keys
import SendEmail as email
import SendSms as sms

def start(update, context):
    """ This function starts the bot """
    update.message.reply_text("""
    Welcome to our bot, here you have some commands of our telegram bot:
    Email:
    /send_single_user_email <email>;<subject>;<message> -> Sends one email to a mail
    /send_multiple_users_email <email1>;<email2>:<subject>:<message> -> Sends one email to a multiple emails
    /send_single_user_sms <phone>;<message> -> Sends one sms to a phone
    /send_multiple_users_sms (not working in free version) <phone1>;<phone2>:<message> -> Sends one sms to a multiple users
    """)

def help(update, context):
    """ This function starts the bot """
    update.message.reply_text("""
    Welcome to our bot, here you have some commands of our telegram bot:
    Email:
    /send_single_user_email <email>;<subject>;<message> -> Sends one email to a mail
    /send_multiple_users_email <email1>;<email2>:<subject>:<message> -> Sends one email to a multiple emails
    /send_single_user_sms <phone>;<message> -> Sends one sms to a phone
    /send_multiple_users_sms (not working in free version) <phone1>;<phone2>:<message> -> Sends one sms to a multiple users
    """)

def send_single_user_email(update, context):
    """ This function sends an email to a single user """
    items = update.message.text.split(';')    
    user_email = items[0][items[0].index(' '):]
    user_subject = items[1]
    user_message = items[2]
    print("user email:", user_email)
    print("user subject:", user_subject)
    print("user message:", user_message)
    email.sendemail(user_email,user_subject,user_message)

def send_multiple_users_email(update, context):
    """ this function sends one email to a list of emails """
    items = update.message.text.split(':')    
    user_email = items[0][items[0].index(' ')+1:]
    user_emails = user_email.split(';')
    user_subject = items[1]
    user_message = items[2]
    print("user email:", user_emails)
    print("user subject:", user_subject)
    print("user message:", user_message)
    email.sendemail(user_emails,user_subject,user_message)

def send_single_user_sms(update, context):
    """ This function is used to send a single sms to a user """
    items = update.message.text.split(';')    
    number = items[0][items[0].index(' ')+1:]
    message = items[1]
    sms.sendSms(number,message)

def send_multiple_users_sms(update, context):
    """ This function is used to send sms to multiple numbers"""
    items = update.message.text.split(':')    
    user_phone = items[0][items[0].index(' ')+1:]
    user_phones = user_phone.split(';')
    user_message = items[1]
#    sms.sendSmsToMultipleUsers(user_phones,user_message)

def handle_images(update, context):
    """ This function handle the messages of the user """
    print(update.message.effective_attachment)

def main():
    """ Main function of the bot """
    updater = Updater(keys.API_KEY, use_context=True)
    disp = updater.dispatcher 

    # Bot commands
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("help", help))

    # Email commands
    disp.add_handler(CommandHandler("send_single_user_email", send_single_user_email))
    disp.add_handler(CommandHandler("send_multiple_users_email", send_multiple_users_email))

    # Sms commands
    disp.add_handler(CommandHandler("send_single_user_sms", send_single_user_sms))
    disp.add_handler(CommandHandler("send_multiple_users_sms", send_multiple_users_sms))
    disp.add_handler(MessageHandler(Filters.attachment, handle_images))

    # Bot polling & listening
    updater.start_polling()
    updater.idle()

# Start Main
main()