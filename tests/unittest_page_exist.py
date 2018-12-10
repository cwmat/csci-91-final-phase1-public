# from __future__ import print_function

import urllib2, sys
from HTMLParser import HTMLParser

# TODO temp, placeholder for the html to parse with. 
url = 'https://docs.python.org'

#### Unit Tests ####

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class Test(unittest.TestCase):
    def setUp(self): 
        self.response_code = get_status_code(url)

    def test_pass(self):
        self.assertEqual(self.response_code, 200)

#### function to get html status code
###### 

def get_status_code(url):
    try:

        ######## Getting URLs
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

if __name__ == "__main__":

    # url from stdin
#    if len(sys.argv) != 2:
#        print 'Usage: {} URL'.format(sys.argv[0])


#    url = sys.argv[1]
#    print url, "\n"
    # start unit test
    unittest.main()