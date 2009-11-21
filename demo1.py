#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model

# http://www.musicbrainz.org/ws/1/release/?title=Songs+in+the+Key+of+Life&artist=Stevie+Wonder&type=xml
# http://musicbrainz.org/release/e3a0afcc-79fa-44da-ab29-0da9973eac24.html
# http://www.musicbrainz.org/ws/1/release/edf99004-eaca-4295-b2f9-581891ba044f?inc=artist+tracks&type=xml

def demo(artist, release):
	print "Searching for '%s' by %s" % (release, artist)
        q = ws.Query()
        filter = ws.ReleaseFilter(title=release,
                                artistName=artist)
        rels = q.getReleases(filter=filter)

	print "number results: %d" % len(rels)
	if len(rels) > 0:
		r = rels[0].getRelease()

		# Get the release information
		includes = ws.ReleaseIncludes(artist=True, tracks=True)
		release = q.getReleaseById(r.id, include=includes)
		print "Release 1: %s (%s) " % (release.getTitle(), release.id)
		# XXX: Print the artist details
		print "Tracks:"
		trackno = 1
		for track in release.getTracks():
			print "%d: %s " % (trackno, track.getTitle())
			trackno += 1

if __name__ == '__main__':
	demo(sys.argv[1], sys.argv[2])
