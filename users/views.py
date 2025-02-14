from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import login
from users.forms import MyUserCreation
from django.contrib.auth.views import LoginView, LogoutView


class RegisterView(FormView):
    form_class = MyUserCreation
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        # from_email = ''
        recipient_list = [user_email]
        send_mail(subject, message, recipient_list)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
