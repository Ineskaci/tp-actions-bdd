def test_moyenne():
    # On appelle la fonction de calcul de moyenne
    resultat = moyenne([10, 14, 16])
    
    # On vérifie si le résultat attendu est correct (ici 13.33 ou 13.4 par exemple)
    assert resultat == 13.33
