import ipaddress


def main():
    ip = input("Enter an IP address: ").strip()
    try:
        ipaddress.ip_address(ip)
        print("Valid IP address!")
    except ValueError:
        print("Error: Invalid IP address format!")


if __name__ == "__main__":
    main()