from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Edge()
driver.get("http://127.0.0.1:8000/signUp/")

def generar_datos(i):
    username = f"pedro{random.randint(1000, 9999)}"
    rut = f"696969696-6{random.randint(1, 99)}"
    email = f"arielquazada564{i}{random.randint(1000, 9999)}@gmail.com"
    password = f"leica666{i}"
    return username, rut, email, password

def formulario(username, rut, email, password):
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'username')))
        username_input.clear()
        username_input.send_keys(username)

        rut_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'rut')))
        rut_input.clear()
        rut_input.send_keys(rut)

        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'email')))
        email_input.clear()
        email_input.send_keys(email)

        pass_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password1")))
        pass_input.clear()
        pass_input.send_keys(password)

        pass2_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password2")))
        pass2_input.clear()
        pass2_input.send_keys(password)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Registrar"]')))
        
        print(f"Enviando: {username}, {email}")
        ActionChains(driver).move_to_element(submit_button).perform()
        time.sleep(1)
        submit_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_changes("http://127.0.0.1:8000/signUp/"))
        
        print(f"Formulario enviado{username}, {email}")
    except Exception as e:
        print(f"Error no se envió la wea {username} {e}")

for i in range(10):
    username, rut, email, password = generar_datos(i)
    print(f"Enviando con los datos: {username}, {rut}, {email}, {password}")
    formulario(username, rut, email, password)
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/signUp/")

driver.quit()
