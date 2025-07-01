# 1 Avantages observés

- **Automatisation des tests :**
  - Gagne du temps car les tests se font rapidement
  - Moins d’erreurs humaines, les tests sont toujours les mêmes
  - Permet de tester beaucoup de cas automatiquement
  - Trouve les bugs plus tôt

- **CI/CD :**
  - Permet d’intégrer le code souvent et facilement
  - Automatise les déploiements, réduit les erreurs
  - Teste le code automatiquement à chaque changement
  - Donne un retour rapide sur la qualité du code

# 2 Défis rencontrés

- **Avec Selenium :**
  - Parfois les tests échouent sans raison claire (instables)
  - Il faut souvent mettre à jour les tests quand l’interface change
  - Les tests peuvent être lents
  - Gestion compliquée des versions de navigateurs et drivers

- **Pour améliorer la stabilité :**
  - Utiliser des attentes explicites pour attendre les éléments
  - Organiser le code avec des objets Page Object
  - Nettoyer les champs avant de taper
  - Avoir un environnement de test stable

# 3 Métriques importantes

- Pour le projet :
  - Pourcentage de tests réussis
  - Durée des tests
  - Couverture des tests (combien de code est testé)
  - Nombre de bugs trouvés avant la production
  - Fréquence des déploiements

- Pour le pipeline CI/CD :
  - Temps total pour faire un build et déployer
  - Combien de fois le pipeline échoue
  - Temps pour corriger les erreurs
  - Satisfaction des utilisateurs après chaque mise à jour
