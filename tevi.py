import os

# from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes
from modelos.tevi import Tevi

from utils import error_letra

CHOOSING, S_TECHO, S_ERROR = range(3)


edades_tecal = [
    ['2 - 2.11 años'],
    ['3 - 3.11 años'],
    ['4 - 4.11 años'],
    ['5 - 5.11 años'],
    ['6 - 6.11 años'],
    ['7 - 8.11 años'],
    ['9 - 10.11 años'],
    ['11 - 12.11 años'],
    ['13 - 14.11 años'],
    ['15 - 18.11 años'],
    ['Volver'],
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def start_tevi(update, context):
    update.message.reply_text(
        'Para el cálculo de TEVI primero debe definir la edad: ',
        reply_markup=markup_edad)
    return CHOOSING

def set_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        f"Edad es {text}.\nEscriba el puntaje techo.")
    return S_TECHO


def set_techo(update, context):
    text = update.message.text
    context.user_data['puntaje_techo'] = text
    update.message.reply_text(
        f"Puntaje techo: {text}.\nEscriba el error.")
    return S_ERROR

def set_error(update, context):
    text = update.message.text
    context.user_data['error'] = text
    ud = context.user_data
    individuo = Tevi(ud['edad'][0], ud['puntaje_techo'], ud['error'])
    update.message.reply_text(
        f"Error: {text}.\n\nResultados:\n\n{individuo}",
        reply_markup=markup_edad)
    return CHOOSING

def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END



def tevi_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('tevi', start_tevi)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(2 - 2.11 años|3 - 3.11 años|4 - 4.11 años|5 - 5.11 años|6 - 6.11 años|7 - 8.11 años|9 - 10.11 años|11 - 12.11 años|13 - 14.11 años|15 - 18.11 años)$'),
                    set_edad
                )
            ],
            S_TECHO: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_techo
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_ERROR: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_error
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
    dispatcher.add_handler(tevi_conversation_handler())

    updater.start_polling()
