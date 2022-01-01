"""
Step 1: Log into youtube
Step 2: Grab liked videos
Step 3: Create a new playlist
Step 4: Search for the song
Step 5: Add this song into the new Spotify playlist
"""
import json
import requests
from secrets import spotify_user_id,spotify_token

class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    def get_youtube_client(self):
        pass

    def get_liked_videos(self):
        pass

    def create_playlist(self):
        request_body = json.dump({
            "name": "Youtube_Tutorial",
            "description": "All liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        #playlist id
        return response_json("id")

    def get_spotify_uri(self,song_name, artist):
        query = https://api.spotify.com/v1/search
    def add_song_to_playlist(self):
        pass