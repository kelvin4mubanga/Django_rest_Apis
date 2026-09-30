from rest_framework import generics
from .models import Poll, PollOption, Vote
from .serializers import PollSerializer, PollOptionSerializer, VoteSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollOptionList(generics.ListCreateAPIView):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer


class PollOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer


class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer