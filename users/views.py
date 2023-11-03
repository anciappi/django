from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    # Condicional para saber si se carga el form o no
    # Muestra el form de registro
    if request.method == "GET":
        print("Mirando el form")
        return render(request, 'register.html', {
            'form': UserCreationForm
        })
    else:
        # Muestra los datos cargados en el form con el metodo POST
        print("obteniendo datos")
        print(request.POST)

        # Conprueba que la password no sea distinta
        # Si es distinta retorna al form
        if (request.POST['password1']) == (request.POST['password2']):
            # se captura el error en caso de que falle con un try / except
            try:
                # Si coincide crea al usuario en la db
                # Guardar el usuario en una variable
                # Creando usuario en la db
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                
                print("Se creo el usuario")
                # Retorna al form con el usuario creado
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'valid': "User created",
                })
            except:
                print("No se creo el usuario")
                # Si el usuario existe envia este mensaje
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'valid': "User already exist",
                })
        else:
            return render(request, 'register.html', {
                'form': UserCreationForm,
                'valid': "Password do not match",
            })


def login(request):
    return render(request, 'login.html')
