from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView): #crea clase que muestra una lista de cosas
    template_name = "polls/index.html" #especifica el template a usar
    context_object_name = "latest_question_list" #nombre del contexto que se pasara al template

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
    #Question.objects. trae todas las preguntas
    #order_by("-pub_date") las ordena por fecha de publicacion, el - indica que es en orden descendente
    #[:5] limita el resultado a las ultimas 5 preguntas
    #__lte es un "lookup" de Django que significa Less Than or Equal (menor o igual que).
    #timezone.now() obtiene la fecha y hora actual con zona horaria
    #en cristiano significa que solo muestra las preguntas cuya fecha de publicacion es menor o igual a la fecha y hora actual, es decir, las que ya han sido publicadas

class DetailView(generic.DetailView): #crea clase que muestra los detalles de un objeto
    model = Question #envia un onjeto llamado Question al template
    template_name = "polls/detail.html" #especifica el template a usar
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
        #solo muestra las preguntas cuya fecha de publicacion es menor o igual a la fecha y hora actual, es decir, las que ya han sido publicadas

class ResultsView(generic.DetailView): #crea clase que muestra los resultados
    model = Question #envia un objeto llamado Question al template
    template_name = "polls/results.html" #especifica el template a usar

def vote(request, question_id): #recibe la peticion del usuario (request) y el id de la pregunta (question_id)
    question = get_object_or_404(Question, pk=question_id)
    #busca la pregunta en la base de datos, si no la encuentra devuelve un error 404
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #busca la opcion seleccionada por el usuario y obtiene el id que marco el usuario
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html", #si eligio bien lo manda a la pagina de resultados
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            }, #si no eligio bien lo manda de nuevo a la pagina de detalle con un mensaje de error
        )
    else:
        selected_choice.votes = F("votes") + 1 #incrementa en 1 el numero de votos de la opcion seleccionada
        selected_choice.save() #lo guarda en la base de datos
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) #usa "polls:results" para obteer la url
    #HttpResponseRedirect() envía al usuario a esa página


#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def index(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #context = {"latest_question_list": latest_question_list}
    #return render(request, "polls/index.html", context)

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)