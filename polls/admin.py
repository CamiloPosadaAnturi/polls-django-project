from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):#personaliza la forma en que se muestra el modelo Question en el admin
    fieldsets = [ #organiza los campos en secciones
        (None, {"fields": ["question_text"]}), # tupla con el titulo de la seccion y un diccionario con los campos
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}), #segunda seccion con titulo y campo, collapse hace que la seccion este colapsada por defecto
    ]
    #fields = ['pub_date', 'question_text']
    # Define el orden de los campos en el admin
    inlines = [ChoiceInline] #Dentro del admin de este modelo, también quiero ver y editar las Choices relacionadas.”
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]

admin.site.register(Question, QuestionAdmin)
# Registra el modelo Question con la configuracion personalizada en el admin