# Google-calender-intregation-With-Django
Hi All
In This application i got to know about google integration with python i have used 2 modules by google are:-
1.google-apis-oauth-django 
2.google-api-python-client
This modules are google provided standard library for more information you read this documentation https://developers.google.com/calendar/api/v3/reference

I have intregated through Django app and It return all the listed events When user authorize
Note:- You can only authorize if you are test your. I mean i have to add you as test user using google cloud console for acessing this application

My app screen has two Button on home one to refresh another to authorize:-
![Screenshot (4)](https://user-images.githubusercontent.com/74177655/178114215-d4acd71e-0436-4589-8bef-ae7652ec9300.png)

Once The user refresh the page and click authorize with google it will redirect automatically google consent screen to authorize 
![Screenshot (5)](https://user-images.githubusercontent.com/74177655/178114292-ffbde39c-d5cb-421f-b404-5eb7bb2f4fbf.png)

once the user authorize sucessfully it will return the list of events in first caleder the user have like given in below picture

![Screenshot (6)](https://user-images.githubusercontent.com/74177655/178114928-dbac6333-868d-412c-80b9-0951a2883c2a.png)

