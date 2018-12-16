"""breaze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from neighbourhood.views import (YelpEventsView,
                                 
                                 YelpSearchView,
                                 YelpBusinessView,
                                 
                                 
                                 HazardList)

from real_estate.views import (AgentViewSet,
                               PropertyViewSet,
                               PropertyDetailViewSet,
                               PropertyViewCountViewSet,
                               PropertyUpdateCountViewSet,
                               PropertyMediaViewSet,
                               PropertyLocationViewSet,
                               PropertyTagViewSet,
                               FavPropertyViewSet,
                               BoardViewSet,
                               ListViewSet,
                               TagViewSet,
                               ThemeViewSet,
                               SavedSearchViewSet,
                               OpenHouseViewSet,
                               BHGeometryViewSet,
                               SearchHistoryViewSet)


from county_records.views import (CountyRecordViewSet, LienRecordViewSet)

from user.views import (UserViewSet,
                        UserTagViewSet,
                        QuestionViewSet,
                        ResetPasswordRequestView,
                        PasswordResetConfirmView,
                        PasswordResetChangeView,
                        UserUpdateView,
                        UserPartialUpdateView,
                        ConfirmAnswerView,
                        ConfirmTokenView,
                        GetQuestionView
                        )



from school.views import (SchoolViewSet,)



from admins.views import (BackupView,
                        ThemesViewSet,
                        ConfigurationViewSet,
                        PropertyFilterViewSet)

from django.views.generic import TemplateView
from user.auth import FacebookLogin, GoogleLogin, TwitterLogin

from user.tests import TestUserQuestionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'agents', AgentViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'favproperties', FavPropertyViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'tags', TagViewSet)
router.register(r'openhouse', OpenHouseViewSet)
router.register(r'geometries', BHGeometryViewSet)
router.register(r'configuration', ConfigurationViewSet)
router.register(r'theme', ThemesViewSet)
router.register(r'propertyFilter', PropertyFilterViewSet)
router.register(r'securityquestion', QuestionViewSet)
router.register(r'countyrecords', CountyRecordViewSet)
router.register(r'liens', LienRecordViewSet)



router.register(r'schools', SchoolViewSet, base_name='schools')



user_nested_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_nested_router.register(r'list', ListViewSet, base_name='lists')
user_nested_router.register(r'searches', SavedSearchViewSet, base_name='searches')
user_nested_router.register(r'searches_history', SearchHistoryViewSet, base_name='searches_history')
user_nested_router.register(r'tags', UserTagViewSet, base_name='tags')

properties_nested_router = routers.NestedSimpleRouter(router, r'properties', lookup='property')
properties_nested_router.register(r'media', PropertyMediaViewSet, base_name='media')
properties_nested_router.register(r'detail', PropertyDetailViewSet, base_name='detail')
properties_nested_router.register(r'location', PropertyLocationViewSet, base_name='location')
properties_nested_router.register(r'tags', PropertyTagViewSet, base_name='tags')

properties_nested_router.register(r'views', PropertyViewCountViewSet, base_name='views')
properties_nested_router.register(r'update_views', PropertyUpdateCountViewSet, base_name='update_views')


favproperties_nested_router = routers.NestedSimpleRouter(router, r'favproperties', lookup='favproperty')
boards_nested_router = routers.NestedSimpleRouter(router, r'boards', lookup='boards')


urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^', include(router.urls)),
    url(r'^', include(properties_nested_router.urls)),
    url(r'^', include(favproperties_nested_router.urls)),
    url(r'^', include(boards_nested_router.urls)),
    url(r'^', include(user_nested_router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^successful_logout/$', TemplateView.as_view(template_name='rest_framework/successful_logout.html'), name='successful_logout'),
    url(r'^auth/register/', include('rest_auth.registration.urls')),
    url(r'^auth/google/$', GoogleLogin.as_view(), name='google_login'),
    url(r'^auth/facebook/$', FacebookLogin.as_view(), name='facebook_login'),
    url(r'^auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^account/reset_password', ResetPasswordRequestView.as_view(), name="reset_password"),
    url(r'^account/password_reset_confirm', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^account/password_reset_change', PasswordResetChangeView.as_view(), name='password_reset_change'),
    url(r'^user/update/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^user/update-partial/(?P<pk>\d+)/$', UserPartialUpdateView.as_view(), name='user_partial_update'),
    url(r'^noaa/', HazardList.as_view()),
    url(r'^backup_config$', BackupView.as_view(), name='backup_config'),
    url(r'^events/', YelpEventsView.as_view()),
    url(r'^search/', YelpSearchView.as_view()),
    url(r'^business/', YelpBusinessView.as_view()),
    url(r'^user/confirm_token/$', ConfirmTokenView.as_view(), name='user_token_confirmation'),
    url(r'^user/confirm_answer/$', ConfirmAnswerView.as_view(), name='user_confirmation'),
    url(r'^user/get_question/$', GetQuestionView.as_view(), name='user_get_question'),
    url(r'^test/(?P<pk>\d+)/answer=(?P<answer>\w+)/$', TestUserQuestionViewSet.as_view(), name='testanswer'),
    url(r'^securityquestion/$', QuestionViewSet.as_view({'get' : 'list'}), name='questions'),

]
