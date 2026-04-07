import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    ChatJoinRequestHandler,
    filters,
)

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError(
        "TELEGRAM_TOKEN secret is missing. Please add it in the Secrets panel."
    )

CHANNEL_IDS = [
    -1003756496817,
    -1003893970181,
    -1003682096987,
    -1003843753081,
    -1003854575520,
    -1003798176026,
]

VIP_MESSAGE = """🔞Special VIP Membership💙👑

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
https://t.me/+O8q7pFuEWndjYTA9
https://t.me/+IYnf5vafrsY3YWU1

Proof channel 
https://t.me/+YUCA8ZnKpug3NWFl"""


async def reply_vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    user = update.effective_user
    print(f"Message from {user.first_name if user else 'unknown'} — sending VIP message")
    await update.message.reply_text(VIP_MESSAGE)


async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.chat_join_request:
        return
    user = update.chat_join_request.from_user
    channel = update.chat_join_request.chat.title
    try:
        await context.bot.send_message(chat_id=user.id, text=VIP_MESSAGE)
    except Exception as e:
        print(f"Failed to message {user.first_name} (ID: {user.id}) from '{channel}': {e}")
        return
    print(f"Join request from {user.first_name} (ID: {user.id}) via '{channel}' — message sent")


async def post_init(application):
    await application.bot.delete_webhook(drop_pending_updates=True)
    print("Webhook cleared.")


if __name__ == "__main__":
    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(MessageHandler(filters.ALL, reply_vip))

    for channel_id in CHANNEL_IDS:
        app.add_handler(ChatJoinRequestHandler(handle_join_request, chat_id=channel_id))
        print(f"Watching channel ID: {channel_id}")

    print(f"Bot is running and watching {len(CHANNEL_IDS)} channel(s)... Press Ctrl+C to stop.")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
