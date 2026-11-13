import random

def guess_number():
    # سیستم یک عدد تصادفی بین 1 تا 100 انتخاب می‌کند
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    
    print("=" * 40)
    print("🎮 بازی حدس عدد شروع شد!")
    print("یک عدد بین 1 تا 100 در نظر گرفته شده.")
    print("شما فقط 10 بار فرصت دارید آن را حدس بزنید.")
    print("=" * 40)
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\n🔢 تلاش {attempts} از {max_attempts}")
        
        try:
            guess = int(input("حدس خود را وارد کنید: "))
        except ValueError:
            print("❌ لطفاً یک عدد صحیح وارد کنید!")
            attempts -= 1  # ورودی نامعتبر حساب نمی‌شود
            continue
        
        if guess < 1 or guess > 100:
            print("⚠️ عدد باید بین 1 و 100 باشد!")
            attempts -= 1
            continue
        
        if guess == secret_number:
            print(f"\n🎉 تبریک! شما برنده شدید!")
            print(f"عدد مخفی {secret_number} بود.")
            print(f"شما در تلاش {attempts} آن را حدس زدید.")
            return
        
        elif guess < secret_number:
            print("⬆️ عدد شما کوچک‌تر از عدد مخفی است.")
        else:
            print("⬇️ عدد شما بزرگ‌تر از عدد مخفی است.")
    
    # اگر کاربر بعد از 10 تلاش موفق نشد
    print("\n" + "=" * 40)
    print("😢 متأسفانه باختید!")
    print(f"شما به 10 تلاش مجاز رسیدید.")
    print(f"عدد مخفی {secret_number} بود.")
    print("=" * 40)


if __name__ == "__main__":
    guess_number()