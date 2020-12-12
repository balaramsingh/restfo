from django.shortcuts import render
from django.http.response import HttpResponse
import requests,json

def nutrition(request):
    return render(request,'nutrition/nutrition.html')

def getanswer(q):
    link = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"
    header = {"X-RapidAPI-Key": "50ebe9284bmsh6a7bcba3637e3eep14602bjsn109feaaaceb4"}

    param={"q":q}

    response = requests.get(link, headers=header,params=param)
    val=response.json()
    print(val)
    data=[]
    data.append(val['answer'])
    data.append(val['image'])
    return data

def ask_question(request):
    return render(request, 'nutrition/question.html')

def get_answer(request):
    context = {}
    if request.method=='GET':
        question=request.GET.get('q')
        data=getanswer(question)
        context={
        'data':data,
        'question':question
        }
    return render(request,'nutrition/answer.html',context)


def getplan(calories,duration):
    link = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
    header = {"X-RapidAPI-Key": "50ebe9284bmsh6a7bcba3637e3eep14602bjsn109feaaaceb4"}

    param={"targetCalories":calories,"timeFrame":duration}
    response = requests.get(link, headers=header,params=param)
    val=response.json()

    time = ["BreakFast","Lunch","Dinner"]
    data = []
    if duration=="day":
        count=0
        for name in val["meals"]:
            temp=[]
            temp.append(name['title'])
            temp.append(name['readyInMinutes'])
            temp.append(val['nutrients']['calories'])
            temp.append(val['nutrients']['protein'])
            temp.append(val['nutrients']['fat'])
            temp.append(val['nutrients']['carbohydrates'])
            temp.append(time[count])
            count = count+1
            data.append(temp)
        return data
    else:
        for name in val["items"]:
            x = name['value'][40:][:-2]
            if x[0]=='"':
                data.append(x[1:])
            else:
                data.append(x)
        return data


def diet_plan(request):
    return render(request, 'nutrition/diet_plan.html')

def get_diet_plan(request):
    context = {}
    if request.method=="GET":
        calories = request.GET.get('calories')
        duration = request.GET.get('duration')
        if duration=="day":
            dur=0
        else:
            dur=1
        data = getplan(calories,duration)

        if duration=="day":
            context = {
               'data': data,
               'cal' : data[0][2],
               'pro' : data[0][3],
               'fat' : data[0][4],
               'carb': data[0][5],
               'dur':dur,
            }
        else:
            context = {
               'data':data,
               'dur':dur,
               'list':list
            }
    return render(request,'nutrition/meal_plan.html',context)


def getnut(item):
    link = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"
    header = {"X-RapidAPI-Key": "50ebe9284bmsh6a7bcba3637e3eep14602bjsn109feaaaceb4"}

    param={"title":item}
    response = requests.get(link, headers=header,params=param)
    val=response.json()

    data=[]
    data.append(val['calories']['value'])
    data.append(val['calories']['unit'])
    data.append(val['calories']['confidenceRange95Percent']['min'])
    data.append(val['calories']['confidenceRange95Percent']['max'])

    data.append(val['fat']['value'])
    data.append(val['fat']['unit'])
    data.append(val['fat']['confidenceRange95Percent']['min'])
    data.append(val['fat']['confidenceRange95Percent']['max'])

    data.append(val['protein']['value'])
    data.append(val['protein']['unit'])
    data.append(val['protein']['confidenceRange95Percent']['min'])
    data.append(val['protein']['confidenceRange95Percent']['max'])

    data.append(val['carbs']['value'])
    data.append(val['carbs']['unit'])
    data.append(val['carbs']['confidenceRange95Percent']['min'])
    data.append(val['carbs']['confidenceRange95Percent']['max'])
    return data



def nutrition_value(request):
    return render(request, 'nutrition/nutrition_value.html')


def get_nut_val(request):
    context = {}
    if request.method=="GET":
        item = request.GET.get('item')
        data = getnut(item)
        context = {
           'data':data,
           'item':item
        }
    return render(request,'nutrition/disp_nutrition_val.html',context)


def getdish(ingredients):
    link = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
    header = {"X-RapidAPI-Key": "50ebe9284bmsh6a7bcba3637e3eep14602bjsn109feaaaceb4"}

    param={"ingredients":ingredients}
    response = requests.get(link, headers=header,params=param)
    val=response.json()

    data = []
    for name in val:
        temp = []
        temp.append(name['title'])
        temp.append(name['image'])
        data.append(temp)
    return data


def ingredients(request):
    return render(request, 'nutrition/ingredients.html')


def get_dish_ing(request):
    context = {}
    if request.method=="GET":
        ingredients = request.GET.get('ingredients')
        data = getdish(ingredients)
        context = {
            'data': data,
            'ingredients' : ingredients
        }
    return render(request, 'nutrition/get_dish_ing.html',context)


def getdish_nut(minCarbs,maxCarbs,minFat,maxFat,minProtein,maxProtein,minCalories,maxCalories):
    link = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients"
    header = {"X-RapidAPI-Key": "50ebe9284bmsh6a7bcba3637e3eep14602bjsn109feaaaceb4"}

    param={"minCarbs":minCarbs,"maxCarbs":maxCarbs, "minProtein":minProtein, "maxProtein":maxProtein,
           "minFat":minFat,"maxFat":maxFat,"minCalories":minCalories,"maxCalories":maxCalories,"number":10}
    response = requests.get(link, headers=header,params=param)
    val=response.json()

    data = []
    for name in val:
        temp = []
        temp.append(name['title'])
        temp.append(name['image'])
        temp.append(str(name['calories']))
        temp.append(str(name['protein']))
        temp.append(str(name['fat']))
        temp.append(str(name['carbs']))
        data.append(temp)
    return data


def nut_val(request):
    return render(request, 'nutrition/nut_values.html')

def get_dish_nut(request):
    context = {}
    if request.method=="GET":
        minCarbs = request.GET.get('minCarbs')
        maxCarbs = request.GET.get('maxCarbs')
        minFat = request.GET.get('minFat')
        maxFat = request.GET.get('maxFat')
        minProtein = request.GET.get('minProtein')
        maxProtein = request.GET.get('maxProtein')
        minCalories = request.GET.get('minCalories')
        maxCalories = request.GET.get('maxCalories')
        data = getdish_nut(minCarbs,maxCarbs,minProtein,maxProtein,minFat,maxFat,minCalories,maxCalories)
        context = {
            'data': data,
        }
    return render(request, 'nutrition/get_dish_nut.html',context)
