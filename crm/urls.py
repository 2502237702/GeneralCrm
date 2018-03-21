
from django.conf.urls import url, include
from crm import views
from rest_framework import routers
from crm.rest_views import UserViewSet, RoleViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    url(r'^$', views.sales_dashboard, name="crm_dashboard"),
    url(r'^customers/$', views.customers, name="customers"),
    url(r'^customers/change/(\d+)/$', views.customer_change, name="customer_change"),
    url(r'^my_customers/$', views.my_customers, name="my_customers"),
    url(r'^sales_report/$', views.sales_report, name="sales_report"),
    url(r'^enrollment/(\d+)/$', views.enrollment, name="enrollment"),
    url(r'^enrollment/stu/(\d+)/$', views.stu_enrollment, name="stu_enrollment"),

    # restframework实例应用
    url(r'^myframe/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
