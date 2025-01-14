# DARKLY

# Top 10 OWASP (2021)
Ce document liste les vulnérabilités web les plus critiques. Voici une explication de chacune :

## 1. Broken Access Control (Contrôle d'accès insuffisant)

➪ Les utilisateurs peuvent accéder à des ressources ou effectuer des actions qui ne leur sont pas destinées (ex. accès non autorisé à une page admin).

*Exemple : Modifier un ID utilisateur dans l'URL pour consulter les données d'autres utilisateurs.*

## 2. Cryptographic Failures (Échecs cryptographiques)

➪ Mauvaise gestion des données sensibles, comme des mots de passe ou numéros de cartes bancaires.

*Exemple : Stocker des mots de passe en clair ou utiliser un chiffrement obsolète comme MD5.*

## 3. Injection

➪ Une entrée utilisateur non sécurisée injectée dans une commande ou requête (SQL, NoSQL, OS, etc.).

*Exemple : '; DROP TABLE users; -- dans un champ de formulaire, causant la suppression de la table.*

## 4. Insecure Design (Conception peu sécurisée)

➪ Problèmes structurels dans la conception des fonctionnalités, permettant des attaques.

*Exemple : Une application qui permet de deviner les mots de passe avec des tentatives illimitées.*

## 5. Security Misconfiguration (Mauvaise configuration de sécurité)

➪ Configurations incorrectes ou défauts exposant des vulnérabilités.

*Exemple : Laisser un fichier .env accessible publiquement.*

## 6. Vulnerable and Outdated Components (Composants vulnérables ou obsolètes)

➪ Utilisation de librairies ou frameworks dépassés contenant des failles connues.

*Exemple : Une ancienne version de jQuery vulnérable au Cross-Site Scripting (XSS).*

## 7. Identification and Authentication Failures (Défaillances d'authentification)

➪ Mauvaise gestion des sessions ou de l'authentification des utilisateurs.

*Exemple : Absence de validation de session après un changement de mot de passe.*

## 8. Software and Data Integrity Failures (Intégrité logicielle et des données)

➪ Téléchargement de logiciels ou de données non fiables.

*Exemple : Utilisation de librairies provenant de sources non vérifiées.*

## 9. Security Logging and Monitoring Failures (Défaillances de journalisation et de surveillance)

➪ Absence de logs ou incapacité à détecter une activité suspecte.

*Exemple : Un attaquant brute-force un compte sans alerte dans les logs.*

## 10. Server-Side Request Forgery (SSRF)

➪ Exploiter un serveur pour effectuer des requêtes vers des systèmes non accessibles publiquement.

*Exemple : Utiliser un formulaire pour accéder à des services internes via une URL malveillante.*
