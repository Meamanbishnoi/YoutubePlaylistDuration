# 🎥 YouTube Playlist Duration Calculator

Calculate the total duration of any YouTube playlist with playback speed options. Perfect for students and content creators who want to plan their viewing time.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- Calculate total duration of any YouTube playlist
- Calculate duration up to a specific video number
- View duration at different playback speeds (1x, 1.25x, 1.5x, 1.75x, 2x)
- Modern dark theme UI
- Fully responsive design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Meamanbishnoi/YoutubePlaylistDuration.git
cd YoutubePlaylistDuration
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get your YouTube API key:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable "YouTube Data API v3"
   - Create credentials (API Key)
   - Copy your API key

4. Set your API key:
```bash
# Windows
set YOUTUBE_API_KEY=your_api_key_here

# Mac/Linux
export YOUTUBE_API_KEY=your_api_key_here
```

5. Run the app:
```bash
python app.py
```

6. Open `http://localhost:5000` in your browser

## Usage

1. Copy a YouTube playlist URL
2. Paste it into the input field
3. (Optional) Enter a video number to calculate up to that video
4. Click "Calculate Duration"
5. View results at different playback speeds

## Deploy Online

### Vercel (Recommended)
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Add environment variable `YOUTUBE_API_KEY` in dashboard

### Render
1. Create account on [render.com](https://render.com)
2. Connect your GitHub repo
3. Add environment variable `YOUTUBE_API_KEY`
4. Deploy

## Built With

- Flask - Web framework
- YouTube Data API v3 - Playlist data
- JavaScript & CSS3 - Frontend

## Contributing

Pull requests are welcome! Feel free to contribute.

## License

MIT License - see [LICENSE](LICENSE) file

## Author

**Aman Bishnoi**
- GitHub: [@Meamanbishnoi](https://github.com/Meamanbishnoi)
- Email: aman.bishnoi7007@gmail.com

## Contact

Questions or suggestions? Reach out!
- Email: aman.bishnoi7007@gmail.com
- GitHub Issues: [Create an issue](https://github.com/Meamanbishnoi/YoutubePlaylistDuration/issues)

---

⭐ Star this repo if you find it helpful!
