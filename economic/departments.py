from economic.query import QueryMixin
from economic.serializer import EconomicSerializer


class DepartmentSerializer(EconomicSerializer):
    id_property_name = 'department_number'


class Department(DepartmentSerializer, QueryMixin):
    base_url = "https://restapi.e-conomic.com/departments/"
