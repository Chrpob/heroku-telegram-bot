# Direccion telegram: t.me/fonocalculadorabot.

import os
import logging

from telegram import (Poll, ParseMode, KeyboardButton, KeyboardButtonPollType)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import CommandHandler
from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters, PollAnswerHandler

from telegram.utils.helpers import mention_html

import edna, tecal, idtel, pecfo, stsg, teprosif, tevi

import constantes

token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.TEXTO_PRINCIPAL
                            )

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='No entendí el comando. Escribe "Volver" para '
                                                                    'volver al menú principal')
    
def qetc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Karl Heitmann')

def define_abuso_vocal(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.DEF_ABUSO_VOCAL)

def define_afasia(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.DEF_AFASIA)

if __name__ == '__main__':
    updater = Updater(token=BOT_KEY, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    dispatcher.add_handler(CommandHandler('autor', qetc))
    dispatcher.add_handler(CommandHandler('quien_es_tu_creador', qetc))
    dispatcher.add_handler(CommandHandler('define_abuso_vocal', define_abuso_vocal))
    dispatcher.add_handler(CommandHandler('define_afasia', define_afasia))

    dispatcher.add_handler(edna.conv_handler())
    dispatcher.add_handler(tecal.tecal_conversation_handler())
    dispatcher.add_handler(idtel.idtel_conversation_handler())
    dispatcher.add_handler(pecfo.pecfo_conversation_handler())
    dispatcher.add_handler(stsg.stsg_conversation_handler())
    dispatcher.add_handler(teprosif.teprosif_conversation_handler())
    dispatcher.add_handler(tevi.tevi_conversation_handler())

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()

