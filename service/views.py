from django.views.generic.base import TemplateView
from django.views.generic import ListView
from service.models import Service, ServiceCategory
from user.models import MasterService
# Create your views here.

class IndexView(TemplateView):
    template_name = 'service/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Домашня сторінка'
        return context


class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список Послуг'
        context['categories'] = ServiceCategory.objects.all()

        category_id = self.request.GET.get('category_id')
        if category_id and category_id.isdigit():
            context['curent_category'] = ServiceCategory.objects.filter(id=category_id).first()
        return context


class MasterServiceListView(ListView):
    model = MasterService
    template_name = 'service/master_service_list.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Список майстрів'
            return context