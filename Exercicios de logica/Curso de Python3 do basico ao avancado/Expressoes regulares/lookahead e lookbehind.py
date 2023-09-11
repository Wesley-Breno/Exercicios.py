import re
from pprint import pprint

texto = """
ONLINE 192.167.9.3 GHIJK active
OFFNLINE 192.161.3.4 GHIJK inactive
OFFNLINE 192.267.9.7 GHIJK active
ONLINE 192.367.9.2 GHIJK active
ONLINE 192.147.9.5 GHIJK inactive
OFFNLINE 192.167.9.2 GHIJK active
"""

# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))  # Pegando apenas os IPs que sao 'active'

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))  # Pegando apenas os IPs que sao 'inactive'

print()

# Positive lookbehind
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+', texto))  # Pegando apenas os IPs que sao 'ONLINE'

# Negative lookbehind
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+', texto))  # Pegando apenas os IPs que sao 'OFFLINE'
