from django.conf.urls import url
from django.conf import settings
from views import AppUserDetailView, CustomerListView, ProposalListView, ProposalDetailView

urlpatterns = [
    url(r'^customers/$', CustomerListView.as_view(), name="customers_list"),
    url(r'^proposals/$', ProposalListView.as_view(), name="proposals_list"),
    url(r'^(proposals/?P<slug>[\w-]+)/$', ProposalDetailView.as_view(), name="proposal_detail"),
    url(r'^(?P<slug>[\w-]+)/$', AppUserDetailView.as_view(), name="appuser_detail"),

]
