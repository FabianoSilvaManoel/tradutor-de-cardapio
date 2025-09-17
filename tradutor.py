menu-translator/
data/
menu.csv
translator.py
cli.py
webapp.py
glossary.py
requiments.txt

data/menu.csv

item, descricao, preco
"Bife a Parmegiana", "Bife empanado coberto com molho de tomate e queijo, servido com arroz e batatas fritas", "R$ 28,00"
"Feijoada", "Feijão preto com carne seca e linguiça e costelinha, acomapanha farofa de couve", "R$ 35,00"
"Salada caesar", "Alface, frango grelhado, croutons e molho caesar", "R$ 22,00"

import re
import pandas as pd
from pathlib import path

_TOKEN_RE = re.compile(r"[\wÀa-ÖØ-öØ-ÿ] + | [^\w\s]", re.UNICODE)

GLOSARIO = {
    "bife": "steak",
    "parmegiana": "parmigiana",
    "bife à parmegiana": "parmigiana steak",
    "empanado": "breaded",
    "coberto": "covered",
    "molho": "sauce",
    "molho caesar": "caesar dressing",
    "tomate": "tomato"
    "queijo": "cheese"






}