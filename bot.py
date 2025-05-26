from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 관리자 텔레그램 ID 리스트 (본인 ID로 변경하세요)
ADMINS = [8069493255]  # 예: [8135523315] 이런 식으로

# /start 명령어 핸들러 함수
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("안녕하세요! 상담봇입니다. 무엇을 도와드릴까요?")

# 사용자가 보낸 메시지를 관리자들에게 전달하는 핸들러 함수
async def forward_to_admins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    # 관리자가 보낸 메시지는 무시 (관리자 자신에게는 전달하지 않음)
    if user.id in ADMINS:
        return

    forward_text = f"📩 사용자 @{user.username or user.first_name} (ID: {user.id}) 님이 보낸 메시지:\n{message.text}"

    for admin_id in ADMINS:
        try:
            await context.bot.send_message(chat_id=admin_id, text=forward_text)
        except Exception as e:
            print(f"관리자 {admin_id}에게 메시지 전달 실패: {e}")

if __name__ == '__main__':
    TOKEN = "8135523315:AAF4UQ9NuSKIkhWj7Hb7nXKv0QGyqWpiWQg"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    # 텍스트 메시지를 받으면 관리자에게 전달하는 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & (~filters.User(user_id=ADMINS)), forward_to_admins))

    print("봇이 실행 중입니다...")
    app.run_polling()

