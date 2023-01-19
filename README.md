# Calculatrice9000

Ce repository contient une calculatrice réalisée en Python avec une interface graphique Tkinter.

Chaque touche que l'on voit faite avec un "Button" de Tkinter. Ils possèdent donc chacun une commande différente, qui s'exécute pour la plupart avec la fonction "click".
La commande "EXE" fonctionne avec "equals_to" et AC avec "clear".
Avoir créé les boutons un à un m'a permis de leur donner des propriétés différentes, notamment au niveau des couleurs, des tailles et des marges. Cependant, il aurait été 
aussi possible de créer tous les boutons d'un seul coup avec une list par exemple.

Pour l'affichage, j'ai utilisé deux "Label", un pour le calcul que l'on effectue, l'autre pour le résultat. Cette partie fonctionne avec la fonction "equals_to". Celle-ci est 
par ailleurs est en deux partie, afin de renvoyer un message d'erreur en cas d'opération interdite.
