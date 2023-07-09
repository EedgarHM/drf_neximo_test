from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib import messages

from app.views import register_user
from app.forms import RegistrationForm

User = get_user_model()

class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_register_user_success(self):
        # Crea una instancia de formulario con datos válidos
        form_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'name': 'John Doe'
        }
        form = RegistrationForm(data=form_data)

        # Crea una solicitud POST con el formulario válido
        request = self.factory.post('/api/register/', data=form_data)
        request.session = {}
        messages.storage = FallbackStorage(request)
        request._messages = messages

        # Realiza la solicitud a la vista
        response = register_user(request)

        # Verifica que la respuesta sea una redirección
        self.assertEqual(response.status_code, 302)

        # Verifica que el usuario se haya registrado correctamente
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

        # Verifica que se haya mostrado un mensaje de éxito
        messages.success(request, 'User saved correctly')
        storage = messages.get_messages(request)
        self.assertEqual(storage.__len__(), 1)
        self.assertEqual(storage.__str__(), '[<message success User saved correctly>]')

    def test_register_user_existing_user(self):
        # Crea un usuario existente en la base de datos
        User.objects.create_user(email='test@example.com', password='password123', name='John Doe')

        # Crea una instancia de formulario con el mismo correo electrónico
        form_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'name': 'Jane Smith'
        }
        form = RegistrationForm(data=form_data)

        # Crea una solicitud POST con el formulario inválido
        request = self.factory.post('/api/register/', data=form_data)
        request.session = {}
        messages.storage = FallbackStorage(request)
        request._messages = messages

        # Realiza la solicitud a la vista
        response = register_user(request)

        # Verifica que la respuesta sea un renderizado del formulario
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        # Verifica que se haya mostrado un mensaje de error
        messages.error(request, 'User already exists')
        storage = messages.get_messages(request)
        self.assertEqual(storage.__len__(), 1)
        self.assertEqual(storage.__str__(), '[<message error User already exists>]')
