from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Make sure this file is in the same directory
def create_calendar_event(request):
    return {
        "summary": request.title,
        "description": request.description,
        "start": request.start_time,
        "end": request.end_time,
        "attendee": request.email
    }
'''
def create_calendar_event(data):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': data.title,
        'description': data.description,
        'start': {
            'dateTime': data.start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': data.end_time,
            'timeZone': 'Asia/Kolkata',
        },
        'attendees': [
            {'email': data.email},
        ],
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return created_event
'''