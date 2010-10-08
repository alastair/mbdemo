Musicbrainz API demo
====================

These files demonstrate how to use the [Musicbrainz webservice][ws] via the
python-musicbrainz2 library.

There are two examples:

 * **demo:** searching for and manipulating data from the webservice
 * **fp-demo:** using acoustic fingerprinting and Musicbrainz

Each demo starts with a simple usecase, and subsequent files add
additional functionality.  See the files for more information on
what is being done.

Dependencies
------------
On Ubuntu or Debian, install python-musicbrainz2 and libofa0.  Install 
mpg123, ogg or flac if you want to fingerprint the respective filetypes.

Documentation
-------------
Further information on the python-musicbrainz2 library can be found at
http://users.musicbrainz.org/~matt/python-musicbrainz2/html/

[ws]: http://wiki.musicbrainz.org/XMLWebService
