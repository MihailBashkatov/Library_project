# from django.http import HttpResponseForbidden
# from rest_framework import generics, status
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from books.models import Habit
# from books.paginators import MyPagination
# from books.permissions import IsOwner
# from books.serializers import HabitSerializer
#
#
# class HabitCreateAPIView(generics.CreateAPIView):
#     """View to create a habit"""
#
#     serializer_class = HabitSerializer
#     permission_classes = [IsOwner, IsAuthenticated]
#
#     def perform_create(self, serializer):
#         """Adding logic to get user, who is creating a habit"""
#         serializer.save(habit_user=self.request.user)
#
#
# class HabitsListAPIView(generics.ListAPIView):
#     """View to create a list of public books"""
#
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.filter(habit_is_public=True)
#
#     # access for all users
#     permission_classes = [
#         IsAuthenticated,
#     ]
#     pagination_class = MyPagination
#
#     def get(self, request, **kwargs):
#         """Adding logic for pagination"""
#         queryset = Habit.objects.filter(habit_is_public=True)
#         paginated_queryset = self.paginate_queryset(queryset)
#         serializer = HabitSerializer(paginated_queryset, many=True)
#         return self.get_paginated_response(serializer.data)
#
#
# class HabitsUserListAPIView(generics.ListAPIView):
#     """View to create a list of books for particular user"""
#
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()
#     permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
#     pagination_class = MyPagination
#
#     def get_queryset(self):
#
#         return Habit.objects.filter(habit_user=self.request.user)
#
#     def get(self, request, **kwargs):
#         """Adding logic for pagination"""
#         queryset = Habit.objects.filter(habit_user=self.request.user)
#         paginated_queryset = self.paginate_queryset(queryset)
#         serializer = HabitSerializer(paginated_queryset, many=True)
#         return self.get_paginated_response(serializer.data)
#
#
# class HabitRetreiveAPIView(generics.RetrieveAPIView):
#     """View to get a particular habit for the user"""
#
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()
#     permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
#
#
# #
# #
# class HabitUpdateAPIView(generics.UpdateAPIView):
#     """View to update a particular habit for the user"""
#
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()
#     permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
#
#
# class HabitDestroyAPIView(generics.DestroyAPIView):
#     """View to delete a particular habit for the user"""
#
#     queryset = Habit.objects.all()
#     permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
#
#
# class PublicAPIView(APIView):
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()
#
#     def post(self, view, pk):
#         """ View to make the habit publicly available or unavailable
#             only for the user of the habit."""
#         message = ""
#
#         if Habit.objects.filter(
#             pk=pk, habit_user=self.request.user
#         ).exists():  # In case if habit belongs to particular user
#
#             habit = get_object_or_404(
#                 Habit, id=pk
#             )  # get a particular habit via request
#
#             if habit.habit_is_public:
#                 habit.habit_is_public = False
#                 habit.save()
#                 message = "Habit is not public anymore"
#
#             elif not habit.habit_is_public:
#                 habit.habit_is_public = True
#                 habit.save()
#                 message = "Habit is publicly available now"
#
#             return Response({"message": {message}}, status=status.HTTP_201_CREATED)
#         return HttpResponseForbidden(
#             "You do not have permission to change a status of public availability"
#         )
