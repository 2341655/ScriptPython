*** Settings ***
Library    SeleniumLabrary
*** Test Cases ***
tc01 Premiertest
    Open Browser    https://www.google.com  get count
    sleep    6
