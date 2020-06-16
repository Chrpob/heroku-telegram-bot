import os

# from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes

from utils import error_letra

CHOOSING, S_, S_, S_, S_= range(5)


edades_tecal = [
    ['4 - 4.11 años'],
    ['Volver'],
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def start_(update, context):
    return CHOOSING

def set_edad(update, context):
    update.message.reply_text(
        'Para el cálculo de  primero debe definir la edad: ',
        reply_markup=markup_edad)

    return S_


def set_(update, context):
    pass

def set_(update, context):
    pass

def set_(update, context):
    pass

def set_(update, context):
    # Calculo de individuo
    pass

def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END



def _conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('tecal', start_)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(3 - 3.11 años|4 - 4.11 años|5 - 5.11 años|6 - 6.11 años)$'),
                    set_edad
                )
            ],
            S_: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_
                ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            S_: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_
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
    dispatcher.add_handler(tecal_conversation_handler())

    updater.start_polling()
