import instaloader
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6690645199:AAE61K6_mxQvoGnvpCCo_Dc2q3iD2piF2n4'
bot = None
L = instaloader.Instaloader()

# Set a custom name for your bot
BOT_NAME = "S_P Insta Info Bot"

def start(update: Update, context: CallbackContext):
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton('👨🏻‍💻 Developer', url='https://t.me/S4NCHIT'),
                                     InlineKeyboardButton('🤡 Channel', url='https://t.me/+Q5RcaQe268lmYmI9')]])

    update.message.reply_text(
        text=f"🎉 Hii {update.message.from_user.first_name}\n\n"
             f"😊 Welcome To {BOT_NAME}\n\n"
             f"👋 Hope You Enjoy This Bot\n\n"
             f"🔍 Please Send The Instagram Username 👤",
        reply_markup=buttons
    )

def get_instagram_info(update: Update, context: CallbackContext):
    # Send "Wait a second..." message
    update.message.reply_text("⏰ Wait A Second...")

    username = update.message.text.strip().lstrip('@')  # Remove "@" symbol if present

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        account_name = profile.full_name  # Get the Instagram account name (full name)

        username = profile.username
        user_id = profile.userid
        followers = profile.followers
        following = profile.followees
        num_posts = profile.mediacount
        profile_url = f"https://www.instagram.com/{username}/"
        is_private = profile.is_private

        if is_private:
            update.message.reply_text("🤨 This Account Is Private. Profile Information Can't Be Accessed.")
        else:
            response = (
                f"»»»𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍«««\n\n"
                f"•🤴🏻 Name: {account_name}\n\n"
                f"•🚨 Username: @{username}\n\n"
                f"•🆔 User ID: {user_id}\n\n"
                f"•👥 Followers: {followers}\n\n"
                f"•👥 Following: {following}\n\n"
                f"•📷 Number of Posts: {num_posts}\n\n"
                f"•🔒 Account Type: {'Private' if is_private else 'Public'}\n\n"
                f"•🔗 Profile URL: {profile_url}\n\n"
                f"•🚀 Developer: @S4NCHIT"
            )

            update.message.reply_text(response)

    except instaloader.exceptions.ProfileNotExistsException:
        update.message.reply_text("🧐 InstaGram Account Not Found.")
    except Exception as e:
        logging.error(f"❌ Error Occurred: {e}")
        update.message.reply_text("❌ Error Occurred While Fetching Instagram Profile Details.")

def main():
    global bot
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot = Updater(TOKEN, use_context=True)
    dp = bot.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_instagram_info))

    # Start the bot polling with clean=True for infinity polling and auto-restart
    bot.start_polling(clean=True)

    # Run the bot until the program is interrupted (e.g., with Ctrl+C)
    bot.idle()

if __name__ == "__main__":
    main()
