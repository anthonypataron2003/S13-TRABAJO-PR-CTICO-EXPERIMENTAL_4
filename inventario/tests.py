from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Categoria,Producto
class VariantTests(TestCase):
    def setUp(self):
        self.client.force_login(get_user_model().objects.create_user(username='test'))
        c=Categoria.objects.create(nombre='Prueba');Producto.objects.create(nombre='Cable',categoria=c,precio=5,stock=2,minimo=5)
    def test_dashboard(self):
        r=self.client.get('/');self.assertContains(r,'Cable')
        self.assertEqual('Exportar PDF' in r.content.decode(),settings.ENABLE_REPORTS)
        self.assertEqual('Alertas de stock' in r.content.decode(),settings.ENABLE_NOTIFICATIONS)
    def test_optional_routes(self):
        r=self.client.get('/reportes/pdf/');self.assertEqual(r.status_code,200 if settings.ENABLE_REPORTS else 404)
        r=self.client.get('/alertas/');self.assertEqual(r.status_code,200 if settings.ENABLE_NOTIFICATIONS else 404)
        if settings.ENABLE_NOTIFICATIONS: self.assertContains(r,'Cable')
