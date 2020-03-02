"""
L’article 43‑1 de la même loi est ainsi modifié :

1° Après le deuxième alinéa, il est inséré un troisième alinéa ainsi rédigé :

« 1° bis Ses coordonnées, y compris l’adresse du courrier électronique ou le site internet ; »

2° Il est ajouté un alinéa ainsi rédigé :

« 5° L’information selon laquelle son service est soumis à la présente loi et au contrôle de l’Autorité de régulation de la communication audiovisuelle et numérique. »
"""

from art69 import inserer

contenu = """
« 1° bis Ses coordonnées, y compris l’adresse du courrier électronique ou le site internet ; »
"""

contenu = contenu.replace('« ', '') \
    .replace('» ;', '') \
    .replace('»', '') \
    .strip()

inserer(
    alinea=2,
    article="43-1",
    texte="Loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication",
    contenu=contenu)


contenu = """
« 5° L’information selon laquelle son service est soumis à la présente loi et au contrôle de l’Autorité de régulation de la communication audiovisuelle et numérique. »
"""

contenu = contenu.replace('« ', '') \
    .replace('» ;', '') \
    .replace('»', '') \
    .strip()

inserer(
    article="43-1",
    texte="Loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication",
    contenu=contenu)
