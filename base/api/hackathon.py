import uuid

import requests
from django.core.files.base import ContentFile
from django.http import JsonResponse

from base.models import Profile


def register_person(request):
    name = request.GET['name']
    email = request.GET['email']
    nationality = request.GET['nationality']
    data = request.GET['data']
    face_id = request.GET['face_id']
    image_id = request.GET['image_id']
    person = Profile()
    person.name = name
    person.email = email
    person.nationality = nationality
    person.face_id = face_id
    person.data = data

    try:
        person.face.save(str(uuid.uuid4()) + ".jpeg", ContentFile(saveImage(getImageToken(), image_id)), save=True)
        it2 = get_image_it2(person.face.url)
        string_ints = [str(int) for int in it2]
        str_of_ints = ",".join(string_ints)
        person.it2 = str_of_ints
    except:
        return JsonResponse({"message": "already exist"}, status=404)
    return JsonResponse({"status": "ok"})


def get_face_id(request):
    email = request.GET['email']
    profile = Profile.objects.filter(email=email)
    if profile:
        return JsonResponse({"status": "ok", "data": {"faceID": profile[0].face_id}})
    else:
        return JsonResponse({"message": "not found"}, status=404)


def perform_login(request):
    email = request.GET['email']
    image_id = request.GET['image_id']
    profile = Profile.objects.filter(email=email)
    if profile:
        profile[0].face_tmp.save(str(uuid.uuid4()) + ".jpeg", ContentFile(saveImage(getImageToken(), image_id)),
                                 save=True)
        it2_a = [int(i) for i in profile[0].it2.split(',')]
        it2_b = get_image_it2(profile[0].face_tmp.url)
        match = it2_compare(it2_a, it2_b)
        if match:
            data = {}
            data["name"] = profile[0].name
            data["nationality"] = profile[0].nationality
            data["email"] = profile[0].email
            data["data"] = profile[0].data
            data["face"] = "http://aayez.com:888" + profile[0].face.url
            return JsonResponse({"status": "ok", "data": data})
        else:
            return JsonResponse({"message": "face is not matching"}, status=404)

    else:
        return JsonResponse({"message": "not found"}, status=404)


def saveImage(token, face_id):
    url = "https://id.dev.uqudo.io/api/v1/info/img/" + str(face_id)

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + str(token)
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.content)
    return response.content


def getImageToken():
    url = 'https://auth.dev.uqudo.io/api/oauth/token'
    myobj = {'grant_type': 'client_credentials', 'client_id': '90dd6963-5be6-4655-a978-a6abf8e92a66',
             'client_secret': '3hbBAFzNaY86Z2wj6nHo2xMD'}
    x = requests.post(url, data=myobj)
    data = x.json()
    return data["access_token"]


def truststamp_token():
    url = 'https://api-stg.truststamp.net/api-token-auth/'
    myobj = {'username': 'ilabs', 'password': '05#f!N^L3Xull&Ey',
             'client_secret': '3hbBAFzNaY86Z2wj6nHo2xMD'}

    x = requests.post(url, data=myobj)

    print(x.text)
    data = x.json()
    return data["token"]


def get_image_it2(image):
    token = truststamp_token()
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
    }
    url = 'https://api-stg.truststamp.net/api/v2/proxy/bhash/encode/'
    myobj = {'media_url': "http://aayez.com:888" + image,
             "UUID": str(uuid.uuid4()),
             "return_now": True}

    x = requests.post(url, json=myobj, headers=headers)

    print(x.text)
    data = x.json()
    re = (convert_to_it2(data["data"]["bhash"], token))
    return re


def convert_to_it2(bhash, token):
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
    }
    url = 'https://api-stg.truststamp.net/api/v2/proxy/it2/translate/forward/'
    myobj = {'bhash': bhash,
             "UUID": str(uuid.uuid4()),
             "return_now": True}

    x = requests.post(url, json=myobj, headers=headers)

    print(x.text)
    data = x.json()
    print(data["data"])
    return data["data"]


def it2_compare(it2_a, it2_b):
    headers = {
        'Authorization': 'JWT ' + truststamp_token(),
        'Content-Type': 'application/json',
    }
    url = 'https://api-stg.truststamp.net/api/v2/proxy/it2/compare/'
    myobj = {'token_a': it2_a, 'token_b': it2_b,
             "UUID": str(uuid.uuid4()),
             "return_now": True}
    print(myobj)

    x = requests.post(url, json=myobj, headers=headers)

    print(x.text)
    data = x.json()
    return data["data"]["face_match"]
