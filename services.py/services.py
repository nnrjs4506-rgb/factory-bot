import requests

def generate_image(prompt):
    # نستخدم Pollinations مجاني بدون مفتاح
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    return url

def generate_text(prompt):
    # مؤقتاً نرجع نفس النص، بعدين نربطه بـ AI
    return f"تم استلام: {prompt}"
