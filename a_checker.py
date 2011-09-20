# AirTrain status checker
#
# Ari Lacenski
# alacenski@gmail.com
#

import urllib
import re
import datetime
from BeautifulSoup import BeautifulSoup

class Source:
    """ Represents an AirTrain shutdown event. """
    def __init__(self, airport='', begin='', end=''):
        self.airport_code = airport
        self.from_date = begin
        self.to_date = end

def get_info():
    """ Parse AirTrain alert page. """
    sources = []
    url = 'http://www.airportinfoalerts.com/recentmessages.aspx'
    filename = 'messages.html'

#    feed = urllib.urlopen(url)
    f = open(filename)
    feed = f.read()
    soup = BeautifulSoup(feed)
    
    soup = soup.find('div', id='page')
    alerts = soup.findAll('tr')

    # regex to tokenize output when there are alert messages
    split_re = re.compile(r'[\s]')
    # regex to match date format mm/dd/yyyy
    date_re = re.compile(r'[^[/](0[1-9]|[12][0-9]|3[01])[/](19|20)\d\d$]')
    for alert in alerts:
        tds = alert.findAll('td')
        """
        Currently, this works incorrectly.
        It should parse the value in the fourth result from the source table
        and grab the time range for maintenance, then compare that
        with the current time.
        """

        if len(tds) > 0:
            location = tds[2].string
            contents = split_re.split(tds[3].string)
            data = Source(location)

            if 'EWR' in location:
                for token in contents:
                    print token
                    if date_re(token) == True:
                        print 'OMG'
                data = Source('EWR', '1', '2')
            elif 'JFK' in location:
                data = Source('JFK', '1', '2')            
            sources.append(data)
    return sources

get_info()
