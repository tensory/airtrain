# AirTrain status checker
#
# Ari Lacenski
# alacenski@gmail.com
#

import urllib
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

    feed = urllib.urlopen(url)
    soup = BeautifulSoup(feed)
    
    soup = soup.find('div', id='page')
    alerts = soup.findAll('tr')
    
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
            data = Source(location)
            if 'EWR' in location:
                data = Source('EWR', '1', '2')
            elif 'JFK' in location:
                data = Source('JFK', '1', '2')            
            sources.append(data)
    return sources
