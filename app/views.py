from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app import models
from app import serializers


#定义继承类 API
class BookAPIView(APIView):
    def get(self,request):

        book =models.BookInfo.objects.all()
        ser = serializers.BookInfoSerializer(book,many=True)

        return Response(ser.data)


    def post(self,request):
        data_dict = request.data
        print(data_dict)
        #进行序列化
        ser = serializers.BookInfoSerializer(data = data_dict)

        #进行序列化数据校验
        ser.is_valid(raise_exception=True)
        #进行数据入库
        ser.save()
        return Response(ser.data)

class BookDetialApiView(APIView):
    def get(self,request,id):
        book = models.BookInfo.objects.get(id=id)

        ser = serializers.BookInfoSerializer(instance=book)

        return Response(ser.data,status.HTTP_200_OK)

    def put(self,request,id):
        book = models.BookInfo.objects.get(id=id)
        data_dict = request.data
        ser = serializers.BookInfoSerializer(instance=book,data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data,status.HTTP_201_CREATED)

    def delete(self,request,id):
        models.BookInfo.objects.get(id=id).delete()

        return Response(status.HTTP_204_NO_CONTENT)


"""
二级视图GenericAPIView
"""
from rest_framework.generics import GenericAPIView

class BookGen(GenericAPIView):

    #公共属性
    queryset = models.BookInfo.objects.all()
    serializer_class = serializers.BookInfoSerializer

    def get(self,request):

        books = self.get_queryset()

        ser = self.get_serializer(instance=books,many=True)

        return Response(ser.data)

    def post(self,request):
        data_dict = request.data

        ser = self.get_serializer(data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()

        return Response(ser.data,status.HTTP_201_CREATED)

class BookDeGen(GenericAPIView):

    #公告属性
    queryset = models.BookInfo.objects.all()
    serializer_class = serializers.BookInfoSerializer

    lookup_url_kwarg = 'pk'

    def get(self,req,pk):
        book = self.get_object()

        ser = self.get_serializer(instance=book)
        return Response(ser.data,status.HTTP_200_OK)

    def put(self,req,pk):
        data_dict = req.data
        book = self.get_object()

        ser = self.get_serializer(instance=book,data = data_dict)

        ser.is_valid()
        ser.save()
        return Response(ser.data,status.HTTP_201_CREATED)

    def delete(self,req,pk):
        self.get_object().delete()

        return Response(status.HTTP_404_NOT_FOUND)























