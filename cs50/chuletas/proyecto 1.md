def new_entry(request):
	if request.method == "POST":
		form = NewEntryForm(request.POST)
		if form.is_valid():
			entry = form.cleaned_data["entry"]
			title = form.cleaned_data["title"]
			#If entry does not exist, save it
			if not util.get_entry(title.capitalize()):
				util.save_entry(title,entry)
				return HttpResponseRedirect(reverse("title", kwargs={'title': title}))
			else:
				return render(request,"encyclopedia/errormsg.html",{
					"errormsg": 'Entry "'+title.capitalize()+'" alreay exists!'
					})	
		else:
			return render(request,"encyclopedia/new_entry.html",{
				"form": form
				})
	return render(request,"encyclopedia/new_entry.html",{
		"form": NewEntryForm()
		})


-- template new_page
{% extends "encyclopedia/layout.html" %}

{% block title %}
    New entry
{% endblock %}

{% block body %}
    <h1>New entry</h1>
    <form action="{% url 'new_entry' %}" method="post">
		{% csrf_token %}
		{{ form }}
        <input type="submit" value="Save">                    
    </form>
{% endblock %}

The project needs the library 

pip install html2markdown

https://pypi.org/project/html2markdown/

for edit entries in markdown format