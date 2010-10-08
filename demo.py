#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model

# Steps:
#  1. Search for a release and print results

# Webservice queries used:
#  http://www.musicbrainz.org/ws/1/release/?title=Songs+in+the+Key+of+Life&artist=Stevie+Wonder&type=xml

# http://musicbrainz.org/release/e3a0afcc-79fa-44da-ab29-0da9973eac24.html

def demo(artist, release):
	print "Searching for '%s' by %s" % (release, artist)
        q = ws.Query()
        filter = ws.ReleaseFilter(title=release,
                                artistName=artist)
        rels = q.getReleases(filter=filter)

	print "number of results: %d" % len(rels)
	for release in rels:
		print "Release: %s (%s)" % (release.getRelease().getTitle(), release.getRelease().getId())

if __name__ == '__main__':
	if len(sys.argv) == 3:
		demo(sys.argv[1], sys.argv[2])
	else:
		print "Usage: %s <name> <title>" % sys.argv[0]
