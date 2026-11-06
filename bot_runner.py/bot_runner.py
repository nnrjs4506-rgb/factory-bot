from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from services import generate_image, generate_text
from database import init_db, add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username or user.first_name)
    await update.message.reply_text(
        "أهلاً فيك في Factory Bot 🔥\n\n"
        "أرسل لي أي وصف وأنا أرسمه لك، أو أرسل /help للمساعدة"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أوامر البوت:\n"
        "/start - بداية\n"
        "/help - المساعدة\n\n"
        "فقط أرسل وصف الصورة وسأرسمها لك."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    await update.message.reply_text("جاري الرسم... 🎨 انتظر ثواني")
    try:
        image_url = generate_image(prompt)
        await update.message.reply_photo(photo=image_url, caption=f"تم! 🎉\n{prompt}")
    except Exception as e:
        await update.message.reply_text(f"صار خطأ: {e}")

def run_bot(token):
    init_db()
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
