from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from blogpost import views as blogpostViews


urlpatterns = [
               url(r'^$', blogpostViews.index, name='main'),
               url(r'^blog/(?P<slug>[^\.]+).html', blogpostViews.view_post, name='view_blog_post'),
               url(r'^admin/', include(admin.site.urls))
               ]
