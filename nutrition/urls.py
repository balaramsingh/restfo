from django.urls import path,include
from .views import (
                       nutrition,
                       ask_question,get_answer,
                       diet_plan, get_diet_plan,
                       nutrition_value,get_nut_val,
                       ingredients,get_dish_ing,
                       nut_val,get_dish_nut
                        )
urlpatterns = [    
    path('',nutrition),
    path('question/', ask_question),
    path('question/answer/', get_answer),

    path('diet_plan/', diet_plan),
    path('diet_plan/get_diet_plan/', get_diet_plan),

    path('nutrition_value/',nutrition_value),
    path('nutrition_value/get_nut_val/', get_nut_val),

    path('ingredients/',ingredients),
    path('ingredients/get_dish_ing/', get_dish_ing),

    path('nutrition_values/',nut_val),
    path('nutrition_values/get_dish_nut/', get_dish_nut),
]