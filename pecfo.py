import os

# from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes
from modelos.pecfo import Pecfo

from utils import error_letra

CHOOSING, S_PUNTAJE_TOTAL, S_CONCIENCIA_SILABICA, S_CONCIENCIA_FONEMICA = range(4)


edades_tecal = [
    ['4 - 4.11 años'],
    ['5 - 5.11 años'],
    ['6 - 6.11 años'],
    ['7 - 7.11 años'],
    ['Volver'],
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def start_pecfo(update, context):
    update.message.reply_text(
        'Para el cálculo de PECFO primero debe definir la edad: ',
        reply_markup=markup_edad)
    return CHOOSING

def set_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        f"Edad es {text}.\nEscriba el puntaje total.")

    return S_PUNTAJE_TOTAL


def set_puntaje_total(update, context):
    text = update.message.text
    context.user_data['puntaje_total'] = text
    update.message.reply_text(
        f"Puntaje total: {text}.\nEscriba el puntaje de conciencia silábica")
    return S_CONCIENCIA_SILABICA

def set_conciencia_silabica(update, context):
    text = update.message.text
    context.user_data['conciencia_silabica'] = text
    update.message.reply_text(
        f"Puntaje de conciencia silábica: {text}.\nEscriba el puntaje de conciencia fonémica")
    return S_CONCIENCIA_FONEMICA

def set_conciencia_fonemica(update, context):
    text = update.message.text
    context.user_data['conciencia_fonemica'] = text
    ud = context.user_data
    individuo = Pecfo(ud['edad'][0], ud['puntaje_total'], ud['conciencia_silabica'], ud['conciencia_fonemica'])
    update.message.reply_text(
        f"Puntaje de conciencia fonémica: {text}.\n\nResultados:\n\n{individuo}",
        reply_markup=markup_edad)
    return CHOOSING

def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END


def pecfo_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('pecfo', start_pecfo)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(4 - 4.11 años|5 - 5.11 años|6 - 6.11 años|7 - 7.11 años)$'),
                    set_edad
                )
            ],
            S_PUNTAJE_TOTAL: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_puntaje_total
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_CONCIENCIA_SILABICA: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_conciencia_silabica
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_CONCIENCIA_FONEMICA: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_conciencia_fonemica
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ]
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
    dispatcher.add_handler(pecfo_conversation_handler())

    updater.start_polling()
