from django.shortcuts import render
from django.views import View
# Create your views here.
from datetime import datetime
from .serializers import CommentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class MyApiView(View):
    def get(self, request):
        c1 = Comment(email='lokesh.rapala@gmail.com',
                     content='python django django rest framework')
        c2 = Comment('abclokesh@gmail.com', content='odoo')
        c3 = Comment('xyzlokesh@gmail.com', content='datascience')
        all_comments = [c1, c2, c3]
        cs1 = CommentSerializer(all_comments, many=True)
        return HttpResponse(JSONRenderer().render(cs1.data), content_type="application/json")

