from botcity.core import DesktopBot
from telnetlib import STATUS
import gspread
from h11 import SEND_RESPONSE
from oauth2client.service_account import ServiceAccountCredentials
from pyparsing import col
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
from PySimpleGUI import PySimpleGUI as sg
from openpyxl import Workbook, load_workbook

#Abrindo navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://app.e-kontroll.com.br/login')
navegador.maximize_window()
time.sleep(5)

#Logando
navegador.find_element(By.XPATH,'/html/body/div/div/section/form/div[1]/input').send_keys('')
time.sleep(1)
navegador.find_element(By.XPATH,'/html/body/div/div/section/form/div[2]/input').send_keys('')
time.sleep(1)
navegador.find_element(By.XPATH,'/html/body/div/div/section/form/div[3]/button').click()
time.sleep(5)
navegador.find_element(By.XPATH,'//*[@id="dlgModalFeira"]/div/div/div/div/button').click()
time.sleep(1)
navegador.find_element(By.XPATH,'//*[@id="sidebar-menu"]/div/ul/li[6]/a/nobr').click()
time.sleep(3)
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/nav/ul/li[1]/a').click()
time.sleep(5)

while True:  
    navegador.find_element(By.XPATH,'//*[@id="tabela_wrapper"]/div[3]/div[1]/div/table/thead/tr[2]/th[4]').click()
    time.sleep(1)
    navegador.find_element(By.XPATH,'//*[@id="tabela_wrapper"]/div[3]/div[1]/div/table/thead/tr[2]/th[4]').click()
    time.sleep(1)
    status = navegador.find_element(By.XPATH,'//*[@id="tabela"]/tbody/tr[1]/td[4]/a').text
    if status == 'Inativado':
        navegador.find_element(By.XPATH,'//*[@id="tabela"]/tbody/tr[1]/td[2]/a').click()
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="eapiForm"]/fieldset[1]/div/div/span/small').click()
        time.sleep(1)
        navegador.find_element(By.XPATH,'//*[@id="eapiForm"]/fieldset[3]/div[1]/div/span/small').click()
        time.sleep(1)
        navegador.find_element(By.XPATH,'//*[@id="eapiForm"]/div/div/div/div/div[1]/a').click()
        time.sleep(5)
        navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/nav/ul/li[1]/a').click()
        time.sleep(5)
    

