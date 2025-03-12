# XSS Advanced
/?page=media&src=nsa

## Méthodologie
Dans ce cas, la faille a été exploitée en injectant un script JavaScript en base64 `<script>alert('Hello');</script>` directement via l'URL du site :

http://10.13.248.135/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnSGVsbG8nKTs8L3NjcmlwdD4=

## Détails de la faille
La faille XSS (Cross-Site Scripting) permet à un attaquant d'injecter du code JavaScript malveillant dans une application web.
Si ce code est exécuté par un utilisateur qui consulte la page, cela peut conduire à des attaques comme le vol de cookies,
l'exécution de commandes malveillantes ou encore la redirection vers des pages de phishing.

Cette technique repose sur l'utilisation d'un schéma data: pour injecter du code directement dans la page sans avoir besoin d'un champ de saisie.
Lorsque l'URL est chargée dans un navigateur vulnérable, le script est interprété et exécuté, permettant à un attaquant de réaliser des actions malveillantes.

## Type de faille

- **Vulnérabilité** : Exécution de scripts malveillants via une URL manipulée contenant du code encodé en Base64.
- **Impact** : Un attaquant peut voler des informations sensibles, comme les cookies d'une session active, ou rediriger l'utilisateur vers un site malveillant.

## Conclusion
Cette faille met en évidence l'importance de valider et d'assainir toutes les entrées utilisateur dans une application web, y compris les paramètres d'URL.
Il est essentiel d'utiliser des méthodes de filtrage ou d'échappement pour prévenir l'injection de scripts malveillants.
Les applications doivent également appliquer des politiques de sécurité telles que la politique de sécurité de contenu (CSP)