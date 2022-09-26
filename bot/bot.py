#-*- coding: utf-8 -*-
from telegram.ext import *
import Constants as keys
import Responses as R

def start_command(update, context):
    """ This function starts the bot """
    update.message.reply_text("encenent el bot")

def handle_message(update, context):
    """ Funció per a gestionar els missatges de l'usuari sense introduïr comandes"""
    text = str(update.message.text).lower()

    # Responses que cridem desde l'altre arxiu, on hi tenim tota la logica
    response = R.sample_responses(text)

    # Responem
    update.message.reply_text(response)

def main():
    """ Funció main per a poder iniciar el bot"""
    # updater -> El que ens dona la retroacció amb el bot
    updater = Updater(keys.API_KEY, use_context=True)

    # dispatcher -> El que gestiona els events a través de comandes
    dp = updater.dispatcher 

    # add_handler, ens permet afegir-hi comandes al nostre bot
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Start polling per al bot
    updater.start_polling()

    # deixa el bot escoltant
    updater.idle()

# Iniciant el programa
main()
