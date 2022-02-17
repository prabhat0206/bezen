from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from bezen.models import Record
from .forms import RecordForm
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializer import RecordSerializer, UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class GetUserRecords(ListAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = request.user.record_set.all().order_by('-datetime')
        serialized = self.serializer_class(queryset, many=True)
        return Response(serialized.data)


class AddRecord(CreateAPIView):
    queryset = Record.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser, )
    
    def post(self, request):
        new_POST = dict()
        for data in request._request.POST:
            new_POST[data] = request._request.POST.get(data)
        new_POST['user']=request.user.id
        data = RecordForm(new_POST, request._request.FILES)
        if data.is_valid():
            data.save()
            return Response({"Success": True})
        return Response({"Success": False})


class UpdateRecord(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def update(self, request, id):
        instance = self.get_queryset().get(id=id)
        data_for_change = request.data
        serialized = self.serializer_class(instance, data=data_for_change, partial=True)
        if serialized.is_valid():
            self.perform_update(serialized)
            return Response({"Success": True, "data": serialized.data})
        return Response({"Success": False, "Errors": str(serialized.errors)})

