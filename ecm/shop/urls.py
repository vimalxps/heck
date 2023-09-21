from django.urls import path
from . import views
# from . views import country_city_view
app_name='shop'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('/<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('redin/',views.redin,name='redin'),
    # path('sub_form/',views.sub_form,name='subf_form'),
    path('success/',views.success,name='success')



]



