#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model
from pyofa import fingerprint
from pyofa import musicdns

# Steps:
#  1. Fingerprint audio file

# Webservice queries used:
#  POST to http://ofa.musicdns.org:80/ofa/1/track

MUSICDNS_KEY = 'a7f6063296c0f1c9b75c7f511861b89b'

def demo(file):
	print "Searching for info on file %s" % file
	fp, dur = fingerprint.fingerprint_any(file)
	print "Fingerprint %s" % fp
	title, artist, puid = musicdns.lookup_fingerprint(fp, dur, MUSICDNS_KEY)
	#puid = "fe0b59ea-d498-a4f3-c52a-23050e3790d9"
	print "Title %s, artist %s, puid %s" % (title, artist, puid)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		demo(sys.argv[1])
	else:
		print "Usage: %s <file>" % sys.argv[0]
