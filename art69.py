import os

from fuzzywuzzy import fuzz, process


REPO = "../pjl-audiovisuel"


def _trouve_fichier_du_texte(texte):
    global REPO
    fichiers = [fichier.replace('_', ' ') for fichier in os.listdir(REPO)]
    fichier, score = process.extractOne(texte, fichiers, scorer=fuzz.token_sort_ratio)
    if score > 90:
        return os.path.join(REPO, fichier)

def _trouve_article(article, contenu_texte):
    for i, line in enumerate(contenu_texte):
        if article in line:
            return i


def inserer(texte, article, alinea, contenu):
    fichier = _trouve_fichier_du_texte(texte)
    print("Fichier du texte:", fichier)
    
    with open(fichier) as f:
        contenu_texte = f.read().split("\n")

    position_article = _trouve_article(article, contenu_texte)
    print("Article du texte:", contenu_texte[position_article])

    position_alinea = position_article + alinea*2
    print("Contenu alinea:", contenu_texte[position_alinea])
    
    nouveau_contenu_texte = contenu_texte[:position_alinea+1]
    for alinea_contenu in contenu:
        nouveau_contenu_texte.append("")
        nouveau_contenu_texte.append(alinea_contenu)
    nouveau_contenu_texte += contenu_texte[position_alinea+1:]

    with open(fichier, 'w') as f:
        f.write('\n'.join(nouveau_contenu_texte))


inserer(
    alinea=5,
    article="L163",
    texte="livre des procédures fiscales",
    contenu=["Pour s’assurer du respect, par les éditeurs de services, de leurs obligations de contribution au développement de la production d’œuvres cinématographiques et audiovisuelles prévues à l’article 71 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication, l’Autorité de régulation de la communication audiovisuelle et numérique peut recevoir de l’administration des impôts tous les renseignements relatifs au chiffre d’affaires de ces éditeurs."])
