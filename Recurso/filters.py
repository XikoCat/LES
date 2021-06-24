from .models import Sala

import django_filters

class orderFilter(django_filters.FilterSet):
    class Meta:
        model = Sala
        fields = '__all__'