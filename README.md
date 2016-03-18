# gmail-search
Experimenting with Gmail API with Python

NOTE: these scripts are still in work and can only do so much

These python scripts will search through your own gmail account using a query statement. 
The query statement is set with the '-q' switch.
The queries can be limited with the '-n' switch.

Example:

  python gmail_search.py -n 10 -q from:oscar

Queries through your email and finds up to a maximum of 10 messages that contain "oscar" in the "from" data set contained in the message. Returns information about the emails it finds (is currently only displaying date, from, and subject). 

