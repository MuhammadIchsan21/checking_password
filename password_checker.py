# Common
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "passw0rd", "shadow", "123123", "654321",
    "superman", "qazwsx", "michael", "football", "password1"
]


def check_password_strength(password):
    score = 0
    feedback = []
    
    # CEK 1: Panjang
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Panjang cukup (8+ karakter)")
    else:
        feedback.append("❌ Terlalu pendek! Minimal 8 karakter")
    
    # CEK 2: Huruf besar
    has_uppercase = any(char.isupper() for char in password)
    if has_uppercase:
        score += 1
        feedback.append("✅ Ada huruf besar")
    else:
        feedback.append("❌ Perlu huruf besar (A-Z)")
    
    # CEK 3: Huruf kecil
    has_lowercase = any(char.islower() for char in password)
    if has_lowercase:
        score += 1
        feedback.append("✅ Ada huruf kecil")
    else:
        feedback.append("❌ Perlu huruf kecil (a-z)")
    
    # CEK 4: Ada angka
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        score += 1
        feedback.append("✅ Ada angka")
    else:
        feedback.append("❌ Perlu angka (0-9)")
    
    # CEK 5: Special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(char in special_chars for char in password)
    if has_special:
        score += 1
        feedback.append("✅ Ada special character")
    else:
        feedback.append("❌ Perlu special character (!@#$%)")
    
    if password.lower() in COMMON_PASSWORDS:
        score = 0  # Reset score ke 0!
        feedback.insert(0, "⚠️ BAHAYA! Password ini ada di common password list!")
        feedback.append("🚨 Ganti SEKARANG! Password ini sangat mudah ditebak!")
    
    return score, feedback
def run_tests():
    """Function untuk test semua scenario"""
    test_cases = [
        ("abc", 0, "Terlalu pendek"),
        ("password", 0, "Common password"),
        ("Password", 2, "No number & special char"),
        ("Password1", 4, "No special char"),
        ("Password1!", 5, "Perfect"),
        ("MyP@ssw0rd!2026", 5, "Very strong"),
    ]
    print("\n🧪 RUNNING TESTS...\n")
    for pwd, expected_min_score, description in test_cases:
        score, feedback = check_password_strength(pwd)
        status = "✅ PASS" if score >= expected_min_score else "❌ FAIL"
        print(f"{status} | {pwd:20} | Score: {score}/5 | {description}")

def get_strength_rating(score, max_score=5):
    """
    Convert score ke rating
    """
    percentage = (score / max_score) * 100
    
    if percentage == 100:
        return "🔒 VERY STRONG", "green"
    elif percentage >= 80:
        return "💪 STRONG", "blue"
    elif percentage >= 60:
        return "😐 MEDIUM", "yellow"
    elif percentage >= 40:
        return "😰 WEAK", "orange"
    else:
        return "💀 VERY WEAK", "red"

# Update main code
if __name__ == "__main__":
    run_tests() 
    # interactive mode
    print("\n" + "="*50)
    print("PASSWORD STRENGTH CHECKER")
    print("="*50)
    password = input("Masukkan password untuk di-cek: ")
    
    score, feedback = check_password_strength(password)
    rating, color = get_strength_rating(score)
    
    print("\n" + "="*50)
    print(f"PASSWORD: {password}")
    print(f"SCORE: {score}/5")
    print(f"RATING: {rating}")
    print("="*50)
    print("\nDETAIL FEEDBACK:")
    for f in feedback:
        print(f"  {f}")
    print("="*50)