# from asyncio import exceptions
import datetime
from django.shortcuts import render, HttpResponseRedirect, redirect
import google_apis_oauth
import os
from googleapiclient.discovery import build

from  django.core import exceptions 



from google_auth_oauthlib.flow import InstalledAppFlow
import pickle


SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.readonly']



JSON_FILEPATH = os.path.join(os.getcwd(), 'client_secret_503635821248-hkfsriho2hdfjkm6ein3ejkncjr8enqr.apps.googleusercontent.com.json')

REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'



def home(request):
    flow = InstalledAppFlow.from_client_secrets_file("client_secret_503635821248-hkfsriho2hdfjkm6ein3ejkncjr8enqr.apps.googleusercontent.com.json", scopes=SCOPES)
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return render(request, 'index.html', { 'flow': oauth_url})



# def RedirectOauthView(request):
#     oauth_url = google_apis_oauth.get_authorization_url(
#         JSON_FILEPATH, SCOPES, REDIRECT_URI)
#     return HttpResponseRedirect(CallbackView)


creds = None
def CallbackView(request):
    try:
        credentials = google_apis_oauth.get_crendentials_from_callback(request,JSON_FILEPATH,SCOPES,REDIRECT_URI)

        pickle.dump(credentials, open("token.pkl", "wb"))
        credentials = pickle.load(open("token.pkl", "rb"))
        # creds, refreshed = google_apis_oauth.load_credentials(stringified_token)
        print(credentials)
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()
        events=result['items']
        return render(request, 'index.html', {'events': events})
        # return redirect('home')
        
        
    except:
        return redirect("home")
        

        
    
