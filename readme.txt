Git - Arnedo Barea, Luis - 21699839Y.
Tenemos Git instalado en el sistema pero no lo tenemos inicializado con el usuario ni nada. 
Por ello, lo primero es hacer:

git config --global user.name lab36-ua
git config --global user.email lab36@alu.ua.esç

De esta manera, hemos configurado los ajustes de manera global, es decir, serían los valores por defecto para todos los repositorios que creemos o importemos a no ser que establezcamos otros de manera local o global. 
Tenemos un proyecto de una aplicación ‘adivinanza.py’. Ahora podemos crear un repositorio en github: Nuevo Repositorio -> Rellenamos los datos, y lo creamos vacío.
Seguimos los pasos para inicializarlo:

echo "# git-dca" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lab36-ua/git-dca.git
git push -u origin main

Si por ejemplo queremos crear algunos alias, vamos a comenzar con un alias global muy útil:

git config –global alias.ci commit 

De esta manera, podemos hacer un commit con “git ci -m “mensaje””. Otro sería:

git config --global alias.hist 'log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short'

Ahora, vamos a crear un alias local para el repositorio. Por ejemplo:

git config alias.st status

Para que, a partir de ahora, dentro de nuestro repositorio, podemos hacer “git st” para ver el status. 
Ahora vamos a crear el fallo y vamos a utilizar “git bisect”. Vamos a introducir un print que hace que el juevo siempre devuelva error cuando el usuario adivina el número. Hacemos commit y push. Hacemos un par de commits más correctos. Y empezamos con:

git bisect start

Seleccionamos un commit que sabemos que aún no tenía el error:

git bisect good 0d956f3a9190e66a64c94048f3a4205894277c8f

Luego indicamos que el commit en el que nos encontramos sí que tiene el error:

git bisect bad
git bisect bad
git bisect good

Y nos devuelve la siguiente información:

a525fc3e5b3121c93b81311f234feb89dc8b5131 is the first bad commit
commit a525fc3e5b3121c93b81311f234feb89dc8b5131
Author: lab36-ua <lab36@alu.ua.es>
Date:   Tue Dec 19 11:39:26 2023 +0100

	Commit que introduce el fallo

 adivinanza.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

En la que podemos ver el hash del commit, podemos ver quién introdujo el fallo, qué archivos y cuánto los modificó y cuándo. 
Detenemos la bisección con:

git bisect reset

Arreglamos el error y lo commiteamos. 
Ahora vamos a usar un hook. En concreto vamos a crear el hook prepare-commit-msg:

#!/bin/sh

echo "# Please include a useful commit message!" > $1

Y lo añadimos a .git/hooks. Después, creamos un archivo ‘testHook.py’ y hacemos un commit, pudiendo ver cómo se muestra el mensaje que hemos añadido.
(Importante dar permisos de ejecución al hook). 


