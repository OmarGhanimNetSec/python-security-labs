def logger(func):
    def wrapper(ip_address):
        print(f"[LOG] Login attempt from IP: {ip_address}")
        return func(ip_address)
    return wrapper


@logger
def login(ip_address):
    allowed_ip = "192.168.1.1"
    if ip_address == allowed_ip:
        print("Login Successful")
    else:
        print("Login Failed")


if __name__ == "__main__":
    login("192.168.1.1")
    login("10.0.0.5")