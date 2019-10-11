import spotipy
import json
	
class Spotify_MP3():
	
	sp = spotipy.Spotify()
	token = ""
	
	# takes in artist name, returns uri and top artist name result
	def get_artist_uri(self, artist):
		results = self.sp.search(q=artist,limit=1, type='artist')
		artist_uri = results["artists"]["items"][0]['uri']
		artist_name = results["artists"]["items"][0]['name']
		return artist_uri, artist_name
		
	# takes in artist name, returns top 10 tracks of number 1 search
	def search_artist_only(self, artist):
		search_results = []
		artist_uri, artist_found = self.get_artist_uri(artist)
		top_tracks = self.sp.artist_top_tracks(artist_uri, country='US')
		print("Top Tracks for " + artist_found + ":")
		for track in top_tracks['tracks']:
			search_results.append(track['name'])
			print track['name']
			
	def search_music(self, track, artist):
		results = self.sp.search(q= track + " " + artist , limit=1)
		print(results["tracks"]["items"][0]['name'])
		print(results["tracks"]["items"][0]['artists'][0]['name'])
			
	# takes in track name, returns top track name result, artist name, and track uri
	def search_track_only(self, track):
		results = self.sp.search(q=track,limit=1, type='track')
		track_uri = results["tracks"]["items"][0]['uri']
		track_name = results["tracks"]["items"][0]['name']
		artist_name = results["tracks"]["items"][0]['artists'][0]['name']
		return track_name, artist_name, track_uri		
	
	def search_music_library(self, track, artist):
		if track == "" and artist == "":
			print "No Search Entered"
		elif track == "":
			self.search_artist_only(artist)
		elif artist == "":
			self.search_track_only(track)
		else:
			self.search_music(track, artist)
	
	# takes in autorization token as input
	# creates spotipy object
	def __init__(self, token):	
		self.token = token
		self.sp = spotipy.Spotify(token)


#sp3 = spotipy.Spotify("BQBROx1LwM0Q_CtudkGxUf021qcJjwkpkjIrtGVvJPmRaIza_h_D9BRcuP8mowhN292WoZ83H1vXO48eZ3mL3awj6S7a8Aqu0I-pvf5GOnme6XRo7iTEwDxDRhT66H-Chmqoj_sFYtfYZId97E_KpwiBLvVIxJY")


#results = sp3.search(q='love sza', limit=1)

#print(results["tracks"]["items"][0]['name'])
#print(results["tracks"]["items"][0]['artists'][0]['name'])

#print results["artists"]["items"][0]['name']
#artist_uri =  results["artists"]["items"][0]['uri']

#artist = sp3.artist(artist_uri)
#print artist

#top_tracks = sp3.artist_top_tracks(artist_uri, country='US')

#for track in top_tracks['tracks']:
#	print track['name']
