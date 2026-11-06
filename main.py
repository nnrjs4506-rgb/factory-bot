import os
from bot_runner import run_bot

if __name__ == "__main__":
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("BOT_TOKEN not found!")
    else:
        run_bot(token)
