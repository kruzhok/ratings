from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

