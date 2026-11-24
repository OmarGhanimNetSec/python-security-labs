SPECIAL_CHARS = set("!@#$%^&*(),.?\\\":{}|<>")


def score_password(passwd):
    has_number = False
    has_special = False
    has_upper = False
    has_lower = False
    score = 0

    for ch in passwd:
        if ch.isdigit():
            has_number = True
        elif ch in SPECIAL_CHARS:
            has_special = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True

    if has_upper and has_lower:
        score += 1
    if has_number:
        score += 1
    if has_special:
        score += 1
    if len(passwd) >= 8:
        score += 1
    if len(passwd) >= 12:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score


def main():
    input_file = "sample_passwords.txt"
    output_file = "password_report.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        passwords = f.read().splitlines()

    results = []
    for passwd in passwords:
        if not passwd:
            continue
        strength, score = score_password(passwd)
        results.append(f"{passwd} => {strength}({score} points)")

    with open(output_file, "w", encoding="utf-8") as out:
        for line in results:
            out.write(line + "\n")

    print(f"Password analysis complete! Results saved in '{output_file}'.")


if __name__ == "__main__":
    main()
