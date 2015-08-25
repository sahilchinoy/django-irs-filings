from django.conf.urls import include, url
from django.contrib import admin

from irs.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FilingListView.as_view(), name='filings'),
    url(r'^filings/(?P<filing_id>([0-9]+))/sa/$', SAView.as_view(), name='sa'),
    url(r'^filings/(?P<filing_id>([0-9]+))/sb/$', SBView.as_view(), name='sb'),
    url(r'^committee/(?P<EIN>([0-9]{9}))/$', CommitteeDetailView.as_view(), name='committee'),
]
