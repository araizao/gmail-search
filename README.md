## gmail-search

Experimenting with Gmail API with Python

NOTE: these scripts are still in work and can only do so much

These python scripts will search through your own gmail account using a query statement.

##### Setup:

The environment was setup using Googles API Quickstart Guide: 
https://developers.google.com/gmail/api/quickstart/python#prerequisites

Google APIs use the OAuth 2.0 protocol for authentication and authorization, so in the guide above you must set up OAuth2.0 with your project. It was very easy and straightforward for me as Google gives pretty good instructions in walking you through the setup. 

##### Usage:
```
usage: gmail_search.py [-h] [--auth_host_name AUTH_HOST_NAME]
                       [--noauth_local_webserver]
                       [--auth_host_port [AUTH_HOST_PORT [AUTH_HOST_PORT ...]]]
                       [--logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                       [-q QUERY] [-n NRESULTS]

optional arguments:
  -h, --help            show this help message and exit
  --auth_host_name AUTH_HOST_NAME
                        Hostname when running a local web server.
  --noauth_local_webserver
                        Do not run a local web server.
  --auth_host_port [AUTH_HOST_PORT [AUTH_HOST_PORT ...]]
                        Port web server should listen on.
  --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level of detail.
  -q QUERY, --query QUERY
                        Query string to search for.
  -n NRESULTS, --nresults NRESULTS
                        Maximum number of results.
```

##### Example:

Queries through your email and finds up to a maximum of 3 messages that contain "*topcoder.com" (note the wildcard is accepted) in the message. Returns raw information about the emails it finds and parses to display (currently only displaying date, sender, and subject).

###### Output:
```
$ python gmail_search.py -n 3 -q *topcoder.com
found 3 messages.
Date:    Mon, 14 Mar 2016 08:33:33 -0500 (CDT)
Sender:  The topcoder team <no-reply@topcoder.com>
Subject: Important Update: Harvard Atrocity Prevention 2 Marathon Match - Date Has Moved!
Date:    Sun, 13 Mar 2016 16:51:13 -0500 (CDT)
Sender:  The topcoder team <no-reply@topcoder.com>
Subject: New Harvard Precision Medicine Marathon Match Coming to Topcoder! - $18,000 in Prizes
Date:    Fri, 11 Mar 2016 17:22:55 -0600 (CST)
Sender:  The topcoder Team <no-reply@topcoder.com>
Subject: Topcoder Design Newsletter - March 11, 2016
```
