from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Configuración del navegador
driver = webdriver.Edge()
driver.get("http://127.0.0.1:8000/cuentas/login/")  # Página de inicio de sesión

# Datos de prueba para agregar productos
productos = [
    {
        "nombre": f"Bolsas",
        "descripcion": f"Colores blanco, azul y rojo",
        "contacto": f"pedro9777@example.com",
        "ubicacion": f"San Javier",
        "categoria": "Plástico",  # Cambia por una categoría válida en tu base de datos
        "imagen": r"C:\Users\casti\Downloads\plasticas.jpg"  # Ruta corregida con cadena cruda
    }
    for i in range(5)  # Cambia el número de productos según sea necesario
]

# Función para iniciar sesión
def iniciar_sesion(username, password):
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'username'))
        )
        username_input.clear()
        username_input.send_keys(username)

        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'password'))
        )
        password_input.clear()
        password_input.send_keys(password)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        submit_button.click()

        WebDriverWait(driver, 10).until(EC.url_changes("http://127.0.0.1:8000/cuentas/login/"))
        print(f"Inicio de sesión exitoso para el usuario '{username}'.")
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")


## Agregar el producto
def agregar_producto(nombre, descripcion, contacto, ubicacion, categoria, imagen):
    try:
        nombre_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'nombre'))
        )
        nombre_input.clear()
        nombre_input.send_keys(nombre)

        descripcion_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'descripcion'))
        )
        descripcion_input.clear()
        descripcion_input.send_keys(descripcion)

        contacto_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'contacto'))
        )
        contacto_input.clear()
        contacto_input.send_keys(contacto)

        ubicacion_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'ubicacion'))
        )
        ubicacion_input.clear()
        ubicacion_input.send_keys(ubicacion)

        categoria_select = Select(WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'categoria'))
        ))
        categoria_select.select_by_visible_text(categoria)

        imagen_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'imagen'))
        )
        imagen_input.send_keys(imagen)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="Guardar Cambios"]'))
        )

        # Asegurarse de que el botón sea clickeable
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        try:
            submit_button.click()
        except Exception:
            driver.execute_script("arguments[0].click();", submit_button)

        print(f"Producto '{nombre}' agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar el producto '{nombre}': {e}")


usuario = "pepito"
contraseña = "leica666"

iniciar_sesion(usuario, contraseña)

# Navegar al formulario de agregar producto y procesar productos
for producto in productos:
    driver.get("http://127.0.0.1:8000/addproducto/")
    time.sleep(2)  # Esperar por si hay carga dinámica
    agregar_producto(**producto)

# Redirigir a la página de productos después de completar
driver.get("http://127.0.0.1:8000/productos/")
print("Todos los productos fueron agregados exitosamente.")

# Cerrar el navegador
driver.quit()
