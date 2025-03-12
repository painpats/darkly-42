# Découverte de la faille Include

## Méthodologie

Cette faille a été trouvée en exploitant la mauvaise configuration du serveur, on a utilisé une technique 
de *traversée de répertoire* pour y accéder, et on a confirmé la vulnérabilité en récupérant des fichiers 
sensibles `/etc/passwd`.

![htpasswd-breach](assets/htpasswd-flag.png)

## Détails de la faille

La faille **admin htpasswd** exploite une vulnérabilité qui permet à un attaquant d'exploiter un 
fichier `.htpasswd` mal configuré pour accéder à des fichiers système sensibles, notamment le fichier 
**/etc/passwd** ici sous Linux.

Les fichiers `.htpasswd` sont utilisés pour protéger les pages web avec un mot de passe. Cependant, 
si un fichier `.htpasswd` est mal configuré ou exposé publiquement, un attaquant peut accéder directement 
aux zones protégées de l'application en accédant au fichier.

### Type de faille

- **Vulnérabilité** : Accès non autorisé via un fichier `.htpasswd` exposé.
- **Impact** : Un attaquant peut obtenir les informations d'identification d'administrateur, ce qui lui permet
de compromettre totalement le site web ou l'application.

## Conclusion

Cette faille met en évidence l'importance de bien gérer les fichiers de configuration et de contrôler l'accès 
aux informations sensibles. Il est crucial de vérifier régulièrement la sécurité des systèmes et de mettre en 
place des contrôles d'accès appropriés.
