import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs= PageVisit.objects.all()
    page_qs= PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
     #    "queryset": queryset
        "page_vigit_count":page_qs.count(),
        "total_visit_count":qs.count()
    }
    path=request.path
    print(path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

# Uncommented code for old_home_page_view
# def old_home_page_view(request, *args, **kwargs):
#     print(this_dir)
#     html_ = ""
#     html_file_path = this_dir / "home.html"
#     html_ = html_file_path.read_text()
#     return HttpResponse(html_)
