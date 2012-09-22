from .views import home, blog, post, events, event, aboutus, projects,members,member

from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', home, name='public_home'),
    url(r'^public/blog$', blog, name='public_blog'),
    url(r'^public/blog/post/(\d+)$', post, name='public_post'),
    url(r'public/events/(\w+)$', events, name='public_events'),
    url(r'public/projects/$', projects, name='public_projects'),
    url(r'public/members/$', members, name='public_members'),
    url(r'public/member/(\d+)$', member, name='public_profile'),
    url(r'public/event/(\d+)$', event, name='solo_event'),
    url(r'^public/about$', aboutus, name='public_about'),
)
