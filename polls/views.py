from django.contrib.auth import get_user_model
from django.http.response import JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TutorialSerializer,UseSerializer
from .models import Tutorial
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
#
# @api_view(['POST'])
# def createview(request):
#     if request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET'])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#
#
# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by Category': '/?category=category_name',
#         'Search by Subcategory': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
#     return Response(api_urls)
#
# @api_view(['GET'])
# def tutorial_detail(request, pk):
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#     except Tutorial.DoesNotExist:
#         return JsoPOSTnResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         tutorial_serializer = TutorialSerializer(tutorial)
#         return JsonResponse(tutorial_serializer.data)
#
# @api_view(['PATCH'])
# def patch_tut(request, pk):
#         if request.method == 'PATCH':
#             tutorial_data = JSONParser().parse(request)
#             tutmodel_object = Tutorial.objects.get(pk=pk)
#             serializer = TutorialSerializer(tutmodel_object, data=tutorial_data,
#                                              partial=True)  # set partial=True to update a data partially
#
#             if serializer.is_valid():
#                 serializer.save()
#                 s = serializer.data
#                 print(s)
#                 title = s["title"]
#                 print(title)
#                 return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#             return JsonResponse(code=400, data="wrong parameters")
#
# @api_view(['PUT'])
# def put_tut(request, pk):
#         if request.method == 'PUT':
#             tutorial_data = JSONParser().parse(request)
#             tutmodel_object = Tutorial.objects.get(pk=pk)
#             serializer = TutorialSerializer(tutmodel_object, data=tutorial_data,
#                                              partial=True)  # set partial=True to update a data partially
#
#             if serializer.is_valid():
#                 serializer.save()
#                 s = serializer.data
#                 print(s)
#                 title = s["title"]
#                 print(title)
#                 return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#             return JsonResponse(code=400, data="wrong parameters")
#
# @api_view(['DELETE'])
# def del_tut(request, pk):
#         if request.method == 'DELETE':
#             tutorial = Tutorial.objects.get(pk=pk)
#             tutorial.delete()
#             return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



class Tutuorialview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        snippets = Tutorial.objects.all()
        serializer = TutorialSerializer(snippets, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # def get(self, request):
        # content = {'message': 'Hello, GeeksforGeeks'}
        # return Response(content)

    def post(self, request, format=None):
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class tutuorialdetailedview(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Tutorial.objects.get(pk=pk)
        except Tutorial.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tut = self.get_object(pk)
        serializer = TutorialSerializer(tut)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TutorialSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"message":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)

class LoginView(APIView):
    permission_classes = (AllowAny,)

    # def post(self, request):
    #     serializer = UseSerializer(data=request.data)
    #     print("serializer")
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             print("hi")
    #             token = Token.objects.create(user=user)
    #             json = serializer.data
    #             json['token'] = token.key
    #             return Response(json, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request):
    #     User = get_user_model()
    #     users = User.objects.all()
    #     serializer = UseSerializer(users, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            phone_number = request.data["phone_number"]
            password = request.data["password"]
            User = get_user_model()
            user = User.objects.get(phone_number=phone_number)
            print("hi",user)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)
                return Response({"refresh":str(refresh),"access" : access}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "password is in correct"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"message":"user not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]
            User = get_user_model()
            user = User.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)
                print(str(refresh),"hi")
                return Response({"refresh":str(refresh),"access" : access}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"message":"user not found"}, status=status.HTTP_404_NOT_FOUND)

class UserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UseSerializer

    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]
        phone_number = request.data["phone_number"]
        username = request.data["username"]
        User = get_user_model()
        user = User.objects.create_user(email, password, phone_number,username)
        print(user,"user")
        return JsonResponse({"message":"user created successfully"}, status=status.HTTP_201_CREATED)


