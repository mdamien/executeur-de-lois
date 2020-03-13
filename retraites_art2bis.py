import art69
from art22 import *
from art23 import inserer_article

art69.REPO = "../pjl-retraites"

"""
Le titre V du livre VI du code de la sécurité sociale est ainsi modifié :
"""
art69.TEXTE = "code de la sécurité sociale"
"""
1° L’article L. 652‑6 est ainsi modifié :

a) À la première phrase du premier alinéa, les mots : « au financement du régime d’assurance vieillesse de base de » sont remplacés par le mot : « à » ;
"""
remplacer_contenu(
    alinea=1,
    contenu_avant=pre_traite_contenu("au financement du régime d’assurance vieillesse de base de"),
    contenu_apres="à",
    article="L. 652‑6")
"""
b) Après la même première phrase, est insérée une phrase ainsi rédigée : « Le montant des droits de plaidoirie est fixé à 13 euros. » ;

c) Le deuxième alinéa est complété par les mots : « dont le taux est fixé par décret, sur proposition du conseil d’administration de la Caisse nationale des barreaux français » ;

d) Après le mot : « couvrent », la fin du dernier alinéa est ainsi rédigée : « les dépenses résultant de l’article L. 653‑8‑1. » ;

2° La section 5 du chapitre III est complétée par un article L. 653‑8‑1 ainsi rédigé :
"""
contenu = """« Art. L. 653‑8‑1. – La Caisse nationale des barreaux français participe au financement :

« 1° De la cotisation mentionnée à l’article L. 611‑2 due par les assurés mentionnés à l’article L. 651‑1 relevant du II de l’article L. 190‑1 ;

« 2° De la cotisation mentionnée à l’article L. 241‑3 due par les assurés mentionnés au 19° de l’article L. 311‑3 relevant du II de l’article L. 190‑1 ;

« 3° Des cotisations mentionnées aux articles L. 652‑7 et L. 654‑2 dues par les assurés mentionnés à l’article L. 651‑1 ne relevant pas du II de l’article L. 190‑1.

« Cette participation au financement s’applique dans la limite des cotisations d’assurance vieillesse dues sur la part du revenu d’activité inférieure à trois fois le plafond mentionné au 1° de l’article L. 241‑3.

« Le conseil d’administration de la Caisse nationale des barreaux français fixe chaque année la part des cotisations mentionnées aux 1° à 3° du présent article prise en charge par la caisse, ainsi que la limite de cette prise en charge.	

« La Caisse nationale des barreaux français verse avant le 31 mars au Fonds de solidarité vieillesse universel le produit des recettes mentionnées aux premier et deuxième alinéas de l’article L. 652‑6 qui excède le montant des prises en charge réalisées en application du présent article au titre de l’exercice précédent. »
"""
inserer_article(
    article="L653‑8‑1",
    contenu=pre_traite_contenu(contenu))