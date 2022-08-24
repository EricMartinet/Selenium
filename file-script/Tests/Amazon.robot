*** Settings ***
Documentation    Ceci est un test
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
L'utilisateur doit se connecter pour s'enregistrer lorsque je clique sur retour
    [Documentation]    Ouvre le site d'amazon
    [Tags]      smoke
    open browser    https://www.amazon.com  chrome
    sleep    3s
    close browser