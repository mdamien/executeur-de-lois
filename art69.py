import os

from fuzzywuzzy import fuzz, process


REPO = "../pjl-audiovisuel"
TEXTE = None


def trouve_fichier_du_texte(texte=None):
    global REPO, TEXTE
    texte = texte or TEXTE
    fichiers = os.listdir(REPO)
    fichiers_clean = [fichier.replace('_', ' ') for fichier in fichiers]
    fichier_clean, score = process.extractOne(texte, fichiers_clean, scorer=fuzz.token_sort_ratio)
    fichier = fichiers[fichiers_clean.index(fichier_clean)]
    if score > 50:
        return os.path.join(REPO, fichier)
    raise Exception("Texte introuvable: " + texte)


def trouve_article(article, contenu_texte):
    article = article.replace('‑', '-')
    article = article.replace('L. ', 'L')
    for i, line in enumerate(contenu_texte):
        if 'Article %s' % article in line:
            return i
    raise Exception("Article introuvable: " + article)


def inserer(article, contenu, alinea=None, texte=None):
    print("Insertion")
    fichier = trouve_fichier_du_texte(texte)
    print("Fichier du texte:", fichier)
    
    with open(fichier) as f:
        contenu_texte = f.read().split("\n")

    position_article = trouve_article(article, contenu_texte)
    print("Article du texte:", contenu_texte[position_article][:30])

    if alinea is None:
        position_alinea = position_article + 1
        while True:
            ligne = contenu_texte[position_alinea]
            if ligne.startswith("#"):
                break
            position_alinea += 1
        position_alinea -= 2
    else:
        position_alinea = position_article + alinea*2

    print("Contenu alinea:", contenu_texte[position_alinea][:30])
    
    nouveau_contenu_texte = contenu_texte[:position_alinea+1]
    nouveau_contenu_texte.append("")
    nouveau_contenu_texte.append(contenu)
    nouveau_contenu_texte += contenu_texte[position_alinea+1:]

    with open(fichier, 'w') as f:
        f.write('\n'.join(nouveau_contenu_texte))


if __name__ == "__main__":
    inserer(
        alinea=5,
        article="L163",
        texte="livre des procédures fiscales",
        contenu="Pour s’assurer du respect, par les éditeurs de services, de leurs obligations de contribution au développement de la production d’œuvres cinématographiques et audiovisuelles prévues à l’article 71 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication, l’Autorité de régulation de la communication audiovisuelle et numérique peut recevoir de l’administration des impôts tous les renseignements relatifs au chiffre d’affaires de ces éditeurs.")
