from django.urls import path
from users import views

urlpatterns = [
    # path('',views.AllStatusList.as_view()),
    # path('<int:id>',views.StatusDetailView.as_view()),
    # path('create',views.StatusCreate.as_view()),
    # path('update/<int:id>',views.StatusUpdateView.as_view()),
    # path('delete/<int:id>',views.StatusDelete.as_view())
    path('',views.StatusListCreateView.as_view()),
    path('<int:id>',views.StatusRetriveDestroyUpdateView.as_view())


]

