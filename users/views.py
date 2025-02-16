from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.contrib.auth import login
from users.forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView

from users.models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'admin@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
