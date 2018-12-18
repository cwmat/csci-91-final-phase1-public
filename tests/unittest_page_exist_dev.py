# from __future__ import print_function

import urllib2, sys, re
from HTMLParser import HTMLParser


#### Dynamically generate dev url. 

def generate_request_url():
    url = ''
    pat = re.compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

    try:

        ######## Getting URLs
        response = urllib2.urlopen('https://s3.amazonaws.com/e91-cloudtrail/AWSLogs/531997612114/CloudTrail/test/devip')
        ## Getting the code
        content = response.read()
        print "This gets the DEV ip: ", content
        matches = pat.match(content)
        if matches:
            devip = matches.group(0)
            url = "http://%s" % devip
     
    except urllib2.HTTPError as e:
        print(e, 'while fetching', url)
        return 
    return url


#### Unit Tests ####

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class Test(unittest.TestCase):
    def setUp(self): 
        self.response_code = 0
        self.response_data = ''

    def test_status_code(self):
        self.response_code = get_status_code(url)
        self.assertEqual(self.response_code, 200)

    def test_content(self):
        self.response_data = get_data_from_tag(url)
        self.assertEqual(self.response_data, 'GET ADT MONITORED')

# define a base class to handle all vary test cases
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = ''
        self.recorddiv = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'top-section-h1':
                    self.recorddiv = True
                    print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        if tag == 'div' and self.recorddiv == True:
            self.recorddiv = False
            print "Encountered the end of a %s tag" % tag 

    def handle_data(self, data):
        if self.recorddiv:
            print "Data     :", data
            self.data = data

#### function to get html status code
######

def get_status_code(url):
    try:

        ######## Getting URLs
        url = generate_request_url()
        response = urllib2.urlopen(url)
        # debug - full html pull-down here
        ## Get the URL. This gets the real URL. 
        print "The URL is: ", response.geturl()
        ## Getting the code
        print "This gets the code: ", response.code
        return response.code

    except urllib2.HTTPError as e:
        print(e, 'while fetching', url)
        return 

#### function to get html data
###### 

def get_data_from_tag(url):
    try:

        ######## Getting URLs
        url = generate_request_url()
        response = urllib2.urlopen(url)
        # debug - full html pull-down here
        ## Get the URL. This gets the real URL. 
        print "The URL is: ", response.geturl()
        ## Getting the code
        print "This gets the code: ", response.code
        # Get all data
        html = response.read()
        # print "Get all data: ", html
    except urllib2.HTTPError as e:
        print(e, 'while fetching', url)
        return

    parser = MyHTMLParser()
    parser.feed(html)
    content = parser.data
    parser.close()
    return content

if __name__ == "__main__":

    # start unit test
    unittest.main()
