from art15 import *


def normalise_numero_article(article):
    article = article.replace('‑', '-')
    return '-'.join([n.rjust(3, '0') for n in article[1:].split('-')])


def trouve_le_point_d_insertion_pour_article(article_a_inserer, contenu_texte):
    article_a_inserer = normalise_numero_article(article_a_inserer)
    print("A inserer:", article_a_inserer)
    dernier_point_insertion = None
    for i, ligne in enumerate(contenu_texte):
        if not ligne:
            continue
        if ligne.startswith("#"):
            if "# Article " in ligne:
                article = ligne.split("Article ")[-1]
                article = normalise_numero_article(article)
                print("Article X:", article)
                if article > article_a_inserer:
                    print("Point limite:", ligne)
                    print("Insertion aprés:", contenu_texte[dernier_point_insertion][:20])
                    return dernier_point_insertion + 1
        else:
            dernier_point_insertion = i


def inserer_article(article, contenu, texte=None):
    print("Insertion")
    fichier = trouve_fichier_du_texte(texte)
    print("Fichier du texte:", fichier)
    
    with open(fichier) as f:
        contenu_texte = f.read().split("\n")

    position_insertion = trouve_le_point_d_insertion_pour_article(article, contenu_texte)
    
    nouveau_contenu_texte = contenu_texte[:position_insertion]
    nouveau_contenu_texte.append("")
    nouveau_contenu_texte.append(contenu)
    nouveau_contenu_texte += contenu_texte[position_insertion:]

    with open(fichier, 'w') as f:
        f.write('\n'.join(nouveau_contenu_texte))


# Au chapitre III du titre III du livre III du code du sport, il est inséré une section 3 ainsi rédigée :

contenu = """
« Section 3
« Lutte contre la retransmission illicite des manifestations et compétitions sportives

« Art. L. 333‑10. – I. – Lorsqu’ont été constatées des atteintes graves et répétées au droit d’exploitation audiovisuelle prévu à l’article L.333‑1, au droit voisin d’une entreprise de communication audiovisuelle prévu à l’article L. 216‑1 du code de la propriété intellectuelle, dès lors que le programme concerné est constitué d’une manifestation ou d’une compétition sportive, ou à un droit acquis à titre exclusif par contrat ou accord d’exploitation audiovisuelle d’une compétition ou manifestation sportive, occasionnées par le contenu d’un service de communication au public en ligne dont l’objectif principal ou l’un des objectifs principaux est la diffusion sans autorisation de compétitions ou manifestations sportives, et afin de prévenir ou de remédier à un nouvelle atteinte grave et irrémédiable à ces mêmes droits, le titulaire de ce droit peut saisir le président du tribunal judiciaire, statuant selon la procédure accélérée au fond ou en référé, aux fins d’obtenir toutes mesures proportionnées propres à prévenir ou à faire cesser cette atteinte, à l’encontre de toute personne susceptible de contribuer à y remédier.

« Peuvent également à ce titre saisir le président du tribunal judiciaire dans les conditions prévues au premier alinéa :

« 1° La ligue professionnelle, dans le cas où elle est concessionnaire de la commercialisation des droits d’exploitation audiovisuelle de compétitions sportives professionnelles, susceptible de faire l’objet, ou faisant l’objet, de l’atteinte mentionnée au premier alinéa ;

« 2° L’entreprise de communication audiovisuelle, dans le cas où elle a acquis un droit à titre exclusif, par contrat ou accord d’exploitation audiovisuelle d’une compétition ou manifestation sportive, que cette compétition ou manifestation sportive soit organisée sur le territoire français ou à l’étranger, susceptible de faire l’objet, ou faisant l’objet, de l’atteinte mentionnée au premier alinéa.

« II. –  président du tribunal judiciaire peut notamment ordonner, au besoin sous astreinte, la mise en œuvre, pour chacune des journées figurant au calendrier officiel de la compétition ou de la manifestation sportive dans la limite d’une durée de deux mois, de toutes mesures proportionnées, telles que des mesures de blocage ou de déréférencement, propres à empêcher l’accès à partir du territoire français, à tout service de communication au public en ligne diffusant illicitement la compétition ou manifestation sportive, ou dont l’objectif principal ou l’un des objectifs principaux est la diffusion sans autorisation de compétitions ou manifestations sportives.

« Si, durant le délai fixé par le président du tribunal judiciaire pour la mise en œuvre de ces mesures, de nouvelles atteintes graves et répétées aux droits mentionnés au premier alinéa du I sont constatées sur les services de communication au public en ligne identifiés dans des décisions rendues sur le fondement de l’alinéa premier du II ou sur des services de communication au public en ligne qui n’ont pas été encore identifiés dans une décision, le président du tribunal judiciaire peut être saisi huit jours avant l’expiration de ce délai pour ordonner, au besoin sous astreinte, pour chacune des journées figurant au calendrier officiel de la compétition ou manifestation sportive et pendant toute la durée de celle‑ci, et dans la limite de neuf mois, le blocage ou le déréférencement des services de communication en ligne dont l’objectif principal ou l’un des objectifs principaux serait la diffusion sans autorisation de compétitions ou manifestations sportives ou qui donnent accès illicitement à la compétition ou manifestation sportive.

« Le président du tribunal judiciaire peut ordonner toute mesure de publicité de la décision notamment son affichage ou sa publication intégrale ou par extraits dans les journaux ou sur les services de communication au public en ligne qu’il désigne, selon les modalités qu’il précise.

« III. – Pendant toute la durée de la compétition ou de la manifestation sportive, pour la mise en œuvre des mesures ordonnées sur le fondement du deuxième alinéa du II, le demandeur communique au défendeur, les données d’identification nécessaires.

« IV. – L’autorité adopte des modèles d’accord type qu’elle invite les titulaires de droits mentionnés au I, la ligue professionnelle, l’entreprise de communication audiovisuelle ayant acquis un droit à titre exclusif et les personnes mentionnées au 1 du I de l’article 6 de la loi n° 2004‑575 du 21 juin 2004 à conclure. L’accord conclu entre les parties détermine leurs conditions d’information réciproque sur d’éventuelles violations de l’exclusivité du droit d’exploitation audiovisuelle de la manifestation ou de la compétition sportive en application du III du présent article, les mesures qu’elles s’engagent à prendre pour les faire cesser et la répartition du coût de celles‑ci. »
"""
contenu = contenu.replace('« ', '') \
    .replace('» ;', '') \
    .replace('»', '') \
    .strip()

contenu = contenu.split('\n')
nouveau_contenu = []
i = 0
while i < len(contenu):
    ligne = contenu[i]
    if ligne.startswith("Section"):
        nouveau_contenu.append("#### %s : %s" % (ligne, contenu[i+1]))
        i += 1
    elif ligne.startswith("Art. L."):
        ligne = ligne.replace("Art. L. ", "##### Article L")
        art, art_contenu = ligne.split(".", maxsplit=1)
        nouveau_contenu.append(art)
        nouveau_contenu.append('')
        nouveau_contenu.append(art_contenu)
    else:
        nouveau_contenu.append(ligne)
    i += 1
contenu = '\n'.join(nouveau_contenu)

inserer_article(
    texte="code du sport",
    contenu=contenu,
    article="L333‑10"
)

