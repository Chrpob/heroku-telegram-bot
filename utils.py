from telegram.ext import ConversationHandler

def error_letra(update, context):
    update.message.reply_text('Mensaje inválido. Por favor ingrese un número entero. Si esto no funciona, Envíe el mensaje "Volver"')
    if update.message.text == 'Volver':
        return ConversationHandler.END
    else:
        return None

