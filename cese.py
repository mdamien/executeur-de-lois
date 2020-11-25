import art69
from art22 import *
from art23 import inserer_article

art69.REPO = "../loi-francaise"

"""
Au troisième alinéa de l'article 1er de l'ordonnance n° 58-1360 du 29 décembre 1958 portant loi organique relative au Conseil économique, social et environnemental, le mot : "suggère" est remplacé par le mot : "recommande".
"""
art69.TEXTE = "ordonnance n° 58-1360"
remplacer_contenu(
    alinea=3,
    contenu_avant="suggère",
    contenu_apres="recommande",
    article="1")