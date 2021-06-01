#!/usr/bin/env python3

# Author: Racter Liu (Racterub / root@racterub.me)

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
        caption = update.message['caption']
        context.bot.sendAudio(
            chat_id = -1001264182630,
            filename = fileName,
            caption = performer,
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

def message_handler(update, context):
    context.bot.sendMessage(
        chat_id=-1001264182630,
        text=f"{update.message.text}"
    )


if __name__=='__main__':
    updater = Updater(token="1821784179:AAHQWfHb9X5s-F6QM5A3FbwRHOgl4DgVkFM", use_context=True)
    dispatcher = updater.dispatcher

    #Add Image/File handler
    dispatcher.add_handler(
        MessageHandler(
            (Filters.audio | Filters.photo) & Filters.user(username=f"@Pgffhjsejahjj"),
        file_handler
        )
    )
    #Add Message handler
    dispatcher.add_handler(
        MessageHandler(
            (Filters.text | (~Filters.command)) & Filters.user(username=f"@Pgffhjsejahjj"),
            message_handler
        )
    )

    updater.start_polling()
