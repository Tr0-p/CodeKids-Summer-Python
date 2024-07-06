
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections


### GLOBAL QUERIES ###

def fetch_top_tracks_global(sp):
    """Fetch the top tracks from Spotify's Global Top 50 playlist and return a DataFrame with track details."""
    top_tracks = sp.playlist_tracks('37i9dQZEVXbMDoHDwVN2tF')  # Spotify's Global Top 50 playlist ID
    tracks = [{
        'name': track['track']['name'],
        'id': track['track']['id'],
        'artist': track['track']['artists'][0]['name'],
        'popularity': track['track']['popularity']
    } for track in top_tracks['items']]
    return pd.DataFrame(tracks)

def fetch_top_tracks_by_artist(sp, artist_name):
    """Fetch top tracks for a given artist by name and return a DataFrame with track details."""
    search_result = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artist = search_result['artists']['items'][0]
    top_tracks = sp.artist_top_tracks(artist['id'])
    tracks = [{
        'name': track['name'],
        'id': track['id'],
        'popularity': track['popularity']
    } for track in top_tracks['tracks']]
    return pd.DataFrame(tracks)

def fetch_audio_features_for_tracks(sp, tracks_df):
    """Fetch audio features for a DataFrame of tracks and return a DataFrame with audio features merged."""
    features = sp.audio_features(tracks_df['id'].tolist())
    features_df = pd.DataFrame(features)
    result_df = pd.merge(tracks_df, features_df, left_on='id', right_on='id', how='left')
    result_df.set_index('name', inplace=True)
    return result_df

def fetch_related_artists(sp, artist_name):
    """Fetch artists related to a given artist by name and return a DataFrame with related artist details."""
    result = sp.search(q=f'artist:{artist_name}', type='artist')
    artist_id = result['artists']['items'][0]['id']
    related_artists = sp.artist_related_artists(artist_id)
    artists = [{
        'name': artist['name'],
        'popularity': artist['popularity']
    } for artist in related_artists['artists']]
    return pd.DataFrame(artists)

def fetch_genre_popularity_global(sp, genres):
    """Fetch popularity of given genres globally and return a DataFrame with genre popularity."""
    genre_popularity = []
    for genre in genres:
        results = sp.search(q=f'genre:"{genre}"', type='artist', limit=50)
        for artist in results['artists']['items']:
            genre_popularity.append((genre, artist['name'], artist['popularity']))
    return pd.DataFrame(genre_popularity, columns=['Genre', 'Artist', 'Popularity'])


### USER QUERIES ###

def fetch_top_tracks_user(sp, limit=10, time_range='long_term'):
    """Fetch the top tracks for the user and return a DataFrame with track details."""
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    tracks_data = [{
        'name': track['name'], 
        'id': track['id'],
        'popularity': track['popularity']
    } for track in top_tracks['items']]
    return pd.DataFrame(tracks_data)

def fetch_top_artists_user(sp, limit=10, time_range='long_term'):
    """Fetch the top artists for the user and return a DataFrame with artist details."""
    top_artists = sp.current_user_top_artists(limit=limit, time_range=time_range)
    artists_data = [{
        'name': artist['name'], 
        'popularity': artist['popularity']
    } for artist in top_artists['items']]
    return pd.DataFrame(artists_data)

def fetch_top_genres_user(sp, time_range='long_term'):
    """Fetch the top genres for the user based on top artists and return a sorted list of genres by popularity."""
    top_artists = sp.current_user_top_artists(limit=50, time_range=time_range)
    genre_count = collections.Counter()
    for artist in top_artists['items']:
        for genre in artist['genres']:
            genre_count[genre] += 1
    top_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    return pd.DataFrame(top_genres, columns=['Genre', 'Count'])

def fetch_recent_tracks_user(sp):
    """Fetch the last 50 tracks played by the user, analyze by hour, and return a DataFrame with hourly counts."""
    results = sp.current_user_recently_played(limit=50)
    tracks = [{'track': item['track']['name'], 'played_at': item['played_at']} for item in results['items']]
    df = pd.DataFrame(tracks)
    df['played_at'] = pd.to_datetime(df['played_at'])
    df['hour'] = df['played_at'].dt.hour
    return df


### PLOTS ###

def radar_chart(df):
  # Create a radar chart
  labels = np.array(df.columns.to_list())
  num_vars = len(labels)

  # Create angle for each axis
  angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
  angles += angles[:1]  # complete the loop

  # Plot each track
  fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
  for i, row in df.iterrows():
      data = row.tolist()
      data += data[:1]  # complete the loop
      ax.fill(angles, data, alpha=0.25)
      ax.plot(angles, data, label=i)  # Add each track's plot

  # Improve aesthetics
  ax.set_theta_offset(np.pi / 2)
  ax.set_theta_direction(-1)
  ax.set_rlabel_position(0)

  # Draw one axe per variable and add labels
  plt.xticks(angles[:-1], labels)

  # Add legend
  plt.legend(title='Tracks', loc='upper right', bbox_to_anchor=(1.1, 1.1))
