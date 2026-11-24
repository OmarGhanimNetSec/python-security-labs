import requests


def main():
    # Authorized local loopback test target only
    url = "http://127.0.0.1:6000/login"
    candidates = ["1111", "0000", "1234"]
    attempts = 0

    for pwd in candidates:
        attempts += 1
        response = requests.post(
            url,
            data={"username": "admin", "password": pwd},
            timeout=5,
        )
        if "Welcome" in response.text:
            print(f"Trying {pwd} -> SUCCESS")
            print(f"Password found after {attempts} attempts.")
            break
        print(f"Trying {pwd} -> fail")


if __name__ == "__main__":
    main()