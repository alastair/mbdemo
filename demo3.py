#!/usr/bin/python

import sys
import musicbrainz2 as mb
import musicbrainz2.webservice as ws
import musicbrainz2.model as model

# http://www.musicbrainz.org/ws/1/release/?title=Songs+in+the+Key+of+Life&artist=Stevie+Wonder&type=xml
# http://www.musicbrainz.org/ws/1/release/edf99004-eaca-4295-b2f9-581891ba044f?inc=artist+tracks+url-rels+release-rels&type=xml
# http://musicbrainz.org/release/e3a0afcc-79fa-44da-ab29-0da9973eac24.html

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
		includes = ws.ReleaseIncludes(artist=True, tracks=True, urlRelations=True, releaseRelations=True)
		release = q.getReleaseById(r.id, include=includes)
		print "Release 1: %s (%s) " % (release.getTitle(), release.id)
		print "Tracks:"
		trackno = 1
		for track in release.getTracks():
			print "%d: %s " % (trackno, track.getTitle())
			trackno += 1

		print "Other information"
		# urlRelations
		for rel in release.getRelations(model.Relation.TO_URL):
			if rel.getType() == "http://musicbrainz.org/ns/rel-1.0#AmazonAsin":
				print "Amazon URL: %s" % rel.getTargetId()
			elif rel.getType() == "http://musicbrainz.org/ns/rel-1.0#Wikipedia":
				print "Wikipedia URL: %s" % rel.getTargetId()
			elif rel.getType() == "http://musicbrainz.org/ns/rel-1.0#Discogs":
				print "Discogs URL: %s" % rel.getTargetId()
		print "Other discs"
		# releaseRelations
		for rel in release.getRelations(model.Relation.TO_RELEASE):
			if rel.getType() == "http://musicbrainz.org/ns/rel-1.0#PartOfSet":
				if rel.getDirection() == model.Relation.DIR_BACKWARD:
					print "Previous disc: %s (%s)" % (rel.getTarget().getTitle(), rel.getTargetId()) 
				else:
					print "Next disc: %s (%s)" % (rel.getTarget().getTitle(), rel.getTargetId()) 

if __name__ == '__main__':
	demo(sys.argv[1], sys.argv[2])
