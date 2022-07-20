Instruccion en desuso para el chromedriver (v102)

increase = driver.find_element_by_id("increase")

Nueva instruccion

from selenium.webdriver.common.by import By
increase = driver.find_element(By.ID, "increase")

Como subir un proyecto local a GitHub

Nos vamos a la carpeta del proyecto y ejecutamos estos comandos.

git init

git add .

git commit -m "first commit"

git remote add origin https://github.com/NOMBRE_USUARIO/NOMBRE_PROYECTO.git

git push -u origin master

Entrar al container para correr comandos

docker exec -it (Container ID) bash -l