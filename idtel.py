import os

from modelos.idtel import Idtel
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes

from utils import error_letra

CHOOSING, S_FONOLOGICO, S_MORFOLOGICO, S_SEMANTICO, S_PRAGMATICO = range(5)

edades_tecal = [
    ['6 - 7.11 años'],
    ['8 - 9.11 años'],
    ['Volver'],
]

markup_edad = ReplyKeyboardMarkup(edades_tecal, one_time_keyboard=True)

def start_idtel(update, context):
    update.message.reply_text(
        'Para el cálculo de IDTEL primero debe definir la edad: ',
        reply_markup=markup_edad)

    return CHOOSING

def set_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        f"Edad es {text}.\nEscriba el *microdominio fonológico*.",
                parse_mode=ParseMode.MARKDOWN)

    return S_FONOLOGICO

def set_fonologico(update, context):
    text = update.message.text
    context.user_data['fonologico'] = text
    update.message.reply_text(
        f"Microdominio fonológico es {text}.\nEscriba el *microdominio morfosintáctico*.",
                parse_mode=ParseMode.MARKDOWN)
    return S_MORFOLOGICO

def set_morfologico(update, context):
    text = update.message.text
    context.user_data['morfologico'] = text
    update.message.reply_text(
        f"Microdominio morfológico es {text}.\nEscriba el *microdominio semántico*.",
                parse_mode=ParseMode.MARKDOWN)
    return S_SEMANTICO


def set_semantico(update, context):
    text = update.message.text
    context.user_data['semantico'] = text
    update.message.reply_text(
        f"Microdominio semántico es {text}.\nEscriba el *microdominio pragmático*.",
                parse_mode=ParseMode.MARKDOWN)
    return S_PRAGMATICO

def set_pragmatico(update, context):
    text = update.message.text
    context.user_data['pragmatico'] = text
    ud = context.user_data
    individuo = Idtel(ud['edad'][0], ud['fonologico'], ud['morfologico'], ud['semantico'], ud['pragmatico'])
    update.message.reply_text(
        f"Microdominio semántico es {text}.\n\nEl resultado es:\n\n{individuo}",
        reply_markup=markup_edad)
    return CHOOSING

def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    user_data.clear()
    return ConversationHandler.END



def idtel_conversation_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('idtel', start_idtel)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(6 - 7.11 años|8 - 9.11 años)$'),
                    set_edad
                )
            ],
            S_FONOLOGICO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_fonologico
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
             ],
            S_MORFOLOGICO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_morfologico
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
             ],
            S_SEMANTICO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_semantico
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
             ],
            S_PRAGMATICO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_pragmatico
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
    dispatcher.add_handler(idtel_conversation_handler())

    updater.start_polling()
