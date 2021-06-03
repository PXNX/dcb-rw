import logging

import discord
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler

TOKEN_DISCORD = "will send it on tg"  # os.getenv('DISCORD_TOKEN')

TOKEN_TELEGRAM = 'will send it on tg'

GROUP = -1001327617858

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


def start(update: Update, context: CallbackContext):
    update.message.reply_text("---Start---")


async def upload(update: Update, context: CallbackContext):
    channel = client.get_channel(761598004942733343)
    await channel.send(update.message.text)


def error(update: object, context: CallbackContext):
    logger.error('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(
        chat_id=-1001338514957,
        text="<b>🤖 Affected Bot</b>\n@" + context.bot.username +
             "\n\n<b>⚠ Error</b>\n<code>" + str(context.error) +
             "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
        parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    updater = Updater(TOKEN_TELEGRAM)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))  # , filters=Filters.chat(VERIFIED_USERS)

    dp.add_handler(MessageHandler(Filters.text, upload))

    dp.add_error_handler(error)  # REMOVE FOR STACKTRACE!!

    client.run(TOKEN_DISCORD) #code works if commented out

    updater.start_polling()
    # updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://ptb-rw-bridge.herokuapp.com/' + TOKEN)
    updater.idle()
