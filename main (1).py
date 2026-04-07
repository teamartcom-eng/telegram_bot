import os
import asyncio
from telegram import Update, Bot
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ChatJoinRequestHandler,
)

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError(
        "TELEGRAM_TOKEN secret is missing. Please add it in the Secrets panel."
    )

# ✏️ ADD OR REMOVE CHANNEL IDs HERE:
CHANNEL_IDS = [
    -1003756496817,  # Channel 1
    -1003659535936,  # Channel 2
    # -1001234567890, # Add more channels below (remove the # to activate)
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received /start from {update.effective_user.first_name}")
    await update.message.reply_text(
        "👋 Welcome! I'm Sharvani Bot.\n\nUse /help to see what I can do."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received /help from {update.effective_user.first_name}")
    await update.message.reply_text(
        "🆘 *Help Menu*\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/tips - Get a useful tip",
        parse_mode="Markdown",
    )


async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received /tips from {update.effective_user.first_name}")
    await update.message.reply_text(
        "💡 *Tip of the day:*\n\nStay consistent and keep learning — small daily progress leads to big results! 🚀",
        parse_mode="Markdown",
    )


async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    channel = update.chat_join_request.chat.title
    try:
        await context.bot.send_message(
            chat_id=user.id,
            # ✏️ CHANGE YOUR MESSAGE HERE:
            text="""🔞Special VIP Membership💙👑

All Categories available 😈
➡️Desi Indian 
➡️Indian Porn 
➡️Webseries (Ullu , Hotshots Etc)
➡️Brazzers , Onlyfans , Site Stuffs...
➡️Viral Porns 
➡️R-Rated Movies 
➡️Adult leaked MMS 
More...
👑 1000+ quality Videos Already Uploaded on that channel 🔞◀️
👉And Daily New Videos Adding ✨

🚨Membership Price Rs 999❌❌
🤔 Today Bumper Offer ⬇️⬇️
📣VIP CHANNEL PRICE DROP📉
🔼 (Only for 100 Memebers)🔽

🔘lifetime Membership Price
499  🔠🔠 only✅ (6$)

   🎁Payment Here🎁 
@vip_seller_latest
@vip_seller_latest
@vip_seller_latest
@vip_seller_latest
@vip_seller_latest
@vip_seller_latest

(You will automatically get Joining link of VIP channel after Payment) ✅
➖➖➖➖➖➖➖➖➖➖➖➖
Join our demo channel and paid vip demo  ⬇️⬇️
https://t.me/+OmKU8eLfA1c5MDc9
https://t.me/+IYnf5vafrsY3YWU1

Proof channel 
https://t.me/+jzkCKx1NXOEyYmE1""",
        )
    except Exception as e:
        print(
            f"Failed to message {user.first_name} (ID: {user.id}) from '{channel}': {e}"
        )
        return
    print(
        f"Join request from {user.first_name} (ID: {user.id}) via '{channel}' — message sent"
    )


async def clear_webhook():
    bot = Bot(token=TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook cleared.")


if __name__ == "__main__":
    asyncio.run(clear_webhook())

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("tips", tips))

    for channel_id in CHANNEL_IDS:
        app.add_handler(ChatJoinRequestHandler(handle_join_request, chat_id=channel_id))
        print(f"Watching channel ID: {channel_id}")

    print(
        f"Bot is running and watching {len(CHANNEL_IDS)} channel(s)... Press Ctrl+C to stop."
    )
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
