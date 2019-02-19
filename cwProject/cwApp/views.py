from django.http import HttpResponse


# function that are called via the chosen path in the app file
def index(request):
    return HttpResponse("Choose a path: getthegood or happyhappyjoyjoy")


def getGood(request):
    return HttpResponse("Here you go! Good books")


def happyJoy(request):
    return HttpResponse("Here you go! Childhood")

