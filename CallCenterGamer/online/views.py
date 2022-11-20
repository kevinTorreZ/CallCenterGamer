from django.shortcuts import render,redirect
from online.forms import RegisterForm,LoginForm,PreguntasForm
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from online.models import Preguntas,Usuario
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Register.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"
    def form_valid(self, form):
        request = self.request
        login(request, form.save())
        return redirect('/Inicio/')
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"

    def form_valid(self, form):
        request = self.request
        Usuario = form.cleaned_data.get("Usuario")
        password = form.cleaned_data.get("password")
        remember_me = form.cleaned_data['remember_me']
        user = authenticate(request, username=Usuario, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                            request.session.set_expiry(0)
            if user.admin:
                return redirect('/Administracion/')
            return redirect('/Inicio/' + str(user.id))
        return super(LoginView, self).form_invalid(form)

def Index(request):
    return render(request, "index.html")
@login_required()
def Inicio(request, id):
    User = Usuario.objects.get(id=id)
    preguntas = Preguntas.objects.filter(Usuario=User)
    form = PreguntasForm(initial={'Usuario': id},)
    if request.method == "POST":
        guardarPregunta = Preguntas(Titulo=request.POST["Titulo"],Pregunta=request.POST["Pregunta"],Usuario=User)
        guardarPregunta.save()
        return redirect('/Inicio/' + str(id))
    return render(request, "inicio.html", {"Preguntas":preguntas,"form":form})

def ViewRespuestas(request,idPregunta):
    pregunta = Preguntas.objects.get(idPregunta=idPregunta)

    return render(request,"Respuestas.html",{"Pregunta":pregunta})