from art69 import *


def remplacer(texte, article, alinea_debut, alinea_fin, contenu):
    print("Remplacement")
    fichier = trouve_fichier_du_texte(texte)
    print("Fichier du texte:", fichier)
    
    with open(fichier) as f:
        contenu_texte = f.read().split("\n")

    position_article = trouve_article(article, contenu_texte)
    print("Article du texte:", contenu_texte[position_article][:20])

    position_debut = position_article + alinea_debut*2
    print("Alinea du début:", contenu_texte[position_debut][:20])
    position_fin = position_article + alinea_fin*2
    print("Alinea de fin:", contenu_texte[position_fin][:20])
    nouveau_contenu_texte = contenu_texte[:position_debut]
    nouveau_contenu_texte += contenu_texte[position_fin + 2:]

    with open(fichier, 'w') as f:
        f.write('\n'.join(nouveau_contenu_texte))

    inserer(
        texte=texte,
        article=article,
        alinea=alinea_debut,
        contenu=contenu
    )


if __name__ == "__main__":
    contenu = """
« I bis. – Au terme d’une durée de 12 mois à compter de la diffusion de programmes de télévision en ultra haute définition par voie hertzienne terrestre auprès d’au moins 30 % de la population française, les téléviseurs de plus de 110 centimètres de diagonale d’écran mis sur le marché à compter de cette date à des fins de vente ou de location au sens de l’article L. 43 du code des postes et des communications électroniques et destinés aux particuliers permettant la réception de services de télévision numérique terrestre, doivent permettre la réception de l’ensemble des programmes gratuits de télévision numérique terrestre en ultra haute définition.

« Au terme d’une durée de 18 mois à compter de la diffusion de programmes de télévision en ultra haute définition par voie hertzienne terrestre auprès d’au moins 30 % de la population française, les téléviseurs et les adaptateurs individuels mis sur le marché à compter de cette date à des fins de vente ou de location au sens de l’article L. 43 du code des postes et des communications électroniques et destinés aux particuliers permettant la réception de services de télévision numérique terrestre, doivent permettre la réception de l’ensemble des programmes gratuits de télévision numérique terrestre en ultra haute définition.

« Lorsque la diffusion de programmes de télévision en ultra haute définition par voie hertzienne terrestre atteint un niveau de couverture correspondant à 30 % de la population française, l’Autorité de régulation de la communication audiovisuelle et numérique rend publique cette information. » ;
    """

    contenu = contenu.replace('« ', '') \
        .replace('» ;', '') \
        .replace('»', '') \
        .strip()

    inserer(
        alinea=6,
        article="19",
        texte="loi du 5 mars 2007 relative à la modernisation de la diffusion audiovisuelle et à la télévision du futur",
        contenu=contenu)


    contenu = """
« Seuls les terminaux permettant la réception des services en ultra haute définition, selon les caractéristiques techniques précisées par application de l’article 12 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication, peuvent se voir accorder le label “Prêt pour la TNT en ultra haute définition”. » ;
    """

    contenu = contenu.replace('« ', '') \
        .replace('» ;', '') \
        .replace('»', '') \
        .strip()

    inserer(
        alinea=6,
        article="19",
        texte="loi du 5 mars 2007 relative à la modernisation de la diffusion audiovisuelle et à la télévision du futur",
        contenu=contenu)


    # 3° Les treizième à seizième alinéas sont remplacés par trois alinéas ainsi rédigés :



    contenu = """
« Les terminaux de réception de services de radio de première monte équipant les véhicules automobiles neufs à moteur conçus et construits pour le transport de personnes et ayant au moins quatre roues et mis sur le marché à compter du 21 décembre 2020 à des fins de vente ou de location au sens de l’article L. 43 du code des postes et des communications électroniques, permettent la réception de services de radio par voie hertzienne terrestre en mode numérique autorisés par application de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication.

« Cette obligation s’applique également aux autres terminaux neufs mis sur le marché à des fins de vente à compter de cette même date et disposant d’un écran d’affichage alphanumérique, pour lesquels la fonction de réception de services de radio diffusés par voie hertzienne terrestre n’est pas purement accessoire.

« Dans les collectivités d’outre‑mer, l’obligation mentionnée à l’alinéa précédent prend toutefois effet dans chaque collectivité ultramarine six mois après le début de la diffusion de services de radio par voie hertzienne terrestre en mode numérique sur son territoire en application des articles 26 et 29‑1 de la loi du 30 septembre 1986 précitée. »
    """

    contenu = contenu.replace('« ', '') \
        .replace('» ;', '') \
        .replace('»', '') \
        .strip()

    remplacer(
        alinea_debut=13,
        alinea_fin=16,
        article="19",
        texte="loi du 5 mars 2007 relative à la modernisation de la diffusion audiovisuelle et à la télévision du futur",
        contenu=contenu)











