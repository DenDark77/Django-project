from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Реєстрація нового користувача."""
    if request.method != 'POST':
    # Виводить пусту форму
        form = UserCreationForm()
    else:
    # Обробка заповненої форми
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
    # Виконання входу і перенаправлення на домашню сторінку
            login(request, new_user)
            return redirect('learning_logs:index')

    # Виводить пусту форму або недійсну форму
    context = {'form': form}
    return render(request, 'users/register.html', context)
