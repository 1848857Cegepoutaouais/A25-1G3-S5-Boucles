import pytest
from ExDebug1 import environnement_optimal

#Test Unitaire pour la fonction environnement_optimal
def test_environnement_optimal():
    #Arange : préparer les valeurs des variables d'entrées et le résultat attendu
    temp = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    # Act : appeler la fonction
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu

#Test Unitaire pour la fonction environnement_optimal
def test_environnement_optimal_2():
    #Arange : préparer les valeurs des variables d'entrées et le résultat attendu
    temp = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    # Act : appeler la fonction
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu

#Test Unitaire pour la fonction environnement_optimal
def test_environnement_optimal_3():
    #Arange : préparer les valeurs des variables d'entrées et le résultat attendu
    temp = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    # Act : appeler la fonction
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu

#Test Unitaire pour la fonction environnement_optimal
def test_environnement_optimal_4():
    #Arange : préparer les valeurs des variables d'entrées et le résultat attendu
    temp = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    # Act : appeler la fonction
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu