# from asyncio import exceptions
import datetime
from django.shortcuts import render, HttpResponseRedirect
import google_apis_oauth
import os
import google_apis_oauth
from googleapiclient.discovery import build

# from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

# Create your views here.

SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.readonly']

JSON_FILEPATH = os.path.join(os.getcwd(), 'client_secret_503635821248-hkfsriho2hdfjkm6ein3ejkncjr8enqr.apps.googleusercontent.com.json')
REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'
def home(request):
    scopes = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.readonly']
    flow = InstalledAppFlow.from_client_secrets_file("client_secret_503635821248-hkfsriho2hdfjkm6ein3ejkncjr8enqr.apps.googleusercontent.com.json", scopes=scopes)
    authorization_url= flow.authorization_url()[0]
    # credentials = flow.run_console()
    return render(request, 'index.html', { 'flow': authorization_url})

def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)




def CallbackView(request):
    try:

        # Get user credentials
        
        credentials = google_apis_oauth.get_crendentials_from_callback(
            request,
            JSON_FILEPATH,
            SCOPES,
            REDIRECT_URI,
           
        )
        print(credentials)
        return render(request, 'index.html')

    except :
        return render(request, 'index.html')

# def list_event(request):
#     service = build('calendar', 'v3', credentials=creds)
#     now = datetime.datetime.utcnow().isoformat() + 'Z'
#     print('Getting the upcoming 10 events')
#     events_result = service.events().list(
#         calendarId='primary', timeMin=now,
#         maxResults=10, singleEvents=True,
#         orderBy='startTime').execute()
#     events = events_result.get('items', [])

#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])
        
#     return render(request, 'index.html', {'event':event})

   