# 🎥 YouTube Playlist Duration Calculator

A professional web application that calculates the total duration of YouTube playlists with playback speed options. Perfect for students, content creators, and anyone who wants to plan their viewing time efficiently.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 📊 Calculate total duration of any YouTube playlist
- 🎯 Calculate duration up to a specific video number
- ⚡ View duration at multiple playback speeds (1x, 1.25x, 1.5x, 1.75x, 2x)
- 🎨 Modern, professional dark theme UI
- 📱 Fully responsive design
- 🚀 Fast and lightweight

## 🖼️ Screenshots

![App Screenshot](https://via.placeholder.com/800x400/0f172a/3b82f6?text=YouTube+Playlist+Calculator)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- YouTube Data API v3 key ([Get one here](https://console.cloud.google.com/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-playlist-calculator.git
cd youtube-playlist-calculator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your YouTube API key:
```bash
# Windows
set YOUTUBE_API_KEY=your_api_key_here

# Mac/Linux
export YOUTUBE_API_KEY=your_api_key_here
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## 🔑 Getting YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable "YouTube Data API v3"
4. Go to Credentials → Create Credentials → API Key
5. Copy your API key

## 🌐 Deploy to Production

### Deploy to Vercel (Recommended)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/youtube-playlist-calculator)

1. Click the button above or:
   ```bash
   npm i -g vercel
   vercel
   ```

2. Add environment variable in Vercel dashboard:
   - `YOUTUBE_API_KEY` = your API key

### Deploy to Render

1. Create account on [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Add environment variable `YOUTUBE_API_KEY`
5. Deploy

### Deploy to Railway

1. Create account on [railway.app](https://railway.app)
2. Create new project from GitHub
3. Add environment variable `YOUTUBE_API_KEY`
4. Deploy

## 📖 Usage

1. Copy any YouTube playlist URL:
   ```
   https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf
   ```

2. Paste it into the input field

3. (Optional) Enter a video number to calculate duration up to that specific video

4. Click "Calculate Duration"

5. View results showing:
   - Total number of videos
   - Duration at different playback speeds

## 🛠️ Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Google API Python Client](https://github.com/googleapis/google-api-python-client) - YouTube API integration
- [isodate](https://github.com/gweis/isodate) - ISO 8601 duration parsing
- Vanilla JavaScript - Frontend interactivity
- CSS3 - Modern styling

## 📝 API Quota Information

- YouTube API has a quota limit of 10,000 units per day (free tier)
- Each playlist calculation uses approximately 1-3 units
- Large playlists may take a few seconds to process

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- YouTube Data API v3 for providing playlist data
- Flask community for excellent documentation
- All contributors who help improve this project

## 📧 Contact

Have questions or suggestions? Feel free to reach out!

- Create an issue on GitHub
- Email: your.email@example.com

---

⭐ Star this repo if you find it helpful!
