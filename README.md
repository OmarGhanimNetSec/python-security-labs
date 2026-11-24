\# Python Security Labs



Hands-on Python scripts covering input validation, IPv4 range classification, and function decorators for security logging\[cite: 1, 9, 10].



> \*\*Note:\*\* For educational and authorized local/lab use only.



\## Scripts Included



\* \*\*`ip\_validator.py`\*\* — Checks whether user input is a valid IP address using `ipaddress.ip\_address()` and catches invalid formats with `try/except ValueError`\[cite: 9].

\* \*\*`ip\_classifier.py`\*\* — Classifies IPv4 addresses into Private, Loopback, Link-local, Multicast, or Public ranges\[cite: 10].

\* \*\*`login\_decorator.py`\*\* — Uses a `@logger` decorator to log login attempts before running the `login()` check\[cite: 1].



\## How to Run



```bash

python3 ip\_validator.py

python3 ip\_classifier.py

python3 login\_decorator.py

