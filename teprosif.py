import os

# from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes
from modelos.teprosif import Teprosif

from utils import error_letra

CHOOSING, S_PSF = range(2)


edades_tecal = [
    ['3 - 3.11 años'],
    ['4 - 4.11 años'],
    ['5 - 5.11 años'],
    ['6 - 6.11 años'],
    ['Volver'],
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def start_teprosif(update, context):
    update.message.reply_text(
        'Para el cálculo de TEPROSIF primero debe definir la edad: ',
        reply_markup=markup_edad)
    return CHOOSING

def set_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        f"Edad es {text}.\nEscriba el *valor total PSF*.",
                parse_mode=ParseMode.MARKDOWN)
    return S_PSF


def set_psf(update, context):
    text = update.message.text
    context.user_data['psf'] = text
    ud = context.user_data
    individuo = Teprosif(ud['edad'][0], ud['psf'])
    update.message.reply_text(
        f"Valor total PSF: {text}.\n\nResultados:\n\n{individuo}",
        reply_markup=markup_edad)
    return CHOOSING


def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END



def teprosif_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('teprosif', start_teprosif)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(3 - 3.11 años|4 - 4.11 años|5 - 5.11 años|6 - 6.11 años)$'),
                    set_edad
                )
            ],
            S_PSF: [
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                    set_psf
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
    dispatcher.add_handler(teprosif_conversation_handler())

    updater.start_polling()
