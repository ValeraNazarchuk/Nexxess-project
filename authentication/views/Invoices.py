from django.shortcuts import render, redirect


def invoices(request):
    return render(request, "invoices/invoices.html")