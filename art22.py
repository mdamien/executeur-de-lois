from art69 import *


def remplacer_contenu(texte, article, alinea=None, contenu_avant, contenu_apres):
    print("Remplacement")
    fichier = trouve_fichier_du_texte(texte)
    print("Fichier du texte:", fichier)
    
    with open(fichier) as f:
        contenu_texte = f.read().split("\n")

    position_article = trouve_article(article, contenu_texte)
    print("Article du texte:", contenu_texte[position_article][:20])

    position_alinea = position_article + alinea*2
    print("Alinea:", contenu_texte[position_alinea][:20])

    contenu_texte[position_alinea] = contenu_texte[position_alinea] \
        .replace(contenu_avant, contenu_apres)

    with open(fichier, 'w') as f:
        f.write('\n'.join(contenu_texte))


"""
Le code de la propriété intellectuelle est ainsi modifié :

I. – Au quatrième alinéa de l’article L. 331‑5, la référence : « L. 331‑31 » est remplacée par la référence : « L. 331‑28 » et la référence : « L. 331‑32 » est remplacée par la référence : « L. 331‑29 ».
"""

remplacer_contenu(
    alinea=4,
    contenu_avant="L. 331-31",
    contenu_apres="L. 331-28",
    article="L331‑5",
    texte="code de la propriété intellectuelle")

remplacer_contenu(
    alinea=4,
    contenu_avant="L. 331-32",
    contenu_apres="L. 331-29",
    article="L331‑5",
    texte="code de la propriété intellectuelle")


"""
II. – À l’article L. 331‑6, la référence : « L. 331‑31 » est remplacée par la référence : « L. 331‑28 » et les références : « L. 331‑33 à L. 331‑35 et L. 331‑37 » sont remplacés par les références : « L. 331‑30 à L. 331‑32 et L. 331‑34 ».
"""
"""
remplacer_contenu(
    contenu_avant="L. 331-31",
    contenu_apres="L. 331-28",
    article="L331‑6",
    texte="code de la propriété intellectuelle")

remplacer_contenu(
    contenu_avant="L. 331-33 à L. 331-35 et L. 331-37",
    contenu_apres="L. 331-30 à L. 331-32 et L. 331-34",
    article="L331-6",
    texte="code de la propriété intellectuelle")
"""
"""
III. –À l’article L. 331‑7, la référence : « L. 331‑31 » est remplacée par la référence : « L. 331‑28 ».

IV. – L’intitulé de la section 3 du chapitre Ier du titre III du livre III du même code est ainsi rédigé : « Autorité de régulation de la communication audiovisuelle et numérique ».

V. – L’intitulé de la sous‑section 1 du chapitre Ier du titre III du livre III du même code est ainsi rédigé : « Compétences et organisation en matière de protection du droit d’auteur et des droits voisins ».

VI. – L’article L. 331‑12 est abrogé.

VII. – L’article L. 331‑13 est remplacé par les dispositions suivantes :

« L’Autorité de régulation de la communication audiovisuelle et numérique assure :

« 1° Une mission d’encouragement au développement de l’offre légale et d’observation de l’utilisation licite et illicite des œuvres et des objets auxquels est attaché un droit d’auteur ou un droit voisin et des droits d’exploitation audiovisuelle prévus à l’article L. 333‑1 du code du sport sur les réseaux de communications électroniques utilisés pour la fourniture de services de communication au public en ligne ;

« 2° Une mission de protection de ces œuvres et objets à l’égard des atteintes à ces droits commises sur les réseaux de communications électroniques utilisés pour la fourniture de services de communication au public en ligne ;

« 3° Une mission de régulation et de veille dans le domaine des mesures techniques de protection et d’identification des œuvres et des objets protégés par un droit d’auteur ou par un droit voisin.

« Au titre de ces missions, l’Autorité prend toute mesure, notamment par l’adoption de recommandations, de bonnes pratiques, de modèles et clauses types, et de codes de conduite visant à favoriser, d’une part, l’information du public sur l’existence des moyens de sécurisation mentionnés à l’article L. 331‑19 et, d’autre part, la signature d’accords volontaires susceptibles de contribuer à remédier aux atteintes au droit d’auteur et aux droits voisins ou aux droits d’exploitation audiovisuelle prévus à l’article L. 333‑1 du code du sport sur les réseaux de communications électroniques utilisés pour la fourniture de services de communication au public en ligne. »

VIII. – L’article L. 331‑14 est remplacé par les dispositions suivantes :

« Art. L. 331‑14. – Le membre mentionné à l’avant‑dernier alinéa du I de l’article 4 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication est chargé d’exercer la mission mentionnée aux articles L. 331‑18 à L. 331‑23. »

IX. – Les articles L. 331‑15 à L. 331‑20 sont abrogés.

X. – L’article L. 331‑21 est ainsi modifié :

1° À la première phrase du premier alinéa, les mots : « , par la commission de protection des droits, de ses attributions, la Haute Autorité dispose d’agents publics assermentés habilités par le président de la Haute Autorité » sont remplacés par les mots : « des missions mentionnées à l’article L. 331‑12, l’Autorité de régulation de la communication audiovisuelle et numérique dispose d’agents publics assermentés et habilités par son président » ;

2° Au deuxième alinéa, les mots : « Les membres de la commission de protection des droits et les agents mentionnés au premier alinéa reçoivent les saisines adressées à ladite commission » sont remplacés par les mots : « I. – Pour l’exercice de la mission mentionnée aux articles L. 331‑18 à L. 331‑24, l’Autorité de régulation de la communication audiovisuelle et numérique et les agents mentionnés au premier alinéa reçoivent les saisines adressées à l’Autorité » et la référence : « L. 331‑23 » est remplacée par la référence : « L. 331‑18 » ;

3° Au cinquième alinéa, les mots : « l’adresse électronique et » sont remplacés par les mots : « la ou les adresses électroniques dont ils disposent, ainsi que » ;

4° Après le cinquième alinéa, sont insérés huit alinéas ainsi rédigés :

« II. – Pour l’exercice de la mission mentionnée à l’article L. 331‑25, les agents habilités et assermentés de l’Autorité de régulation de la communication audiovisuelle et numérique peuvent constater les faits susceptibles de constituer des infractions prévues aux articles L. 335‑3 et L. 335‑4, lorsqu’elles sont commises sur les réseaux de communications électroniques utilisés pour la fourniture de services de communication au public en ligne.

« Dans ce cadre, les agents habilités et assermentés de l’Autorité peuvent, sans en être tenus pénalement responsables :

« 1° Participer sous un pseudonyme à des échanges électroniques susceptibles de se rapporter à ces infractions ;

« 2° Reproduire des œuvres ou objets protégés sur les services de communications au public en ligne ;

« 3° Extraire, acquérir ou conserver par ce moyen des éléments de preuve sur ces services aux fins de leur caractérisation ;

« 4° Acquérir et étudier les matériels et logiciels propres à faciliter la commission d’actes de contrefaçon.

« À peine de nullité, ces actes ne peuvent avoir pour effet d’inciter autrui à commettre une infraction.

« Les agents mentionnés au premier alinéa du présent II consignent les informations ainsi recueillies dans un procès‑verbal qui rend compte des conditions dans lesquelles les facultés reconnues aux 1° à 4° du présent article ont été employées. » 

XI. – Au premier alinéa de l’article L. 331‑21‑1, les mots : « Les membres de la commission de protection des droits, ainsi que ses agents habilités et assermentés devant l’autorité judiciaire mentionnés à l’article L. 331‑21 » sont remplacés par les mots : « Le membre de l’Autorité de régulation de la communication audiovisuelle et numérique chargé d’exercer la mission de protection des œuvres et des objets protégés, ainsi que les agents habilités et assermentés devant l’autorité judiciaire mentionnés au I de l’article L. 331‑14 ».

XII. – L’article L. 331‑22 est ainsi modifié :

1° Le premier alinéa est supprimé ;

2° Au second alinéa, la référence : « L. 331‑21 » est remplacée par la référence : « L. 331‑14 ».

XIII. – L’article L. 331‑23 est ainsi modifié :

1° Au premier alinéa, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique développe des outils visant à renforcer la visibilité de l’offre légale auprès du public et » ;

2° Au premier et au cinquième alinéas, les mots : « l’article L. 331‑34 » sont remplacés par les mots : « l’article 18 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication » ;

3  Le deuxième, le troisième et le quatrième alinéa sont supprimés.

XIV. – L’article L. 331‑24 est ainsi modifié :

1° Au premier alinéa, les mots : « La commission de protection des droit » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique » ;

2° Au cinquième alinéa, les mots : « La commission de protection des droits » sont remplacés par les mots : « l’Autorité » et les mots : « de la République » sont remplacés par les mots : « de la République ou sur la base d’un constat d’huissier établi à la demande d’un ayant‑droit » ;

3° Au dernier alinéa, il est ajouté une phrase ainsi rédigée :

« Ce délai est de douze mois s’agissant des informations transmises par le procureur de la République. »

XV. – L’article L. 331‑25 est ainsi modifié :

1° Au premier alinéa, les mots : « la commission de protection des droits peut envoyer à l’abonné, sous son timbre et pour son compte, par la voie électronique et par l’intermédiaire de la personne dont l’activité est d’offrir un accès à des services de communication au public en ligne ayant conclu un contrat avec l’abonné » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique peut envoyer à l’abonné, sous son timbre et pour son compte, par la voie électronique ou par lettre simple » ;

2° Au second alinéa, les mots : « la commission » sont remplacés par les mots : « l’Autorité » ;

3° Au troisième alinéa, les mots : « En revanche, elles ne divulguent pas » sont remplacés par les mots : « Elles précisent » et la dernière phrase est remplacée par la phrase suivante :

« Elles indiquent les coordonnées postales et électroniques où leur destinataire peut adresser, s’il le souhaite, des observations à l’Autorité » ;

4° Il est inséré un dernier alinéa ainsi rédigé :

« L’Autorité publie, dans le rapport mentionné à l’article 18 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication, des indicateurs synthétiques indiquant le nombre de saisines reçues en application de l’article L. 331‑18 et le nombre de recommandations adressées sur le fondement du présent article. »

XVI. – L’article L. 331‑26 est abrogé.

XVII. – Au premier alinéa de l’article L. 331‑27, les mots : « la commission de protection des droits » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique ».

XVIII. – L’article L. 331‑28 est ainsi modifié :

1° Au premier alinéa, les mots : « la commission de protection des droits » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique » ;

2° Au deuxième alinéa, les mots : « la commission de protection des droits » sont remplacés par les mots : « l’Autorité » et les mots : « la commission procède » sont remplacés par les mots : « l’Autorité procède ».

XIX. – L’article L. 331‑29 est ainsi modifié :

1° Au premier alinéa, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique » et les mots : « de la présente sous‑section » sont remplacés par les mots : « du présent paragraphe » ;

2° Au deuxième alinéa, les mots : « par la commission de protection des droits, des mesures prévues à la présente sous‑section » sont remplacés par les mots : « par l’Autorité, des mesures prévues au présent paragraphe » ;

3° Au dernier alinéa, les mots : « de la Haute Autorité » sont remplacés par les mots : « de l’Autorité ».

XX. – À l’article L. 331‑30, les mots : « le collège et la commission de protection des droits de la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique ».

XXI. – Après l’article L. 331‑30 sont insérés des articles L. 331‑30‑1 à L. 331‑30‑4 ainsi rédigés :

« Art. L. 331‑30‑1. – I. – L’Autorité de régulation de la communication audiovisuelle et numérique évalue l’efficacité des mesures de protection des œuvres ou objets protégés prises par les fournisseurs de services de partage de contenus en ligne mentionnés à l’article L. 137‑1.

« Ces fournisseurs de services adressent chaque année à l’Autorité une déclaration précisant les mesures mises en œuvre, les conditions de leur déploiement et de leur fonctionnement, leur niveau d’efficacité et les modalités de collaboration avec les titulaires de droits.

« L’Autorité peut, sans que puisse lui être opposé le secret des affaires, obtenir toutes informations utiles auprès des fournisseurs de services mentionnés au premier alinéa, des titulaires de droits et des concepteurs de mesures de protection pour l’exercice de la présente mission.

« II. – L’Autorité peut formuler des recommandations sur le niveau d’efficacité des mesures au regard de leur aptitude à assurer la protection des œuvres et objets protégés, y compris sur les conditions de leur déploiement et de leur fonctionnement et les modalités de leur amélioration, ainsi que sur le niveau de transparence requis.

« III. – L’Autorité rend compte de la mission prévue au présent article dans le rapport prévu à l’article 18 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication.

« Art. L. 331‑30‑2. – I. – Au titre de sa mission, l’Autorité de régulation de la communication audiovisuelle et numérique peut rendre publique l’inscription sur une liste du nom et des agissements de ceux des services de communication au public en ligne ayant fait l’objet d’une délibération dans le cadre de laquelle aura été constaté que ces services portent atteinte, de manière grave et répétée, aux droits d’auteur ou aux droits voisins.

« II. – L’engagement de la procédure d’instruction préalable à cette inscription sur la liste mentionnée au I est assuré par un membre de l’Autorité désigné par son président pour une durée de trois ans, renouvelable une fois.

« Sont qualifiés pour procéder, à la demande du membre de l’Autorité mentionné à l’alinéa précédent, à la recherche et à la constatation d’une atteinte aux droits d’auteur ou aux droits voisins les agents habilités et assermentés devant l’autorité judiciaire mentionnés au II de l’article L. 331‑14.

« Ces agents, qui disposent des pouvoirs d’enquête reconnus à l’Autorité à l’article 19 de la loi n° 86‑1067 du 30 septembre 1986 relative à la liberté de communication peuvent prendre en compte tout élément utile et solliciter des titulaires de droits d’auteur ou de droits voisins toute information relative :

« – aux autorisations d’exploitation qu’ils ont consenties à des services de communication au public en ligne ;

« – aux notifications qu’ils ont adressées aux services de communication au public en ligne ou aux autres éléments permettant de constater l’exploitation illicite d’œuvres et d’objets protégés sur ces services ;

« – aux constats effectués par les agents agréés et assermentés mentionnés à l’article L. 331‑2.

« Les constats des agents habilités et assermentés devant l’autorité judiciaire mentionnés au II de l’article L. 331‑14 font l’objet de procès‑verbaux qui sont communiqués au membre de l’Autorité mentionné au premier alinéa du II, qui, s’il estime que les éléments recueillis justifient l’inscription sur la liste mentionnée au I, transmet le dossier à cette fin au président de l’Autorité.

« III. – L’Autorité convoque alors le service de communication au public en ligne en cause à une séance publique pour le mettre en mesure de faire valoir ses observations et de produire tout élément justificatif. Cette convocation est effectuée par voie électronique sur la base des informations mentionnées au 2° de l’article 19 de la loi n° 2004‑575 du 21 juin 2004 pour la confiance dans l’économie numérique ; lorsque ces informations ne sont pas disponibles, l’Autorité informe le service concerné par l’intermédiaire de son site internet. Dans tous les cas, la convocation est adressée au moins quinze jours avant la date qu’elle fixe.

« À la date fixée pour cette séance publique, le service en cause comparaît en personne ou par l’intermédiaire de ses représentants. Le défaut de comparution personnelle ou de représentation ne fait pas obstacle à la poursuite de la procédure.

« IV. – À l’issue, l’Autorité délibère sur l’inscription du service de communication au public en ligne sur la liste mentionnée au I. L’Autorité délibère hors la présence du membre mentionné au premier alinéa du II.

« La délibération, prise après procédure contradictoire, par laquelle l’Autorité estime qu’un service de communication au public en ligne a porté atteinte, de manière grave et répétée, aux droits d’auteur ou aux droits voisins, et décide, en conséquence, de son inscription sur la liste mentionnée au I est motivée. L’Autorité fixe la durée de l’inscription sur la liste mentionnée au I, qui ne peut excéder 12 mois.

« La délibération est notifiée au service en cause par voie électronique ou publiée sur le site internet de l’Autorité, dans les conditions prévues au premier alinéa du III.

« À tout moment, le service de communication au public en ligne peut demander à l’Autorité à être retiré de la liste mentionnée au I dès lors qu’il justifie du respect des droits d’auteur et des droits voisins. L’Autorité statue sur cette demande par une décision motivée rendue après une séance publique organisée selon les modalités définies au III.

« V. – Pendant toute la durée de l’inscription sur la liste mentionnée au I, toute personne en relation commerciale avec le service mentionné, notamment pour y pratiquer des insertions publicitaires ou lui procurer des moyens de paiement de ses prestations, est tenu de rendre publique, dans des conditions que précise l’Autorité, l’existence de ces relations, et de les mentionner au rapport annuel si elle est tenue d’en adopter un.

« Art. L. 331‑30‑3. – Un décret en Conseil d’État précise les conditions d’application du présent paragraphe.

« Art. L. 331‑30‑4. – I. – Lorsqu’une décision judiciaire passée en force de chose jugée interdit la reprise totale ou partielle d’un contenu portant atteinte à un droit d’auteur ou à un droit voisin, elle est notifiée à l’Autorité de régulation de la communication audiovisuelle et numérique. L’autorité, saisie par un titulaire de droits concerné, peut demander aux personnes mentionnées au 1 du I de l’article 6 de la loi n° 2004‑575 du 21 juin 2004 pour la confiance dans l’économie numérique ainsi qu’à tout fournisseur de noms de domaine de bloquer l’accès à tout site, à tout serveur ou à tout autre procédé électronique donnant accès aux contenus jugés illicites par ladite décision.

« Dans les mêmes conditions, l’Autorité peut également demander à tout moteur de recherche ou tout annuaire de faire cesser le référencement des adresses électroniques donnant accès à ces contenus.

« Pour faciliter l’exécution des décisions judiciaires mentionnées au premier alinéa, l’Autorité adopte des modèles d’accords type qu’elle invite les ayants droits et les personnes mentionnées au 1 du I de l’article 6 de la loi n° 2004‑575 du 21 juin 2004 pour la confiance dans l’économie numérique concernées par la décision à conclure. L’accord conclu entre les parties détermine notamment leurs conditions d’information réciproque sur l’existence de violations de la décision judiciaire par les ayants droits. Il engage les personnes mentionnées au 1 du I de l’article 6 de la loi n° 2004‑575 du 21 juin 2004 pour la confiance dans l’économie numérique à prendre les mesures de blocage ou de déréférencement prévues par la décision judiciaire. 

« II. – Lorsqu’il n’est pas procédé au blocage ou au déréférencement des contenus en application des trois premiers alinéas, l’autorité judiciaire peut être saisie, en référé ou sur requête pour ordonner toute mesure destinée à faire cesser l’accès à ces contenus. »

XXII. – L’article L. 331‑31 est ainsi modifié :

1° Au premier alinéa, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique » ;

2° Au quatrième et au cinquième alinéas, les mots : « à compter du 1er janvier 2009 » sont supprimés ;

3° Au sixième alinéa, les mots : « , à compter du 1er janvier 2009, » sont supprimés ;

4° Au neuvième alinéa, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité » et les mots : « L. 331‑33 à L. 331‑35 et L. 331‑37 du présent code » sont remplacés par les mots : « L. 331‑30 à L. 331‑32 et L  331‑34 du présent code ».

XXIII. – L’article L. 331‑32 est ainsi modifié :

1° À la première phrase du premier alinéa, les mots : « à la Haute Autorité » sont remplacés par les mots : « à l’Autorité de régulation de la communication audiovisuelle et numérique » ;

2° À la seconde phrase du premier alinéa, les mots : « deux mois » sont remplacés par les mots : « quatre mois » ;

3° À la deuxième phrase du premier alinéa et aux quatrième et cinquième alinéas, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité » ;

4° Au sixième et au dernier alinéas, les mots : « de la Haute Autorité » sont remplacés par les mots : « de l’Autorité » ;

5° Au dernier alinéa, les mots : « à la Haute Autorité » sont remplacés par les mots : « à l’Autorité ».

XXIV. – À l’article L. 331‑33, la référence : « L. 331‑31 » est remplacée par la référence : « L. 331‑28 » et les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique ».

XXV. – L’article L. 331‑34 est ainsi modifié :

1° Au début du premier alinéa, est ajoutée la mention : « I. – » et les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique » ;

2° Sont insérés deux alinéas ainsi rédigés :

« II. – Au titre de sa participation à la mission de facilitation de l’accès des personnes en situation de handicap aux œuvres protégées par un droit d’auteur ou un droit voisin, l’Autorité peut recueillir auprès des éditeurs, de la Bibliothèque nationale de France et des personnes morales et établissements mentionnées au 7° de l’article L. 122‑5 toutes informations et document utiles. Elle peut à ce titre mettre en demeure les éditeurs de respecter les obligations prévues au 2° de l’article L. 122‑5‑1.

« L’Autorité peut rendre publique ces mises en demeure, qui ne peuvent conduire à des sanctions. »

XXVI. – L’article L. 331‑35 est ainsi modifié :

1° Au premier alinéa, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité de régulation de la communication audiovisuelle et numérique » ;

2° Au deuxième alinéa, les mots : « la Haute Autorité » sont remplacés par les mots : « l’Autorité » et il est ajouté une phrase ainsi rédigée :

« À compter de sa saisine, l’Autorité dispose d’un délai de quatre mois, renouvelable deux mois, pour rendre sa décision. »

XXVII. – L’article L. 331‑36 est ainsi modifié :

1° Au premier alinéa, les mots : « La Haute Autorité » sont remplacés par les mots : « L’Autorité de régulation de la communication audiovisuelle et numérique », la référence : « l’article L. 331‑32 » est remplacée par la référence : « l’article L. 331‑29 » et il est ajouté une phrase ainsi rédigée :

« L’Autorité peut déterminer dans le cadre de ses avis, les éléments constitutifs de la documentation technique prévue à l’article L. 331‑29. » ;

2° Au second alinéa, la référence : « L. 331‑31 » est remplacée par la référence : « L. 331‑28 ».

XXVIII. – Les articles L. 331‑12 à L. 331‑36, dans leur rédaction résultant du présent article font l’objet de la nouvelle numérotation suivante :

1° Les articles L. 331‑13 et L. 331‑14 deviennent les articles L. 331‑12 et L. 331‑13 ;

2° Les articles L. 331‑21, L. 331‑21‑1, L. 331‑22, L. 331‑23, L. 331‑24, L. 331‑25, L. 331‑27, L. 331‑28, L. 331‑29, L. 331‑30, L. 331‑30‑1, L. 331‑30‑2, L. 331‑30‑3, L. 331‑30‑4, L. 331‑31, L. 331‑32, L. 331‑33, L. 331‑34, L. 331‑35 et L. 331‑36 deviennent respectivement les articles L. 331‑14, L. 331‑15, L. 331‑16, L. 331‑17, L. 331‑18, L. 331‑19, L. 331‑20, L. 331‑21, L. 331‑22, L. 331‑23, L. 331‑24, L. 331‑25, L. 331‑26, L. 331‑27, L. 331‑28, L. 331‑29, L. 331‑30, L. 331‑31, L. 331‑32, et L. 331‑33 ;

3° L’article L. 331‑37 devient l’article L. 331‑34.

XXIX. – La sous‑section 3 du chapitre Ier du titre III du livre III est ainsi modifié :

1° Il est créé un paragraphe 1 intitulé : « Envoi de recommandations aux abonnés » qui comprend les articles L. 331‑18 à L. 331‑23 » ;

2° Il est créé un paragraphe 2 intitulé : « Mesures destinées à prévenir ou faire cesser des atteintes aux droits » qui comprend l’article L. 331‑24 ;

3° Il est créé un paragraphe 3 intitulé : « Caractérisation des atteintes aux droits » qui comprend les articles L. 331‑25 et L. 331‑26 ;

4° Il est créé un paragraphe 4 intitulé : « Lutte contre les sites miroirs » qui comprend l’article L. 331‑27.

XXX. – L’article L  342‑3‑1 est ainsi modifié :

1° La référence : « L. 331‑31 » est remplacée par la référence : « L. 331‑29 » et les références : « L. 331‑33 à L. 331‑35 et L. 331‑37 » sont remplacés par les références : « L. 331‑30 à L. 331‑32 et L. 331‑34 » ;

2° Au dernier alinéa, les mots : « à la Haute Autorité pour la diffusion des œuvres et la protection des droits sur internet prévue à l’article L. 331‑12 » sont remplacés par les mots : « à l’Autorité de régulation de la communication audiovisuelle et numérique ».
"""
