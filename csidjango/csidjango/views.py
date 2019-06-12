from django.views.generic import TemplateView, ListView, View
from process.models import *
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = "index.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class Error404View(TemplateView):
    template_name = "page_404.html"

# class UserListView(ListView):
# 	template_name = "lists/user.html"
# 	context_object_name = 'users'
# 	queryset = User.objects.all().order_by('id')

# class MultiListView(View):
#     template_name ="sidebar_dashboard.html"
#     context_object_name = 'list1'
#     context_object_name2 = 'list2'
#     context_object_name3 = 'list3'

#     def get(self, request, *args, **kwargs):
#         list1 = Types.objects.all()
#         list2 = Types.objects.all()
#         list3 = Types.objects.all()
#         return render(request, 'sidebar_dashboard.html', {'list1':list1, 'list2':list2, 'list3':list3})

# class MultiListView(View):
#     def get(self, request, *args, **kwargs):
#         list1 = Types.objects.all().order_by('id')
#         list2 = Types.objects.all().order_by('id')
#         list3 = Types.objects.all().order_by('id')
#         return render(request, 'list.html', {'list1':list1, 'list2':list2, 'list3':list3})

# class IndexView(generic.ListView):
#   template_name = 'expcore/index.html'
#   model = Activity
#   context_object_name = 'activities_list'
#   queryset = Activity.objects.all()
  

#   def get_context_data(self, **kwargs):
#     context = super(IndexView, self).get_context_data(**kwargs)
#     context['interviews_list'] = Interview.objects.all()
#     return context

# class BookListView(View):
# 	def get(self, request, *args, **kwargs):
# 		books = Book.objects.all()
# 		return render(request, "book-list.html", {'books': books})

# class BookListView(ListView):
# 	template_name = 'book-list.html'
# 	queryset = Book.objects.all()
# 	context_object_name = 'books'

# class MultiListView(View):
#     def get(self, request, *args, **kwargs):
#         list1 = Types.objects.all().order_by('id')
#         list2 = Types.objects.all().order_by('id')
#         list3 = Types.objects.all().order_by('id')
#         return render(request, 'list.html', {'list1':list1, 'list2':list2, 'list3':list3})

# class BookListView(ListView):
# 	template_name = 'book-list.html'
# 	queryset = Book1.objects.all(), Book2.objects.all()
# 	context_object_name = 'books1', 'books2'