from django.urls import path
#这里弄完后还要在整体的urls里设置一下
from apps.modules.cart.views import CartView, DeleteView
from apps.modules.user.views import Userapiview, Login, SetPassword
from apps.modules.commodity.views import CommodityView

urlpatterns = [
    path('user',Userapiview.as_view()),
    path('login',Login.as_view()),
    path('reset',SetPassword.as_view()),

    path('commodity',CommodityView.as_view()),

    path('addcart',CartView.as_view()),
    path('delcart',DeleteView.as_view())
]