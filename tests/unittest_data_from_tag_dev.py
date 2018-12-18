# from __future__ import print_function

import urllib2, sys
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

# define a base class to handle all vary test cases
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = ''
        self.recordtitle = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.recordtitle = True
            print "Encountered the beginning of a %s tag" % tag
            # for name, value in attrs:
                # print name, value
                # if name == 'class' and value == 'body':
                #     print name, value
                #     print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        if tag == 'title':
          self.recording -=1
          self.recordtitle = False
          print "Encountered the end of a %s tag" % tag 

    def handle_data(self, data):
        if self.recordtitle:
            print "Data     :", data
            self.data = data

#### function to get html status code
###### 

def get_data_from_tag():
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
    print parser.close()
    return content


#### Unit Tests ####

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class Test(unittest.TestCase):
    def setUp(self): 
        self.response_data = get_data_from_tag()

    def test_pass(self):
        self.assertEqual(self.response_data, 'CSCI-91 Public: Phase 1')

if __name__ == "__main__":

    unittest.main()
