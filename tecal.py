import os

from modelos.tecal import Tecal
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes
from utils import error_letra

CHOOSING, VOCABULARIO, MORFOLOGIA, SINTAXIS, TOTAL = range(5)



edades_tecal = [
    ['3 - 3.11 años'],
    ['4 - 4.11 años'],
    ['5 - 5.11 años'],
    ['6 - 6.11 años'],
    ['Volver']
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def set_vocabulario(update, context):
    text = update.message.text
    context.user_data['vocabulario'] = text
    update.message.reply_text(
        'Ha establecido el puntaje de vocabulario: {}. Ahora ingrese la puntuación de morfologia'.format(text.lower()))
    return MORFOLOGIA


def set_morfologia(update, context):
    text = update.message.text
    context.user_data['morfologia'] = text
    update.message.reply_text(
        'Ha establecido el puntaje de morfología: {}. Ahora ingrese la puntuación de sintaxis'.format(text.lower()))
    return SINTAXIS

def set_sintaxis(update, context):
    text = update.message.text
    context.user_data['sintaxis'] = text
    update.message.reply_text(
        'Ha establecido el puntaje de sintaxis: {}. Ahora ingrese la puntuación total'.format(text.lower()))
    return TOTAL

def set_total(update, context):
    text = update.message.text
    context.user_data['total'] = text
    ud = context.user_data
    edad = ud['edad']
    individuo = Tecal(edad[0], ud['vocabulario'], ud['morfologia'], ud['sintaxis'], ud['total'])

    # update.message.reply_text(
    #     'Ha establecido el puntaje de sintaxis: {}.\nEl resultado es el siguiente: \n\n{}'.format(text.lower(), individuo.resultados),
    #     reply_markup=markup_edad)
    update.message.reply_text(
        'Ha establecido el puntaje de sintaxis: {}.\nEl resultado es el siguiente:\n\n{}'.format(text.lower(), individuo),
        reply_markup=markup_edad)
    return CHOOSING

def set_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        f"Edad es {text}. Escriba la puntuación de vocabulario.")

    return VOCABULARIO

def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END

def start_tecal(update, context):
    update.message.reply_text(
        'Para el cálculo de TECAL primero debe definir la edad: ',
        reply_markup=markup_edad)

    return CHOOSING


def tecal_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('tecal', start_tecal)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(3 - 3.11 años|4 - 4.11 años|5 - 5.11 años|6 - 6.11 años)$'),
                    set_edad
                )
            ],
            VOCABULARIO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_vocabulario
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            MORFOLOGIA: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_morfologia
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            SINTAXIS: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_sintaxis
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )],
            TOTAL: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_total
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )],
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
    dispatcher.add_handler(tecal_conversation_handler())

    updater.start_polling()
