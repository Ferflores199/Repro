from django.contrib.auth import get_user_model
from django.core.cache import cache
from login.models import CustomUser  

class LockoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Usuario autenticado, restablece el contador de intentos fallidos
            request.user.failed_login_attempts = 0
            request.user.save()
        elif request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
            # Intento de inicio de sesión
            username = request.POST['username']
            password = request.POST['password']
            user = CustomUser.objects.filter(username=username).first()

            if user and not user.is_locked:
                # Comprueba si las credenciales son correctas
                if not user.check_password(password):
                    # Las credenciales son incorrectas, registra el intento fallido
                    user.failed_login_attempts += 1
                    user.save()

                    # Si se supera el número máximo de intentos, bloquea al usuario
                    if user.failed_login_attempts >= 3:
                        user.lock_user()  # Llama al método personalizado para bloquear al usuario
                        # Aquí puedes notificar al administrador o realizar otras acciones
                else:
                    # Las credenciales son correctas, restablece el contador
                    user.failed_login_attempts = 0
                    user.save()

        response = self.get_response(request)
        return response