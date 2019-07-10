from django.shortcuts import render

# Create your views here.
def report_sertifikasi(request):
    return render(request, "reports/sertifikasi.html")