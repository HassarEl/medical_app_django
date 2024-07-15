from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('patients/', views.patients, name='patients'),
    path('patients/ajouter', views.add_patients, name='add_patients'),
    path('patients/ajoute', views.add_pat, name='add_pat'),
    path('patients/update/<int:id>', views.update_pat, name='update_pat'),
    path('patients/updat/<int:id>', views.update_p, name='update_p'),
    path('patients/delete/<int:id>', views.patient_drop, name='delet_pat'),
    path('patients/<int:pk>', views.view_patients, name='view_patients'),

    path('rdv', views.rdv, name='rdv'),
    path('rdv/<int:pk>', views.view_rdv, name='veiw_rdv'),
    path('rdv/ajouter', views.add_rdv, name='add_rdv'),
    path('rdv/ajoute', views.add_r, name='add_r'),
    path('rdv/update/<int:id>', views.update_rdv, name='update_rdv'),
    path('rdv/updat/<int:id>', views.updat_rdv, name='updat_rdv'),

    path('rdv/delete/<int:id>', views.rdv_drop, name='delet_rdv'),

    path('ordonnance/', views.ordonnancee, name='ordonnance'),
    path('ordonnance/voire/<int:id>', views.view_ord, name='view_ord'),
    path('ordonnance/ajouter', views.add_ord, name='add_ord'),
    path('ordonnance/ajoute', views.add_o, name='add_o'),
    path('ordonnance/delete/<int:id>', views.delete_ord, name='delete_ord'),
]
