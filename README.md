# Browser Fingerprinting Application

A comprehensive browser fingerprinting application built with Flask and MongoDB that collects and analyzes unique browser characteristics for user identification and tracking.

## Features

### 🔍 Advanced Fingerprinting
- **Canvas Fingerprinting**: Generates unique signatures based on HTML5 canvas rendering
- **WebGL Fingerprinting**: Collects GPU and graphics driver information
- **Audio Fingerprinting**: Uses Web Audio API to create audio context signatures
- **Font Detection**: Identifies installed fonts using canvas text measurement
- **Hardware Profiling**: Collects screen resolution, memory, CPU cores, and device capabilities

### 📊 Data Management
- Automatic duplicate detection using composite fingerprint hashing
- Visit counting and user session tracking
- Comprehensive statistics and analytics
- RESTful API for data access

### 🎨 User Interface
- Modern, responsive web interface
- Real-time fingerprint generation and visualization
- Interactive canvas demonstration
- Statistics dashboard

## Installation

### Prerequisites
- Python 3.8 or higher
- MongoDB database (local or cloud)
- Modern web browser with JavaScript enabled

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd browser_fingerprint
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Update `MONGO_URI` with your MongoDB connection string
   - Set other environment variables as needed

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser to `http://localhost:5000`

### Cloud Deployment

#### Deploy to Render
1. Fork this repository
2. Connect your GitHub account to Render
3. Create a new Web Service
4. Set environment variables in Render dashboard
5. Deploy automatically from GitHub

#### Deploy to Heroku
1. Install Heroku CLI
2. Create a new Heroku app
3. Set environment variables
4. Deploy using Git

## API Endpoints

### POST /api/fingerprint
Save a new browser fingerprint.

**Request Body:**
```json
{
  "userAgent": "Mozilla/5.0...",
  "canvasHash": "abc123...",
  "screenResolution": "1920x1080",
  // ... other fingerprint data
}
```

**Response:**
```json
{
  "message": "Fingerprint saved successfully",
  "isReturningUser": false,
  "visitCount": 1,
  "fingerprintId": "..."
}
```

### GET /api/fingerprints
Retrieve stored fingerprints with pagination.

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10)

**Response:**
```json
{
  "fingerprints": [...],
  "total": 100,
  "page": 1,
  "limit": 10,
  "totalPages": 10
}
```

### GET /api/stats
Get application statistics.

**Response:**
```json
{
  "totalFingerprints": 100,
  "uniqueUsers": 85,
  "totalVisits": 150,
  "commonBrowsers": [...]
}
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGO_URI` | MongoDB connection string | Required |
| `FLASK_ENV` | Flask environment | `production` |
| `SECRET_KEY` | Flask secret key | Required |
| `PORT` | Application port | `5000` |
| `LOG_LEVEL` | Logging level | `INFO` |

### MongoDB Setup

#### Local MongoDB
```bash
# Install MongoDB
# macOS: brew install mongodb-community
# Ubuntu: sudo apt install mongodb

# Start MongoDB service
mongod --dbpath /path/to/data/directory
```

#### MongoDB Atlas (Cloud)
1. Create account at mongodb.com
2. Create a new cluster
3. Get connection string
4. Add to `.env` file

## Project Structure

```
browser_fingerprint/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version
├── .env                  # Environment variables
├── README.md             # Documentation
├── templates/
│   └── index.html        # Main web interface
└── static/
    └── js/
        └── fingerprint.js # JavaScript fingerprinting module
```

## Fingerprinting Techniques

### Canvas Fingerprinting
Creates a unique signature by:
- Drawing shapes and text on HTML5 canvas
- Using different fonts, colors, and effects
- Generating SHA-256 hash of canvas data
- Detecting rendering differences across browsers/systems

### WebGL Fingerprinting
Collects GPU information:
- Graphics card vendor and model
- Driver version and capabilities
- Supported WebGL extensions
- Rendering context properties

### Audio Fingerprinting
Uses Web Audio API to:
- Create audio oscillators and filters
- Apply dynamic compression
- Analyze frequency response
- Generate audio context signature

### Font Detection
Identifies installed fonts by:
- Measuring text width with different fonts
- Comparing against baseline measurements
- Detecting font substitution patterns
- Creating font availability fingerprint

## Privacy Considerations

This application is designed for educational and legitimate business purposes such as:
- Fraud detection and prevention
- Analytics and user experience optimization
- Security research and testing

**Important Notes:**
- Always obtain user consent before collecting fingerprints
- Comply with privacy regulations (GDPR, CCPA, etc.)
- Provide clear privacy policies and opt-out mechanisms
- Use collected data responsibly and securely

## Security Features

- Input validation and sanitization
- MongoDB injection protection
- CORS configuration
- Error handling and logging
- Environment variable security

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## Changelog

### v1.0.0
- Initial release with basic fingerprinting
- MongoDB integration
- Web interface

### v2.0.0
- Advanced fingerprinting techniques
- Improved user interface
- Statistics dashboard
- Enhanced API endpoints
- Better error handling