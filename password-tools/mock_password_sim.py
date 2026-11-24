from mock_user import users


def main():
    sample_candidates = [
        "password123",
        "letmein",
        "123456",
        "samplepass",
        "admin",
        "demo_pass",
    ]

    passwords = []
    seen = set()
    for item in sample_candidates:
        pwd = item.strip()
        if pwd and pwd not in seen:
            passwords.append(pwd)
            seen.add(pwd)

    username = input("Enter test username: ").strip()
    expected_list = users.get(username)

    if expected_list is None:
        print(f"Username '{username}' not found in mock dataset.")
        return

    for idx, password in enumerate(passwords):
        print(f"[{idx}] Trying test password: {password}")
        if password in expected_list:
            print(f"Match found: {password}")
            print(f"Total attempts: {idx + 1}")
            break
        print("Attempt failed.")


if __name__ == "__main__":
    main()