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
    "tomate": "tomato",
    "queijo": "cheese",
    "servido": "served",
    "com": "with",
    "arroz": "rice",
    "batata": "potato",
    "fritas": "fries",
    "feijoada": "feijoada (Brazilian black-bean stew)"
    "feijão": "beans",
    "preto": "black",
    "carne": "meat",
    "seca":, "dried",
    "linguiça": "sausage",
    "costelinha": "pork ribs",
    "farofa": "toasted cassava flour(farofa)",
    "couve": "collard greens",
    "salada": "salad",
    "alface": "lettuce",
    "frango": "chicken",
    "grelhado": "grilled",
    "croutons": "croutons",
    "pão": "bread",
    "alho": "garlic",
    "assado": "roasted",
    "manteiga": "butter",
    "ervas": "herbs",
    "doce": "sweet",
    "chocolate": "chocolate",
    "granulado": "sprinkles",
    "brigadeiro": "brigadiro(chocolate truffle)",
}
def normalize_text(text: str) -> str:
    ***Limpeza/normalizaçao simples(abreviaçoes comuns),***
    if not isinstance(text, str):
        return s.strip()"""
        s = text
        repl = {
    " c/ ": " com ",
    " c/ ": "com",        
    " c/": "com",
    "p/ ": "para",
    " R$": "R$"    

        }

def traduzir_texto(texto: str,
glosario: dict) ->