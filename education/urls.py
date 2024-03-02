from django.urls import path

from education.apps import EducationConfig
from education.views import ProductCreateListAPIView, ProductView, LessonCreateListAPIView, LessonView, \
    GroupCreateListAPIView, GroupView

app_name = EducationConfig.name

urlpatterns = [
    path('product/create_list', ProductCreateListAPIView.as_view(), name='product/create_list'),
    # path('product/list/', ProductListAPIView.as_view(), name='product/list'),
    # path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product/get'),
    # path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product/update'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),

    path('lesson/create_list', LessonCreateListAPIView.as_view(), name='lesson/create_list'),
    path('lesson/<int:pk>/', LessonView.as_view(), name='lesson'),

    path('group/create_list', GroupCreateListAPIView.as_view(), name='group/create_list'),
    path('group/<int:pk>/', GroupView.as_view(), name='group')
]

