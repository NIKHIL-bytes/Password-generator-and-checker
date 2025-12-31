import sys
import random
import string
import re

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1

    return score

def get_label(score):
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    return "Strong"

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    return "".join(random.choice(chars) for _ in range(length))

def usage():
    print("Usage:")
    print("Check password strength:")
    print("  python password_tool.py check <password>")
    print("")
    print("Generate strong password:")
    print("  python password_tool.py generate <length>")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == "check":
        password = sys.argv[2]
        score = check_strength(password)
        label = get_label(score)
        print(f"Password Strength: {label}")

    elif command == "generate":
        try:
            length = int(sys.argv[2])
            if length < 6:
                print("Length should be at least 6")
                sys.exit(1)
            pwd = generate_password(length)
            print("Generated Password:")
            print(pwd)
        except ValueError:
            print("Invalid length")

    else:
        usage()
