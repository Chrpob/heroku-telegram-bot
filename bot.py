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

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.TEXTO_PRINCIPAL
                            )
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.TEXTO_APOYO
                            )

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='No entendí el comando. Escribe "Volver" para '
                                                                    'volver al menú principal')


BOT_KEY = os.environ['BOT_KEY']

def qetc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Karl Heitmann')

# XXX Función define_abuso_vocal. Aqui el CommandHandler hace el trabajo de filtrar cuando se envia el comando
# /define_abuso_vocal y solo ahi activa esta funcion
def define_abuso_vocal(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.DEF_ABUSO_VOCAL)

# XXX Función define_afasia. Aqui el CommandHandler hace el trabajo de filtrar cuando se envia el comando
# /define_afasia y solo ahi activa esta funcion
def define_afasia(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constantes.DEF_AFASIA)

# XXX Función define. divide la respuesta por espacios. Aquí siempre la primera palabra será '/define', porque
# eso es lo que captura el CommandHandler que amarra esta función en el lazo main.
# El resto de las palabras pueden ser lo que se le ocurra al usuario. Por eso si se entregan 2 palabras, significa
# que el usuario envió '/define algomas', y si recibe 3 palabras, el usuario envió '/define algomas yotromas'
# En el caso que recibe dos palabras, verificamos que la segunda sea 'afasia' y solo ahi devolvemos la definición
# de afasia. Y para cualquier otra cosa devolvemos error. Similarmente en el caso que recibe 3 palabras, verificamos
# que la segunda sea "abuso" y la tercera sea "vocal". Solo ahí devolvemos la definición de "abuso vocal".
# En cualquier otro caso devolvemos el error y le sugerimos al usuario que escriba /define abuso vocal o
# /define afasia para que el comando funcione
def define(update, context):
    palabras = update.message.text.split(' ')
    if (len(palabras) == 2):
        if palabras[1] == 'afasia':
            respuesta = constantes.DEF_AFASIA
        else:
            respuesta = constantes.INCORRECTA_CANTIDAD_DE_ARGUMENTOS
    elif (len(palabras) == 3):
        if (palabras[1] == 'abuso') and (palabras[2] == 'vocal'):
            respuesta = constantes.DEF_ABUSO_VOCAL
        else:
            respuesta = constantes.INCORRECTA_CANTIDAD_DE_ARGUMENTOS
    else:
        respuesta = constantes.INCORRECTA_CANTIDAD_DE_ARGUMENTOS
    context.bot.send_message(chat_id=update.effective_chat.id, text=respuesta)

if __name__ == '__main__':
    updater = Updater(token=BOT_KEY, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    dispatcher.add_handler(CommandHandler('autor', qetc))
    dispatcher.add_handler(CommandHandler('quien_es_tu_creador', qetc))
    dispatcher.add_handler(CommandHandler('define', define)) # XXX Aqui agregamos la funcion /define.
    dispatcher.add_handler(CommandHandler('define_abuso_vocal', define_abuso_vocal)) # XXX Aqui agregamos la funcion /define_abuso_vocal
    dispatcher.add_handler(CommandHandler('define_afasia', define_afasia)) # XXX Aqui agregamos la funcion /define_afasia

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

