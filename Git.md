Aca repasaremos los comandos de git.

entonces tenemos que para empezar a trabajar con Git// lo primero sera tener nuestra cuenta  creada. preferiblemente subir algun proyecto antes a Git desde la plataforma o creamos uno nuevo 


git config --global user.name "Osbaldo"
git config --global user.name "dssfdgdsfg"
git config --global user.email "jocnals@glmail.com "

git init 

git add. 

git config -global user.email "perro@gmail.com"

git init

git add .

git commit -m "primer commit"

git remote add origin

1. Estado y ramas
• git status # Ver el estado actual de los archivos
• git branch # Ver ramas locales
• git branch -r # Ver ramas remotas
• git branch -a # Ver todas las ramas (locales y remotas)
• git branch -vv # Ver ramas locales y su upstream
2. Actualizar repositorio local
• git fetch --all # Traer información de todas las ramas remotas
• git fetch origin # Traer solo desde 'origin'
• git pull # Actualizar rama actual con su remota
• git pull origin main # Actualizar la rama main con el remoto
3. Subir cambios
• git add . # Agregar todos los cambios
• git commit -m "mensaje" # Confirmar cambios en local
• git push # Subir cambios a la rama remota configurada
• git push origin main # Subir cambios a la rama main
4. Trabajar con ramas
• git checkout -b nueva-rama # Crear y cambiar a nueva rama
• git checkout nombre-rama # Cambiar a otra rama
• git push -u origin nombre-rama # Subir una nueva rama y vincularla con el remoto
• git push --set-upstream origin rama # Configurar upstream explícitamente
5. Configuración útil
• git config --global push.autoSetupRemote true # Hacer que 'git push' configure upstream
automáticamente
6. Fusionar cambios
• git checkout main # Cambiar a la rama principal
• git pull # Actualizar main
• git merge nombre-rama # Fusionar otra rama en main
• git push # Subir cambios fusionados