#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model
import sys
import os
sys.path.insert(0, os.path.expanduser("~/Projects/pyofa"))
import fingerprint
import musicdns

# http://www.musicbrainz.org/ws/1/track/?puid=e0488c71-2d76-f3b8-6b63-59c21fe93cb1&type=xml
# http://www.musicbrainz.org/ws/1/track/29dd9077-f6dd-4b56-97c0-92ca31d273d8?inc=artist+releases&type=xml
# http://www.musicbrainz.org/ws/1/release/93c971ac-b822-4be5-9e0c-b8f1210a291e?inc=artist+tracks&type=xml
# http://musicbrainz.org/release/93c971ac-b822-4be5-9e0c-b8f1210a291e.html 

MUSICDNS_KEY = 'a7f6063296c0f1c9b75c7f511861b89b'

def demo(file):
	print "Searching for info on file %s" % file
	fp, dur = fingerprint.fingerprint_any(file)
	print "Fingerprint %s" % fp
	title, artist, puid = musicdns.lookup_fingerprint(fp, dur, MUSICDNS_KEY)
	#puid = "e0488c71-2d76-f3b8-6b63-59c21fe93cb1"
	print "Title %s, artist %s, puid %s" % (title, artist, puid)

if __name__ == '__main__':
	demo(sys.argv[1])
