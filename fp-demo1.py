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
import repr

# http://www.musicbrainz.org/ws/1/track/?puid=e0488c71-2d76-f3b8-6b63-59c21fe93cb1&type=xml

MUSICDNS_KEY = 'a7f6063296c0f1c9b75c7f511861b89b'

def demo(file):
	print "Searching for info on file %s" % file
	fp, dur = fingerprint.fingerprint_any(file)
	print "Fingerprint %s" % fp
	title, artist, puid = musicdns.lookup_fingerprint(fp, dur, MUSICDNS_KEY)
	#puid = "e0488c71-2d76-f3b8-6b63-59c21fe93cb1"
	print "Title %s, artist %s, puid %s" % (title, artist, puid)
        q = ws.Query()
        filter = ws.TrackFilter(puid=puid)
        tracks = q.getTracks(filter=filter)

	print "Results: %d" % len(tracks)
	for track in tracks:
		print "%s (%s)" % (track, track.getTrack().getTitle())

if __name__ == '__main__':
	demo(sys.argv[1])
