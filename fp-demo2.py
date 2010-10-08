#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model
from pyofa import fingerprint
from pyofa import musicdns

# Steps:
#  1. Fingerprint audio file
#  2. Find fingerprint in Musicbrainz
#  3. Look up track information
#  4. Look up release information

# Webservice queries used:
#  POST to http://ofa.musicdns.org:80/ofa/1/track
#  http://www.musicbrainz.org/ws/1/track/?puid=fe0b59ea-d498-a4f3-c52a-23050e3790d9&type=xml
#  http://www.musicbrainz.org/ws/1/track/1df11035-0a12-4bce-ab72-41bbd0f9fde3?inc=artist+releases&type=xml
#  http://www.musicbrainz.org/ws/1/release/267a7c89-3624-4b7a-b7a2-aefc2bdc5e89?inc=artist+tracks&type=xml

# http://musicbrainz.org/release/267a7c89-3624-4b7a-b7a2-aefc2bdc5e89.html 

MUSICDNS_KEY = 'a7f6063296c0f1c9b75c7f511861b89b'

def demo(file):
	print "Searching for info on file %s" % file
	fp, dur = fingerprint.fingerprint_any(file)
	print "Fingerprint %s" % fp
	title, artist, puid = musicdns.lookup_fingerprint(fp, dur, MUSICDNS_KEY)
	#puid = "fe0b59ea-d498-a4f3-c52a-23050e3790d9"
	print "Title %s, artist %s, puid %s" % (title, artist, puid)
	q = ws.Query()
	filter = ws.TrackFilter(puid=puid)
	tracks = q.getTracks(filter=filter)

	print "Number of results: %d" % len(tracks)
	if len(tracks) > 0:
		t = tracks[0].getTrack()
		print "Track: %s (%s)" % (t.getTitle(), t.getId())

		releaseid = t.getReleases()[0].getId()

		includes = ws.ReleaseIncludes(artist=True, tracks=True, urlRelations=True, releaseRelations=True)
		release = q.getReleaseById(releaseid, include=includes)
		print "From release %s by %s" % (release.getTitle(), release.getArtist().getName())
		print "Tracks:"
		trackno = 1
		for track in release.getTracks():
			print "%d: %s" % (trackno, track.getTitle()),
			if track.getArtist() is not None:
				print " [%s]" % track.getArtist().getName(),
			if track.getId() == t.getId():
				print "   <-- selected file"
			else: print
			trackno += 1

if __name__ == '__main__':
	if len(sys.argv) == 2:
		demo(sys.argv[1])
	else:
		print "Usage: %s <file>" % sys.argv[0]
