from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ✅ 관리자 텔레그램 ID (본인 ID로 바꿔주세요)
ADMINS = [8069493255]

# ✅ /start 명령 처리
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = (
        "안녕하세요, 오리엔 인베스트 입니다.\n"
        "원활하고 빠른 상담을 진행을 위해 정보 확인 부탁드립니다.\n"
        "정보 확인 후 상담접수 도와 드리겠습니다.\n\n"
        "이름 :\n"
        "연락처 :\n"
        "생년월일 :"
    )
    await update.message.reply_text(welcome_message)

# ✅ 일반 메시지 핸들러 (관리자 전달 및 접수 확인 응답)
async def forward_to_admins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    # 관리자가 보낸 메시지는 무시
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
            print(f"❌ 관리자 {admin_id}에게 메시지 전달 실패: {e}")

    # 사용자에게 접수 완료 메시지 전송
    await update.message.reply_text(
        "접수 되었습니다.\n정보 확인 후 신속하게 상담사 연결 도와 드리겠습니다.\n잠시만 기다려 주세요."
    )

# ✅ 메인 실행부
if __name__ == '__main__':
    TOKEN = "8135523315:AAHUv6TX6-KNxzMJERk8IyJ4P50YFQxaI9Y"  # ← 자신의 봇 토큰으로 바꾸세요

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.User(user_id=ADMINS)), forward_to_admins))

    print("🤖 봇이 실행 중입니다...")
    app.run_polling()





