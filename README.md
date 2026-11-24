# Python Security Labs

Organized Python security scripts and labs covering network address checks, login logging decorators, and password/authentication exercises.

> **Note:** For educational and authorized local/lab use only.

## Repository Structure

### `ip-and-network/`
- `ip_validator.py` — Checks whether user input is a valid IP address using `ipaddress.ip_address()` and catches invalid formats with `try/except ValueError`.
- `ip_classifier.py` — Classifies IPv4 addresses into Private, Loopback, Link-local, Multicast, or Public ranges.

### `auth-and-logging/`
- `login_decorator.py` — Uses a `@logger` decorator to log login attempts before running the `login()` check.

### `password-tools/`
- `batch_password_scorer.py` — Reads passwords from `sample_passwords.txt` and scores strength based on length, character variety, and special characters.
- `sample_passwords.txt` — Sample test password list for `batch_password_scorer.py`.
- `mock_user.py` & `mock_password_sim.py` — Local mock credential-testing simulation with deduplication and attempt counting.
- `brute_counter_lab.py` — Local `127.0.0.1:6000` lab script that counts attempts and stops on a match.

## How to Run

python3 ip-and-network/ip_validator.py
python3 ip-and-network/ip_classifier.py
python3 auth-and-logging/login_decorator.py
python3 password-tools/batch_password_scorer.py
python3 password-tools/mock_password_sim.py