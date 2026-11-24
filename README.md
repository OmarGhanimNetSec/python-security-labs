# Python Security Labs

Hands-on Python scripts covering input validation, IPv4 range classification, and function decorators for security logging.

> **Note:** For educational and authorized local/lab use only.

## Scripts Included

- `ip_validator.py` — Checks whether user input is a valid IP address using `ipaddress.ip_address()` and catches invalid formats with `try/except ValueError`.
- `ip_classifier.py` — Classifies IPv4 addresses into Private, Loopback, Link-local, Multicast, or Public ranges.
- `login_decorator.py` — Uses a `@logger` decorator to log login attempts before running the `login()` check.

## How to Run

python3 ip_validator.py
python3 ip_classifier.py
python3 login_decorator.py