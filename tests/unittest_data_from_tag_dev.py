# from __future__ import print_function

import urllib2, sys
from HTMLParser import HTMLParser

# TODO temp, placeholder for the html to parse with. 
url = 'http://3.81.16.217'

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

def get_data_from_tag(url):
    try:

        ######## Getting URLs
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
        self.response_data = get_data_from_tag(url)

    def test_pass(self):
        self.assertEqual(self.response_data, 'CSCI-91 Public: Phase 1')

if __name__ == "__main__":

    unittest.main()