#!/usr/bin/env python3

# Author: Racter Liu (Racterub / root@racterub.me)
import os
import constants
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def file_handler(update, context):
    """File handler for fowarding images and files to BOT_CHAT_ID
    Ref: https://stackoverflow.com/questions/65882704/how-to-forward-image-to-another-chat-with-telegram-bot-python-api
    Args:
        update (Object): Update
        context (Object): Context
    """
    if update.message['photo'] == []:
        # File
        fileID = update.message['audio']['file_id']
        fileName = update.message['audio']['file_name']
        performer = update.message['audio']['performer']
        title = update.message['audio']['title']
        album = update.message['audio']['album']
        genre = update.message['audio']['genre']
        channel = os.environ.get('CHANNEL_ID')
        context.bot.sendAudio(
            chat_id = channel,
            filename = fileName,
            caption = "✏️ Title: " + title + "\n" + "👤 Artist: " + performer + "\n" + "💽 Album: " + album + "\n" + "🎼 Genre: " + genre, 
            audio = fileID
        )
    else:
        # Image
        fileID = update.message['photo'][-1]['file_id']
        caption = update.message['caption']
        channel = os.environ.get('CHANNEL_ID')
        context.bot.sendPhoto(
        chat_id = channel,
        caption = caption,
        photo = fileID
    )


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(constants.welcome_text)


if __name__=='__main__':
    token = os.environ.get('BOT_TOKEN')
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    #Add Image/File handler
    dispatcher.add_handler(
        MessageHandler(
            (Filters.audio | Filters.photo),
        file_handler
        )
    )

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
