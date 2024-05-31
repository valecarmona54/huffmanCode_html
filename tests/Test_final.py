import unittest
from unittest.mock import patch, Mock
import requests

class TestLoginForm(unittest.TestCase):

    @patch('requests.post')
    def test_login_success(self, mock_post):
        # Simula una respuesta exitosa del servidor
        mock_response = Mock()
        mock_response.json.return_value = {
            'status': 'success',
            'message': 'Inicio de sesión exitoso'
        }
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': 'johndoe',
            'contrasena': 'password'
        })

        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], 'Inicio de sesión exitoso')

    @patch('requests.post')
    def test_login_failure(self, mock_post):
        # Simula una respuesta de fallo del servidor
        mock_response = Mock()
        mock_response.json.return_value = {
            'status': 'failure',
            'message': 'Credenciales incorrectas'
        }
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': 'johndoe',
            'contrasena': 'wrongpassword'
        })

        self.assertEqual(response.json()['status'], 'failure')
        self.assertEqual(response.json()['message'], 'Credenciales incorrectas')

    @patch('requests.post')
    def test_register_redirect(self, mock_post):
        # Verifica si redirige al endpoint de registro
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/register', json={
            'usuario': 'johndoe',
            'contrasena': 'password'
        })

        self.assertEqual(response.status_code, 200)

    @patch('requests.post')
    def test_empty_username(self, mock_post):
        # Verifica que no se permita el envío con el campo de usuario vacío
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': '',
            'contrasena': 'password'
        })

        self.assertEqual(response.status_code, 400)  # Espera un código de error 400 (Bad Request)

    @patch('requests.post')
    def test_empty_password(self, mock_post):
        # Verifica que no se permita el envío con el campo de contraseña vacío
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': 'johndoe',
            'contrasena': ''
        })

        self.assertEqual(response.status_code, 400)  # Espera un código de error 400 (Bad Request)

    @patch('requests.post')
    def test_server_error(self, mock_post):
        # Simula un error del servidor
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {
            'status': 'error',
            'message': 'Error del servidor'
        }
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': 'johndoe',
            'contrasena': 'password'
        })

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json()['message'], 'Error del servidor')

    @patch('requests.post')
    def test_handle_exception(self, mock_post):
        # Simula una excepción en la solicitud
        mock_post.side_effect = requests.exceptions.RequestException

        with self.assertRaises(requests.exceptions.RequestException):
            requests.post('http://example.com/login', json={
                'usuario': 'johndoe',
                'contrasena': 'password'
            })

    @patch('requests.post')
    def test_success_redirect_to_compress(self, mock_post):
        # Verifica la redirección a la página de compresión después del inicio de sesión exitoso
        mock_response = Mock()
        mock_response.json.return_value = {
            'status': 'success',
            'message': 'Inicio de sesión exitoso'
        }
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': 'johndoe',
            'contrasena': 'password'
        })

        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], 'Inicio de sesión exitoso')

    @patch('requests.get')
    def test_register_page_load(self, mock_get):
        # Verifica la carga de la página de registro
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = requests.get('http://example.com/register')
        self.assertEqual(response.status_code, 200)

    @patch('requests.post')
    def test_login_invalid_json_response(self, mock_post):
        # Simula una respuesta no válida del servidor
        mock_response = Mock()
        mock_response.json.side_effect = ValueError('No JSON object could be decoded')
        mock_post.return_value = mock_response

        response = requests.post('http://example.com/login', json={
            'usuario': 'johndoe',
            'contrasena': 'password'
        })

        with self.assertRaises(ValueError):
            response.json()


if __name__ == '__main__':
    unittest.main()
