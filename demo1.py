#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model

# Steps:
#  1. Search for a release and print results
#  2. Get detailed release information

# Webservice queries used:
#  http://www.musicbrainz.org/ws/1/release/?title=Songs+in+the+Key+of+Life&artist=Stevie+Wonder&type=xml
#  http://www.musicbrainz.org/ws/1/release/edf99004-eaca-4295-b2f9-581891ba044f?inc=artist+tracks&type=xml
#  http://www.musicbrainz.org/ws/1/release/24a355b3-940d-4428-b54d-d830fb5766f6?inc=artist+tracks&type=xml

# http://musicbrainz.org/release/e3a0afcc-79fa-44da-ab29-0da9973eac24.html

def demo(artist, release):
	print "Searching for '%s' by %s" % (release, artist)
        q = ws.Query()
        filter = ws.ReleaseFilter(title=release,
                                artistName=artist)
        rels = q.getReleases(filter=filter)

	print "number of results: %d" % len(rels)
	if len(rels) > 0:
		r = rels[0].getRelease()

		# By default the webservice only returns basic information, so we
		#  need to ask it to give us artist and track information
		includes = ws.ReleaseIncludes(artist=True, tracks=True)
		release = q.getReleaseById(r.id, include=includes)
		print "Release 1: %s (%s) " % (release.getTitle(), release.id)
		print "By %s" % release.getArtist().getName();
		print "Tracks:"
		trackno = 1
		for track in release.getTracks():
			print "%d: %s" % (trackno, track.getTitle()),
			if track.getArtist() is not None:
				print "[by %s]" % track.getArtist().getName()
			else: print
			trackno += 1

if __name__ == '__main__':
	if len(sys.argv) == 3:
		demo(sys.argv[1], sys.argv[2])
	else:
		print "Usage: %s <name> <title>" % sys.argv[0]
