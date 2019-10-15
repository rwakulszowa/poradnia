from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    url(r'^$', views.StatsIndexView.as_view(),
        name="index"),
    url(r'^api/sprawy/czas_reakcji$', views.StatsCaseReactionApiView.as_view(),
        name="case_reaction_api"),
    url(r'^api/sprawy/utworzone$', views.StatsCaseCreatedApiView.as_view(),
        name="case_created_api"),
    url(r'^api/sprawy/bez_odpowiedzi$', views.StatsCaseUnansweredApiView.as_view(),
        name="case_unanswered_api"),
    url(r'^api/listy/utworzone$', views.StatsLetterCreatedApiView.as_view(),
        name="letter_created_api"),
    url(r'^api/uzytkownicy/zarejestrowani$', views.StatsUserRegisteredApiView.as_view(),
        name="user_registered_api"),
    url(r'^render/sprawy/utworzone$', views.StatsCaseCreatedRenderView.as_view(),
        name="case_created_render"),
    url(r'^render/sprawy/czas_reakcji$', views.StatsCaseReactionRenderView.as_view(),
        name="case_reaction_render"),
    url(r'^render/sprawy/bez_odpowiedzi$', views.StatsCaseUnansweredRenderView.as_view(),
        name="case_unanswered_render"),
    url(r'^render/listy/utworzone$', views.StatsLetterCreatedRenderView.as_view(),
        name="letter_created_render"),
    url(r'^render/uzytkownicy/zarejestrowani$', views.StatsUserRegisteredRenderView.as_view(),
        name="user_registered_render"),
    url(r'^sprawy/utworzone$', views.StatsCaseCreatedView.as_view(),
        name="case_created"),
    url(r'^sprawy/czas_reakcji$', views.StatsCaseReactionView.as_view(),
        name="case_reaction"),
    url(r'^sprawy/bez_odpowiedzi$', views.StatsCaseUnansweredView.as_view(),
        name="case_unanswered"),
    url(r'^listy/utworzone$', views.StatsLetterCreatedView.as_view(),
        name="letter_created"),
    url(r'^uzytkownicy/zarejestrowani$', views.StatsUserRegisteredView.as_view(),
        name="user_registered"),
    url(_(r'^item-(?P<key>[\w\-.]+)/$'), views.ValueBrowseListView.as_view(),
        name="item_detail"),
    url(_(r'^item-(?P<key>[\w\-.]+)/(?P<month>\d+)/(?P<year>\d+)/~csv$'), views.CSVValueListView.as_view(),
        name="item_detail_csv"),
    url(_(r'^item-(?P<key>[\w\-.]+)/(?P<month>\d+)/(?P<year>\d+)/~json$'), views.JSONValueListView.as_view(),
        name="item_detail_json"),
    url(_(r'^item-(?P<key>[\w\-.]+)/(?P<month>\d+)/(?P<year>\d+)$'), views.ValueBrowseListView.as_view(),
        name="item_detail"),
    url(_(r'^graph-(?P<pk>\d+)$'), views.GraphDetailView.as_view(),
        name="graph_detail"),
    url(_(r'^graph-(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)$'), views.GraphDetailView.as_view(),
        name="graph_detail"),
    url(_(r'^graph-(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)/~json$'), views.JSONGraphDetailView.as_view(),
        name="graph_detail_json"),
]

app_name = 'poradnia.stats'