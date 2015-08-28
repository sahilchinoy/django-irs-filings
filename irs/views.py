from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from irs.models import F8872, Contribution, Expenditure, Committee

class FilingListView(ListView):
    model = F8872
    template_name = "irs/filing_list.html"
    paginate_by = 10
    queryset = F8872.objects.exclude(is_amended=True)

class SAView(ListView):
    model = Contribution
    template_name = "irs/sa_list.html"

    def get_queryset(self, **kwargs):
        return Contribution.objects.filter(
            form_id_number=self.kwargs['filing_id'])

    def get_context_data(self, **kwargs):
        context = super(SAView, self).get_context_data(**kwargs)
        EIN = F8872.objects.get(form_id_number=self.kwargs['filing_id']).EIN
        context['EIN'] = EIN
        committee_name = Committee.objects.get(EIN=EIN).name
        context['committee_name'] = committee_name
        context['filing_id'] = self.kwargs['filing_id']
        return context

class SBView(ListView):
    model = Expenditure
    template_name = "irs/sb_list.html"

    def get_queryset(self, **kwargs):
        return Expenditure.objects.filter(
            form_id_number=self.kwargs['filing_id'])

    def get_context_data(self, **kwargs):
        context = super(SBView, self).get_context_data(**kwargs)
        EIN = F8872.objects.get(form_id_number=self.kwargs['filing_id']).EIN
        context['EIN'] = EIN
        committee_name = Committee.objects.get(EIN=EIN).name
        context['committee_name'] = committee_name
        context['filing_id'] = self.kwargs['filing_id']
        return context

class CommitteeDetailView(DetailView):
    """
    Information about a specific committee.
    """
    model = Committee
    slug_url_kwarg = 'EIN'
    slug_field = 'EIN'