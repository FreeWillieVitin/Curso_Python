import re
from pprint import pprint

valida_senha_forte = re.compile(
    r"^"
    r"(?=.*[a-z])"
    r"(?=.*[A-Z])"
    r"(?=.*[0-9])"
    r"(?=.*[ -\/:-@[-`{-~]).{12,}$",
    flags=re.M
    )

senhas = """
VÁLIDAS
8Z6I2d:}V(hp
~{Q1I9~mPt2k
RS26h2Fe;~l/
aF2:no>A9Z2>
0PpRh3e<N3-=
VictorHugo1*

SEM MINÚSCULAS
XC^R/`M8+413
O}64=H8-?FB5
?2`4QHX\X}23
|7K[D=+O4E89
P>3/>88{CO9K

SEM MINÚSCULAS E NÚMEROS
,DY$U]R<B$@Y
ROP](`[_NQY"
@XO>NM-LQ_=}
AOIWJ?|"}L>;
[-}CKJZF`?A_

SEM NÚMEROS CARACTERES E MINÚSCULAS
LQFVRBYFWVJN
KYGFAVFSAQOY
APGFLXKPKFUN
OHLJQCYCFFPA
YYPONJQJJZUK

QUANTIDADE INVÁLIDA (6)
q27tN]
s9<Hh1
to[A74
4nJ2/t
Bf99h^
"""

pprint(valida_senha_forte.findall(senhas))