from django.shortcuts import render
from .utils import encrypt_text, decrypt_text

def home(request):
    return render(request, 'theapp/home.html')

def encrypt_view(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        encrypted_text = encrypt_text(input_text)
        return render(request, 'theapp/encrypt.html', {'encrypted_text': encrypted_text})
    return render(request, 'theapp/encrypt.html')

def decrypt_view(request):
    if request.method == 'POST':
        input_numbers = request.POST['input_numbers']
        decrypted_text = decrypt_text(input_numbers)
        return render(request, 'theapp/decrypt.html', {'decrypted_text': decrypted_text})
    return render(request, 'theapp/decrypt.html')


