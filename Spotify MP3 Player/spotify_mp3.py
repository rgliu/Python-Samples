import spotipy
import json
import text_options
	
class Spotify_MP3():
	
	sp = spotipy.Spotify()
	text = text_options.Text_Options()
	search_results = [[],[]]
	token = ""
	
	# takes in artist name, returns uri and top artist name result
	def get_artist_uri(self, artist):
		results = self.sp.search(q=artist,limit=1, type='artist')
		artist_uri = results["artists"]["items"][0]['uri']
		artist_name = results["artists"]["items"][0]['name']
		return artist_uri, artist_name
		
	# takes in artist name, returns top 10 tracks of number 1 search in string format
	def search_artist_only(self, artist):
		#search_results = []
		artist_uri, artist_found = self.get_artist_uri(artist)
		top_tracks = self.sp.artist_top_tracks(artist_uri, country='US')
		#search_results.append(self.text.BOLD + "Top Tracks for " + artist_found + ":" + self.text.END)
		for track in top_tracks['tracks']:
			self.search_results.append(["    " + track['name'] + " - " + artist_found, track['uri']] )
		#self.search_results_msg = "\n".join(search_results)
			
	def search_music(self, track, artist):
		#search_result = ""
		results = self.sp.search(q= track + " " + artist , limit=1)
		self.search_results.append(["    " + results["tracks"]["items"][0]['name'] + " - " + results["tracks"]["items"][0]['artists'][0]['name'], results["tracks"]["items"][0]['uri'] ])
		#self.search_results_msg = self.text.BOLD + "Top Result:\n" + self.text.END + search_result		
			
	# takes in track name, returns top track name result, artist name, and track uri
	def search_track_only(self, track):
		#search_results = [self.text.BOLD + "Top Result(s):" + self.text.END]
		results = self.sp.search(q=track,limit=10, type='track')
		#track_uri = results["tracks"]["items"][0]['uri']
		for i in range(10):
			track_name = results["tracks"]["items"][i]['name']
			artist_name = results["tracks"]["items"][i]['artists'][0]['name']
			track_uri = results["tracks"]["items"][i]['uri']
			self.search_results.append(["    " + track_name + " - " + artist_name,track_uri])
		#self.search_results_msg = "\n".join(search_results)
		#return track_name, artist_name, track_uri		
	
	def play_track(self, track_uri):
		self.sp.start_playback(context_uri=track_uri)
	
	def search_music_library(self, track, artist):
		if track == "" and artist == "":
			print self.text.BOLD + "No Search Entered" +  self.text.END
		elif track == "":
			self.search_artist_only(artist)
		elif artist == "":
			self.search_track_only(track)
		else:
			self.search_music(track, artist)
			
	def clear_search_results(self):
		del self.search_results[:]
	
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
