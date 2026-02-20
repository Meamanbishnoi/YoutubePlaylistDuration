// Register Service Worker for PWA
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/static/sw.js')
            .then(registration => {
                console.log('Service Worker registered successfully:', registration.scope);
            })
            .catch(error => {
                console.log('Service Worker registration failed:', error);
            });
    });
}

// PWA Install Prompt
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    showInstallPromotion();
});

function showInstallPromotion() {
    const installBanner = document.createElement('div');
    installBanner.className = 'install-banner';
    installBanner.innerHTML = `
        <div class="install-content">
            <span>📱 Install app for quick access</span>
            <button onclick="installApp()" class="install-btn">Install</button>
            <button onclick="dismissInstall()" class="dismiss-btn">✕</button>
        </div>
    `;
    document.body.appendChild(installBanner);
}

function installApp() {
    const banner = document.querySelector('.install-banner');
    if (banner) banner.remove();
    
    if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the install prompt');
            }
            deferredPrompt = null;
        });
    }
}

function dismissInstall() {
    const banner = document.querySelector('.install-banner');
    if (banner) banner.remove();
}

async function calculateDuration() {
    const playlistUrl = document.getElementById('playlist-url').value.trim();
    const videoCount = document.getElementById('video-count').value;
    
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const results = document.getElementById('results');
    
    // Reset displays
    loading.style.display = 'none';
    error.style.display = 'none';
    results.style.display = 'none';
    
    if (!playlistUrl) {
        error.textContent = 'Please enter a YouTube playlist URL';
        error.style.display = 'block';
        return;
    }
    
    loading.style.display = 'block';
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                playlist_url: playlistUrl,
                video_count: videoCount ? parseInt(videoCount) : null
            })
        });
        
        const data = await response.json();
        
        loading.style.display = 'none';
        
        if (!response.ok) {
            error.textContent = data.error || 'An error occurred';
            error.style.display = 'block';
            return;
        }
        
        // Display results
        document.getElementById('total-videos').textContent = data.video_count;
        document.getElementById('duration-1x').textContent = data.durations['1x'];
        document.getElementById('duration-1-25x').textContent = data.durations['1.25x'];
        document.getElementById('duration-1-5x').textContent = data.durations['1.5x'];
        document.getElementById('duration-1-75x').textContent = data.durations['1.75x'];
        document.getElementById('duration-2x').textContent = data.durations['2x'];
        
        results.style.display = 'block';
        
    } catch (err) {
        loading.style.display = 'none';
        error.textContent = 'Network error. Please try again.';
        error.style.display = 'block';
    }
}

// Allow Enter key to trigger calculation
document.getElementById('playlist-url').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        calculateDuration();
    }
});

document.getElementById('video-count').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        calculateDuration();
    }
});
