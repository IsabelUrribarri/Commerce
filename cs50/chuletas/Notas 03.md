1) Crear un nuevo proyecto

django-admin startproject PROJECT_NAME

2) Crear una nueva aplicacion

python manage.py startapp APP_NAME

3)Levantar el servidor web

python manage.py runserver

4)Como correr los test de una aplicacion (flight)

python manage.py test

5) Estructura de la aplicacion 

- Se crea un proyecto, el proyecto tiene urls.
- Dentro del proyecto se crean aplicaciones, cada aplicacion tiene su url. Por ejemplo: Proyecto/App para la url de la aplicacion(app) es "".
- Cada url llama a una vista, que realmente es una funcion. Los url tienen que pasar el tipo de request, por defecto es get. 
- Dentro del archivo views estan las funciones. Estas funciones reciben parametros del url, como por ejemplo el tipo de request y algun string, entre otros. Estas funciones dentro de views pueden usar librerias de python y son las que llaman a las paginas html que se van  a mostrar. Cuando se llaman a las paginas html (render) se puede enviar informacion dentro de variables; como por ejemplo la entrada que se quiere visualizar.

Pista para el proyecto

By default, when substituting a value in a Django template, Django HTML-escapes the value to avoid outputting unintended HTML. If you want to allow for an HTML string to be outputted, you can do so with the safe filter (as by adding |safe after the variable name you’re substituting).


 action="{% url 'index' %}" method="post"


 if request.method == 'POST':
        title = request.POST.get('q')
        text = util.get_entry(title.capitalize())
        if text:
            return render(request, "encyclopedia/title.html", {
            "entry": util.get_entry(title.capitalize()), 
            "name": title.capitalize()})
        else:
            all_entries = list(util.list_entries())
            new_list = []
            for entry in all_entries:
                if entry.upper().count(title.upper()) > 0:
                    new_list.append(entry)
            return render(request, "encyclopedia/index.html", {
                "entries": new_list
            })