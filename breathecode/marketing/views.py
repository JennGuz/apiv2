import os
from urllib import parse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from breathecode.utils import APIException
from .serializers import PostFormEntrySerializer
from .actions import register_new_lead, sync_tags, sync_automations, get_facebook_lead_info
from .tasks import persist_single_lead, update_link_viewcount
from .models import ShortLink, ActiveCampaignAcademy


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def create_lead(request):
    serializer = PostFormEntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        persist_single_lead.delay(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def receive_facebook_lead(request):
    if request.method == 'GET':

        challenge = 'no challenge'
        if 'hub.challenge' in request.GET:
            challenge = request.GET['hub.challenge']
        
        verify_token = ''
        if 'hub.verify_token' in request.GET:
            verify_token = request.GET['hub.verify_token']

        mode = ''
        if 'hub.mode' in request.GET:
            mode = request.GET['hub.mode']

        if verify_token == os.getenv("FACEBOOK_VERIFY_TOKEN", ""):
            return Response(int(challenge), status=status.HTTP_200_OK)
        else:
            return Response(int(challenge), status=status.HTTP_400_BAD_REQUEST)
    else:
        print(request.data)
        if "object" in request.data:
            if request.data["object"] == "page":
                for entry in request.data["entry"]:
                    for changes in entry["changes"]:
                        if changes["field"] == "leadgen":
                            serializer = PostFormEntrySerializer(data={
                                "fb_leadgen_id": changes["value"]["leadgen_id"],
                                "fb_page_id": changes["value"]["page_id"],
                                "fb_form_id": changes["value"]["form_id"],
                                "fb_adgroup_id": changes["value"]["adgroup_id"],
                                "fb_ad_id": changes["value"]["ad_id"]
                            })
                            if serializer.is_valid():
                                serializer.save()
                                #persist_single_lead.delay(request.data)
                                return Response(serializer.data, status=status.HTTP_201_CREATED)
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"details": "No leads found"}, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
@api_view(['GET'])
def sync_tags_with_active_campaign(request, academy_id):
    
    academy = ActiveCampaignAcademy.objects.filter(academy__id=academy_id).first()
    if academy is None:
        raise APIException('Academy not found')

    tags = sync_tags(academy)
    return Response(tags, status=status.HTTP_200_OK)

# Create your views here.
@api_view(['GET'])
def sync_automations_with_active_campaign(request, academy_id):
    
    academy = ActiveCampaignAcademy.objects.filter(academy__id=academy_id).first()
    if academy is None:
        raise APIException('Academy not found')

    tags = sync_automations(academy)
    return Response(tags, status=status.HTTP_200_OK)

def redirect_link(request, link_slug):
    short_link = ShortLink.objects.filter(slug=link_slug, active=True).first()
    if short_link is None:
        return HttpResponseNotFound("URL not found")

    update_link_viewcount.delay(short_link.slug)

    params = {}
    if short_link.utm_source is not None:
        params["utm_source"] = short_link.utm_source
    if short_link.utm_content is not None:
        params["utm_content"] = short_link.utm_content
    if short_link.utm_medium is not None:
        params["utm_medium"] = short_link.utm_medium
    if short_link.utm_campaign is not None:
        params["utm_campaign"] = short_link.utm_campaign

    destination_params = {}
    url_parts = short_link.destination.split('?')
    if len(url_parts) > 1:
        destination_params = dict(parse.parse_qsl(url_parts[1]))
    
    params = { **destination_params, **params }
    return HttpResponseRedirect(redirect_to=url_parts[0]+"?"+parse.urlencode(params))