import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del navegador
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")


# Configurar permisos automáticos
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,  # Permitir micrófono
    "profile.default_content_setting_values.media_stream_camera": 1,  # (Opcional) Permitir cámara
    # "profile.default_content_setting_values.geolocation": 1,  # (Opcional) Permitir geolocalización
    # "profile.default_content_setting_values.notifications": 1  # (Opcional) Permitir notificaciones
}
options.add_experimental_option("prefs", prefs)

# Inicializar el navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL de Blackboard
url = "https://cibertec.blackboard.com/webapps/login/"
driver.get(url)

# Tiempo de espera explícito
wait = WebDriverWait(driver, 10)

# Aceptar cookies si aparece el botón
try:
    agree_button = wait.until(EC.element_to_be_clickable((By.ID, "agree_button")))
    agree_button.click()
    print("Cookies aceptadas ------------------")
except Exception as e:
    print("No apareció el mensaje de cookies:", e)

# Ingresar las credenciales
try:
    # Campo de usuario
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user_id")))
    username_field.send_keys("i202216926")  # Reemplaza TU_USUARIO con tu nombre de usuario
    # Campo de contraseña
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("David182003")  # Reemplaza TU_CONTRASEÑA con tu contraseña
    # Botón de inicio de sesión
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
    login_button.click()
    # Verificar que se cargó la página del aula
    wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text()= 'Bienvenido']")))
except Exception as e:
    print("Inicio de sesion exitoso ------------------")


# Interactuar con el enlace "Cursos"
try:
    cursos_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cursos']/ancestor::a")))
    cursos_link.click()
    print("Navegaste a la pagina de cursos ------------------")
except Exception as e:
    print("Error al intentar navegar a 'Cursos':", e)
print("")

# Obtener el día de la semana (0 = lunes, 1 = martes, ..., 4 = viernes, 5 = sábado, 6 = domingo)
dia_semana = datetime.datetime.now().weekday()
# Lógica según el día de la semana
if dia_semana == 3:  # Si es jueves
    # Intentar localizar el curso 'Desarrollo de Aplicaciones' por el atributo ID
    curso = wait.until(EC.element_to_be_clickable((By.ID, "course-list-course-_1417656_1")))
    curso.click()
    print("Desarrollo de Aplicaciones Ejecutandose ------------------")
elif dia_semana == 2:  # Si es viernes
    # Intentar localizar el curso 'Desarrollo' por el atributo ID
    curso = wait.until(EC.element_to_be_clickable((By.ID, "course-list-course-_1419129_1")))
    curso.click()
    print("Pruebas de Software Ejcutandose ------------------.")
else:
    print(f"Hoy es {datetime.datetime.now().strftime('%A')}, no es jueves ni viernes.")


# Hacer clic en "Unirse a la sesión"
try:
    # Esperar a que el botón "Unirse a la sesión" sea visible y clicable
    unirse_sesion_button = wait.until(EC.element_to_be_clickable((By.ID, "sessions-list-dropdown")))
    unirse_sesion_button.click()
except Exception as e:
    print("Error al intentar acceder a la 'Sala del curso':", e)


# Hacer clic en "Microfono"
try:
    # Esperar y localizar el enlace "Sala del curso"
    microfono = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@ng-click, 'courseOutline.joinSession(courseOutline.courseRoomSession.id)')]")
        )
    )
    microfono.click()
    print("Entrando a Clase Videoconferencia ------------------")
except Exception as e:
    print("Error al intentar acceder a la 'Sala del curso':", e)

print("Bot Listo XRMX")
# Mantener el navegador abierto hasta que el usuario presione Enter
input("Presiona Enter para cerrar el navegador...")

# Cerrar el navegador
driver.quit()
