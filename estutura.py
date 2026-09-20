import pyautogui

pyautogui.alert("Aula de RPA")

idade = pyautogui.prompt("informe sua idade: ")
idade = int(idade)

if idade <= 18:
    pyautogui.alert("Você é menor de idade")
else:
    pyautogui.alert("Você é maior de idade")