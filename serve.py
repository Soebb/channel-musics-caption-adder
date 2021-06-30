#!/usr/bin/env python3

# Author: Racter Liu (Racterub / root@racterub.me)
import os
from telegram.ext import Updater, Filters, MessageHandler


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
        context.bot.sendAudio(
            chat_id = -1001264182630,
            filename = fileName,
            caption = performer + "-" + title,
            audio = fileID
        )
    else:
        # Image
        fileID = update.message['photo'][-1]['file_id']
        caption = update.message['caption']
        context.bot.sendPhoto(
        chat_id = -1001264182630,
        caption = caption,
        photo = fileID
    )


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

    updater.start_polling()
