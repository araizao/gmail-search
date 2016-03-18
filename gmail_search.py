
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import gmail_list
import gmail_get_message

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser])
    flags.add_argument(
        '-q', '--query', type=str, help='Query string to search for.', 
        required=False, default='', nargs=1)
    flags.add_argument(
        '-n', '--nresults', type=int, help='Maximum number of results.', 
        required=False, default=10)

    args = flags.parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_subject(message):
    """

    """
    payload = message['payload']
    for header in payload['headers']:
        if header['name'] == 'Subject':
            subject = header['value']
            break

    return subject

def get_sender(message):
    """

    """
    payload = message['payload']
    for header in payload['headers']:
        if header['name'] == 'From':
            sender = header['value']
            break

    return sender

def get_date(message):
    """

    """
    payload = message['payload']
    for header in payload['headers']:
        if header['name'] == 'Date':
            date = header['value']
            break

    return date


def main():
    """Seaerch mail using the Gmail API.

    Creates a Gmail API service object and outputs a list of messages
    from the user's Gmail account with a specific query string
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    user_id = 'me'
    query = args.query
    max_results = args.nresults

    #results = listGmail.ListMessagesMatchingQuery(service, user_id, query)
    results = gmail_list.ListMessagesMatchingQueryMax(service, user_id, query, max_results)
    if not results:
        print('No messages found.')
    else:
        print('found ' +  str(len(results)) + ' messages.')
        for messages in results:
            mid = messages['id']
            message = gmail_get_message.GetMessage(service, user_id, mid)
            subject = get_subject(message)
            sender = get_sender(message)
            date = get_date(message)
            print('Date:    ' + date)
            print('Sender:  ' + sender)
            print('Subject: ' + subject)
            #print('\n')

        # count = 0
        # for messages in results:
        #     mid = messages['id']
        #     message = gmail_get_message.GetMessage(service, user_id, mid)
        #     count = count + 1
        #     #print('Message #' + str(count) + ' snippet: ' + message['snippet'])
        #     payload = message['payload']
        #     for header in payload['headers']:
        #         if header['name'] == 'Subject':
        #             subject = header['value']
        #             break
        #     if subject:
        #         print('Subject: ' + subject)



if __name__ == '__main__':
    main()