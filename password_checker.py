    # password_checker.py
    # Project: Password Strength Checker
    # Day 1 - Cybersecurity Learning

def check_password_strength(password):
        """
        Function untuk cek kekuatan password
        Input: password (string)
        Output: score dan feedback
        """
        score = 0 
        feedback = []

        #Kita akan tes logic disini

        # return score, feedback

    # ===== CEK 1: PANJANG PASSWORD =====
    # len() function menghitung jumlah karakter
        if len(password) >= 8:
            score += 1
            feedback.append("✅ Panjang cukup (8+ karakter)")
        else:
            feedback.append("❌ Terlalu pendek! Minimal 8 karakter")

        # ===== CEK 2: ADA HURUF BESAR =====
        has_uppercase = False  # inisialisasi dulu

        # ===== CEK HURUF BESAR =====
        for char in password:
            if char.isupper():
                has_uppercase = True
                break

        if has_uppercase:
            score += 1
            feedback.append("✅ Ada huruf besar")
        else:
            feedback.append("❌ Perlu huruf besar (A-Z)")

    # # ===== CEK 3: HURUF KECIL =====
    #     if any(c.islower() for c in password):
    #         score += 1
    #         feedback.append("✅ Mengandung huruf kecil")
    #     else:
    #         feedback.append("❌ Tambahkan huruf kecil")

    # # ===== CEK 4: ANGKA =====
    #     if any(c.isdigit() for c in password):
    #         score += 1
    #         feedback.append("✅ Mengandung angka")
    #     else:
    #         feedback.append("❌ Tambahkan angka")

    # # ===== CEK 5: SIMBOL =====
    #     if any(c in "!@#$%^&*()" for c in password):
    #         score += 1
    #         feedback.append("✅ Mengandung simbol")
    #     else:
    #         feedback.append("❌ Tambahkan simbol (!@#$%^&*)")

        return score, feedback

    # Test dengan berbagai password
test_passwords = ["password", "Password", "PASSWORD123"]
for pwd in test_passwords:
        score, feedback = check_password_strength(pwd)
        print(f"\nPassword: {pwd}")
        print(f"Score: {score}/1")
        for f in feedback:
            print(f)
        
