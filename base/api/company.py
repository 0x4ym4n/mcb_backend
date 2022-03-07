import json
import string
from random import random

import requests
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from urllib3 import poolmanager
import ssl

from baseproject import settings

from base.api.utils import company_data_post_request


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ctx)


def search_company(request):
    name = request.GET['name']
    country = request.GET['country']
    headers = {'ApiToken': '2H39b40660dd0893ec1180ea00155d124506',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://Orbis.bvdinfo.com/api/orbis/Companies/data?query={"WHERE":[{"MATCH":{"Criteria":{"Name":"%s","Country":"%s"}}}],"SELECT":["NAME","BVDID","CITY","Match.EmailOrWebsite","Match.ADDRESS"]}' % (name, country)
    s = requests.Session()
    s.mount('https://', TLSAdapter())
    r = s.get(url, headers=headers, timeout=30)
    print(r.content)
    return JsonResponse(r.json())


def get_company_data(request):
    bvDID = request.GET['bvDID']
    url = "https://Orbis.bvdinfo.com/api/orbis/Companies/data"
    headers = {'ApiToken': '2H39b40660dd0893ec1180ea00155d124506',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    s = requests.Session()
    s.mount('https://', TLSAdapter())

    response = s.post( url, headers=headers, data=company_data_post_request(bvDID))
    response = response.json()
    print(response)

    return JsonResponse(response["Data"][0])



def send_email(request):
    company_name = request.GET.get('company_name', '0')
    sender = request.GET.get('sender', '0')
    subject = company_name +  ': KYC Onboarding'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['0x4ym4n@gmail.com']
    html_content = render_to_string('templates_verify_email.html',
                                    {'sender': sender})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return JsonResponse({"status": "ok"})