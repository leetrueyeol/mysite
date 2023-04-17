from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse("""A move that requires the opponet's answer.
  #                     \n one can enforce.""")
  return HttpResponse("A move that requires the opponet's answer. A state in which one can enforce the opponent to answer.")
