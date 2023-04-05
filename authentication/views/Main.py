from django.shortcuts import render, redirect
import requests
import json


def main(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    else:
        # виведення інформації про новий інвойс чи нову задачу, який отримав вебхук бітрікса
        url = "https://apps.devplace.info/client_apps/nexxess/webhook.php"
        get_request = requests.get(url)
        webhook = get_request.text
        info = json.loads(webhook)
        if(info['event'] == 'ONCRMINVOICEADD'): # invoice
            invoice_url = "https://b24-hx1f8l.bitrix24.eu/rest/1/36b359umrza782tx/crm.invoice.get/?id=" + info['data']['FIELDS']['ID']
            invoice_request = requests.get(invoice_url)
            invoice_info = invoice_request.text
            if request.user.is_superuser:
                invoice = json.loads(invoice_info)
            else:
                invoice = "you are not admin"

        res = {
            'webhook': info['event'],
            'invoice': invoice
        }
        return render(request, "main.html", res)