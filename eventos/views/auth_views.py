from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from eventos.models import Alumno


@login_required
def redirect_dashboard(request):
    user = request.user

    # Administrador
    if user.is_staff or user.is_superuser:
        return redirect('admin_dashboard')

    # Alumno
    if Alumno.objects.filter(user=user).exists():
        return redirect('alumno_dashboard')

    # Fallback
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login')
