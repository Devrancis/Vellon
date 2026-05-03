from django.views.generic import TemplateView
from products.models import Product, Category

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(is_featured=True, is_active=True)[:8]
        context['categories'] = Category.objects.filter(parent=None)[:6]
        return context
