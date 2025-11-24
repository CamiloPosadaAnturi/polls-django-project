#ALL OF POLLS/VIEW.PY

#Question.objects. trae todas las preguntas
    #order_by("-pub_date") las ordena por fecha de publicacion, el - indica que es en orden descendente
    #[:5] limita el resultado a las ultimas 5 preguntas
    #__lte es un "lookup" de Django que significa Less Than or Equal (menor o igual que).
    #timezone.now() obtiene la fecha y hora actual con zona horaria
    #en cristiano significa que solo muestra las preguntas cuya fecha de publicacion es menor o igual a la fecha y hora actual, es decir, las que ya han sido publicadas

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def index(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #context = {"latest_question_list": latest_question_list}
    #return render(request, "polls/index.html", context)

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)