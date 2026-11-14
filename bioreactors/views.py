from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import (
    AlgaeSpeciesForm,
    BioreactorUnitForm,
    BioreactorUpdateForm,
    EquipmentForm,
)
from .models import AlgaeSpecies, BioreactorUnit, Equipment


class AlgaeSpeciesListView(ListView):
    model = AlgaeSpecies
    template_name = 'bioreactors/algae_list.html'
    context_object_name = 'algae_list'


class AlgaeSpeciesCreateView(CreateView):
    model = AlgaeSpecies
    form_class = AlgaeSpeciesForm
    template_name = 'bioreactors/algae_form.html'
    success_url = reverse_lazy('algae_list')


class AlgaeSpeciesUpdateView(UpdateView):
    model = AlgaeSpecies
    form_class = AlgaeSpeciesForm
    template_name = 'bioreactors/algae_form.html'
    success_url = reverse_lazy('algae_list')


class AlgaeSpeciesDeleteView(DeleteView):
    model = AlgaeSpecies
    template_name = 'bioreactors/algae_confirm_delete.html'
    success_url = reverse_lazy('algae_list')


class EquipmentListView(ListView):
    model = Equipment
    template_name = 'bioreactors/equipment_list.html'
    context_object_name = 'equipment_list'


class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'bioreactors/equipment_form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'bioreactors/equipment_form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'bioreactors/equipment_confirm_delete.html'
    success_url = reverse_lazy('equipment_list')


class BioreactorListView(ListView):
    model = BioreactorUnit
    template_name = 'bioreactors/bioreactor_list.html'
    context_object_name = 'bioreactors'

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search', '').strip()
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(algae_species__name__icontains=search_query)
            )

        sort_by = self.request.GET.get('sort', '')
        if sort_by == 'name':
            queryset = queryset.order_by('name')
        elif sort_by == 'newest':
            queryset = queryset.order_by('-setup_date')
        elif sort_by == 'oldest':
            queryset = queryset.order_by('setup_date')

        return queryset


class BioreactorDetailView(DetailView):
    model = BioreactorUnit
    template_name = 'bioreactors/bioreactor_detail.html'
    context_object_name = 'bioreactor'


class BioreactorCreateView(CreateView):
    model = BioreactorUnit
    form_class = BioreactorUnitForm
    template_name = 'bioreactors/bioreactor_form.html'
    success_url = reverse_lazy('bioreactor_list')


class BioreactorUpdateView(UpdateView):
    model = BioreactorUnit
    form_class = BioreactorUpdateForm
    template_name = 'bioreactors/bioreactor_form.html'
    success_url = reverse_lazy('bioreactor_list')


class BioreactorDeleteView(DeleteView):
    model = BioreactorUnit
    template_name = 'bioreactors/bioreactor_confirm_delete.html'
    success_url = reverse_lazy('bioreactor_list')