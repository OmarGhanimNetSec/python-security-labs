import ipaddress


def classify_ip(ip_str):
    ip = ipaddress.IPv4Address(ip_str.strip())

    if (
        ip in ipaddress.IPv4Network("10.0.0.0/8")
        or ip in ipaddress.IPv4Network("172.16.0.0/12")
        or ip in ipaddress.IPv4Network("192.168.0.0/16")
    ):
        print(f"{ip} = Private IP")
    elif ip in ipaddress.IPv4Network("127.0.0.0/8"):
        print(f"{ip} = Loopback IP")
    elif ip in ipaddress.IPv4Network("169.254.0.0/16"):
        print(f"{ip} = Link-local IP")
    elif ip in ipaddress.IPv4Network("224.0.0.0/4"):
        print(f"{ip} = Multicast IP")
    else:
        print(f"{ip} = Public IP")


def main():
    ip_input = input("Enter an IPv4 address: ")
    try:
        classify_ip(ip_input)
    except ValueError:
        print("Invalid IP format. Please enter a valid IPv4 address (example: 192.168.0.1).")


if __name__ == "__main__":
    main()