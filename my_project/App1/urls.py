from django.urls import path
from App1.views import exterior, interior,inicio,carnivora,formulario_exteriores,formulario_interiores,formulario_carnivoras
urlpatterns = [
    path("",inicio, name="inicio"),
    path("Exterior/",exterior, name= "exterior"),
    path("Interior/",interior, name= "interior"),
    path("Carnivoras/",carnivora, name="carnivoras"),

    path('form-exteriores/',formulario_exteriores, name='form exteriores'),
    path('form-interiores/',formulario_interiores, name='form interiores'),
    path('form-carnivoras/',formulario_carnivoras, name='form carnivoras'),
    
    
]