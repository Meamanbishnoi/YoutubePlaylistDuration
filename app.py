from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
import isodate
import re
import os

app = Flask(__name__)

# Get API key from environment variable (for deployment) or use placeholder for local dev
API_KEY = os.environ.get('YOUTUBE_API_KEY', 'AIzaSyAjob1OnFIbsKd9X2Zz9lvw5M6mvcuyAlE')

def extract_playlist_id(url):
    """Extract playlist ID from YouTube URL"""
    patterns = [
        r'list=([a-zA-Z0-9_-]+)',
        r'playlist\?list=([a-zA-Z0-9_-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_playlist_duration(playlist_id, video_count=None):
    """Get total duration of playlist videos"""
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        videos = []
        next_page_token = None
        
        while True:
            playlist_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()
            
            videos.extend([item['contentDetails']['videoId'] for item in playlist_response['items']])
            
            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break
        
        # Limit to specified video count
        if video_count:
            videos = videos[:video_count]
        
        total_seconds = 0
        for i in range(0, len(videos), 50):
            video_ids = videos[i:i+50]
            video_request = youtube.videos().list(
                part='contentDetails',
                id=','.join(video_ids)
            )
            video_response = video_request.execute()
            
            for item in video_response['items']:
                duration = item['contentDetails']['duration']
                total_seconds += isodate.parse_duration(duration).total_seconds()
        
        return total_seconds, len(videos)
    
    except Exception as e:
        return None, str(e)

def format_duration(seconds):
    """Format seconds into readable duration"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours}h {minutes}m {secs}s"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    playlist_url = data.get('playlist_url')
    video_count = data.get('video_count')
    
    playlist_id = extract_playlist_id(playlist_url)
    
    if not playlist_id:
        return jsonify({'error': 'Invalid YouTube playlist URL'}), 400
    
    total_seconds, video_total = get_playlist_duration(playlist_id, video_count)
    
    if total_seconds is None:
        return jsonify({'error': f'Error fetching playlist: {video_total}'}), 400
    
    # Calculate durations at different speeds
    speeds = {
        '1x': total_seconds,
        '1.25x': total_seconds / 1.25,
        '1.5x': total_seconds / 1.5,
        '1.75x': total_seconds / 1.75,
        '2x': total_seconds / 2
    }
    
    formatted_durations = {speed: format_duration(duration) for speed, duration in speeds.items()}
    
    return jsonify({
        'video_count': video_total,
        'durations': formatted_durations,
        'total_seconds': total_seconds
    })

if __name__ == '__main__':
    app.run(debug=True)
