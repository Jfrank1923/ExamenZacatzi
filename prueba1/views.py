from django.shortcuts import render
from .models import Datos 
import pandas as pd 
# Create your views here.



def  muestra_datos(request):
    consulta = Datos.objects.all()
    lista=calculaSuma(consulta)
    contexto= {'datos':consulta, 'suma':lista }

    print(lista)
      # data = pd.read_csv('prueba1/data1.csv')
      # for i in range(len(data)):
     #       info = Datos(
      #          x1= data['V1'][i],
       #         c1=data['C1'][i],
        #        x2 = data['V2'][i],
         #       x3 = data['V3'][i],
         #   )
         #   info.save()

    return render (request,'prueba1/index.html', contexto)

def calculaSuma(l):
        lista=[]
        for i in l:
            r=i.x1 + i.x2 + i.x3
            lista.append(r)

        return lista 