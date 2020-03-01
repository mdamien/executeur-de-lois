from parsimonious.grammar import Grammar

grammar = Grammar("""
article = "Article " numero (~"\s*"s alinea)+ ~"\s*"s
numero = ~"\d+"
alinea = ~".+"
""")

import sys

file = sys.argv[1]

print(grammar.parse(open(file).read()))
