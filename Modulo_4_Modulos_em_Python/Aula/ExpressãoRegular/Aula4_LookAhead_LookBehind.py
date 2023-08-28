import re
from pprint import pprint

texto = """
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
"""

# Positive lookahead - Verifica se existe algo após a expressão regular checada
# , no caso o número dos ip
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))
print()

pprint(re.findall(r'.+', texto))
print()
pprint(re.findall(r'(?=.*[^in]active).+', texto))
print()

# Positive lookbehind - Verifica se existe algo antes da expressão regular
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# Negative lookbehind
pprint(re.findall(r'\w+(?<!ONLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

