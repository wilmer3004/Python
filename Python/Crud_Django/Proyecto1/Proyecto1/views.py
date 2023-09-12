from django.http import HttpResponse
import datetime

# Insercion de lenguaje de etiquetado HTML
def saludo(request):
    documento=""""<html>
    <body>
    <h1>
    Hello world!
    </h1>
    </body>
    </html>    
    """
    
    
    return HttpResponse(documento)

# Definicion de varias urls
def despedida(request):
    
    return HttpResponse('Good bye world')


def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h1>
    La fecha y hora actual es %s
    </h1>
    </body>
    </html>    
    """ % fecha_actual
    return HttpResponse(documento)

def calcularEdad(request, agno):
    
    edadActual = 18
    periodo = agno - 2023
    edadFutura=edadActual+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendras %s años
    </h1>
    </body>
    </html>    
    """ % (agno,edadFutura)
    return HttpResponse(documento)

    


