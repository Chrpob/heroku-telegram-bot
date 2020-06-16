import os

from modelos.edna import Edna, DESEMPENO_NARRATIVO, COMPRENSION_DISCURSO_NARRATIVO
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters
import constantes

from utils import error_letra

CHOOSING, STATE_DESEMPENO_NARRATIVO, STATE_COMPRENSION_DISCURSO_NARRATIVO = range(3)

TERMINAR = 'Volver'


reply_keyboard = [
    ['4 - 4.11 años'],
    ['5 - 5.11 años'],
    ['6 - 6.11 años'],
    ['7 - 7.11 años'],
    ['10 - 10.11 años'],
    ['Volver']
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def edna(update, context):
    update.message.reply_text(
        'Para el cálculo de EDNA primero debe definir la edad: ',
        reply_markup=markup)

    return CHOOSING


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))


def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text(constantes.TEXTO_PRINCIPAL)
    # update.message.reply_text("I learned these facts about you:"
    #                           "{}"
    #                           "Until next time!".format(facts_to_str(user_data)))

    user_data.clear()
    return ConversationHandler.END



def seleccionar_edad(update, context):
    text = update.message.text
    context.user_data['edad'] = text
    update.message.reply_text(
        'Ha seleccionado este rango de edad: {}.\nAhora ingrese la puntuación de Desempeño Narrativo'.format(text.lower()))

    # if text.lower() == '4 - 4.11 años':
    #     update.message.reply_text()
    return STATE_DESEMPENO_NARRATIVO

def set_desempeno_narrativo(update, context):
    text = update.message.text
    context.user_data[DESEMPENO_NARRATIVO] = text
    update.message.reply_text('Desempeño narrativo OK: {}.\nIngrese ahora la puntuación de Comprensión del Discurso Narrativo'.format(text.lower()))
    return STATE_COMPRENSION_DISCURSO_NARRATIVO

def set_comprension_discurso_narrativo(update, context):
    text = update.message.text
    ud = context.user_data
    context.user_data[COMPRENSION_DISCURSO_NARRATIVO] = text
    individuo = Edna(ud['edad'][0], ud[DESEMPENO_NARRATIVO], ud[COMPRENSION_DISCURSO_NARRATIVO])
    update.message.reply_text('Comprensión Discurso Narrativo OK: {}.\nEl calculo es este:\n\n{}'.format(text.lower(), individuo),
                              reply_markup=markup)
    return CHOOSING

def conv_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('edna', edna)],

        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(4 - 4.11 años|5 - 5.11 años|6 - 6.11 años|7 - 7.11 años|10 - 10.11 años)$'),
                    seleccionar_edad
                )
            ],

            STATE_DESEMPENO_NARRATIVO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_desempeno_narrativo
            ),
                MessageHandler(
                    Filters.regex(constantes.REGEX_ONLY_STRINGS),
                    error_letra
                )
            ],
            STATE_COMPRENSION_DISCURSO_NARRATIVO: [MessageHandler(
                Filters.regex(constantes.REGEX_ONLY_NUMBERS),
                set_comprension_discurso_narrativo
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
    dispatcher.add_handler(conv_handler())
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()


