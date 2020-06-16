import os

# from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes
from modelos.stsg import Stsg

from utils import error_letra

CHOOSING, S_EXPRESIVO, S_RECEPTIVO = range(3)


edades_tecal = [
    ['3 - 3.11 años'],
    ['4 - 4.11 años'],
    ['5 - 5.11 años'],
    ['6 - 6.11 años'],
    ['7 - 7.11 años'],
    ['Volver'],
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def start_stsg(update, context):
    update.message.reply_text(
        'Para el cálculo de STSG primero debe definir la edad: ',
        reply_markup=markup_edad)
    return CHOOSING

def set_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        f"Edad es {text}.\nEscriba el puntaje expresivo.")

    return S_EXPRESIVO


def set_expresivo(update, context):
    text = update.message.text
    context.user_data['expresivo'] = text
    update.message.reply_text(
        f"Puntaje expresivo es {text}.\nEscriba el puntaje receptivo.")
    return S_RECEPTIVO

def set_receptivo(update, context):
    text = update.message.text
    context.user_data['receptivo'] = text
    ud = context.user_data
    individuo = Stsg(ud['edad'][0], ud['expresivo'], ud['receptivo'])
    update.message.reply_text(
        f"Puntaje receptivo es {text}.\nResultados:\n\n{individuo}.",
        reply_markup=markup_edad)
    return CHOOSING

def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END



def stsg_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('stsg', start_stsg)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(3 - 3.11 años|4 - 4.11 años|5 - 5.11 años|6 - 6.11 años|7 - 7.11 años)$'),
                    set_edad
                )
            ],
            S_EXPRESIVO: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_expresivo
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_RECEPTIVO: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_receptivo
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Volver$'), done)]
    )



if __name__ == '__main__':
    import logging

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)
    BOT_KEY = os.environ['BOT_KEY']

    updater = Updater(token=BOT_KEY, use_context=True)
    dispatcher = updater.dispatcher
    # dispatcher.add_handler(CommandHandler('start', edna))
    dispatcher.add_handler(stsg_conversation_handler())

    updater.start_polling()
