from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import  json


from course.models import Course,CourseMaster
from trainer.models import Trainer
from backendapp.settings import STATIC_CHART_CONFIG


# use https://jsonformatter.curiousconcept.com/ to cross check json file is correctly formatted or not

def index(request):
    return render(request,"dashboard/dashboard.html")


def getCourseChartData(request):
    with open(STATIC_CHART_CONFIG+"\config.js") as dataFile:
        data = dataFile.read()
        obj = data[data.find('{') : data.rfind('}')+1]
        jsonObj = json.loads(obj)    
        
    
    course_list = [item[1] for item in list(Course.objects.all().values_list())]
    context = {
        "data":{
            "labels" : course_list,
            "datasets":[{
                "label" : "Courses",
                "data:":[23,41,23],
                "backgroundColor":jsonObj["backgroundColor"],
                "borderColor":jsonObj["borderColor"],
                "borderWidt":1
            }]
        }
    }
    print("\n\n type = ",context["data"], "\n\n")
    return JsonResponse({'data':context["data"]},json_dumps_params={'indent': 2})        