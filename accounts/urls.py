"""
Copyright(C) 2014, Stamus Networks
Written by Eric Leblond <eleblond@stamus-networks.com>

This file is part of Scirius.

Scirius is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Scirius is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Scirius.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^logout/$', views.logoutview, name='accounts_logout'),
    url(r'^login/(?P<target>.*)$', views.loginview, name='accounts_login'),
    url(r'^edit/(?P<action>.*)$', views.editview, name='accounts_edit'),
    url(r'^manage/user/(?P<user_id>.*)/$', views.manageuser, name='user'),
    url(r'^manage/user/(?P<user_id>.*)/(?P<action>.*)$', views.manageuseraction, name='accounts_useraction'),
    url(r'^manage/(?P<action>.*)$', views.manageview, name='accounts_manage'),
]
