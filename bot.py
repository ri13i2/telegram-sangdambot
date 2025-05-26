from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

ADMINS = [8069493255]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "안녕하세요, 오리엔 인베스트입니다. 원활하고 빠른 상담을 진행하기 위해 아래 항목 기재 부탁드립니다.\n\n"
        "항목1. 기존회원 / 신규회원\n"
        "항목2. 이름\n"
        "항목3. 연락처\n"
        "항목4. 생년월일\n"
        "항목5. 문의내용"
    )

async def forward_to_admins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    if user.id in ADMINS:
        return

    forward_text = (
        f"📩 사용자 @{user.username or user.first_name} (ID: {user.id}) 님이 보낸 메시지:\n"
        f"{message.text}"
    )

    for admin_id in ADMINS:
        try:
            await context.bot.send_message(chat_id=admin_id, text=forward_text)
        except Exception as e:
            print(f"관리자 {admin_id}에게 메시지 전달 실패: {e}")

    await update.message.reply_text("접수 되었습니다. 문의내용 파악 후 신속하게 상담사 연결 도와 드리겠습니다. 잠시만 기다려 주세요.")

if __name__ == '__main__':
    TOKEN = "8135523315:AAF4UQ9NuSKIkhWj7Hb7nXKv0QGyqWpiWQg"

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.User(user_id=ADMINS)), forward_to_admins))

    print("봇이 실행 중입니다...")
    app.run_polling()




