# Spam Detection Tool

A machine learning web application that classifies text messages as spam or legitimate using natural language processing.

## Live Demo

[Try it here](https://spam-detector-ffss.onrender.com)

## Features

- Real-time text analysis
- Confidence scoring
- Responsive web interface
- RESTful API

## Tech Stack

### Backend
- Python
- Flask
- scikit-learn
- pandas & numpy
- joblib

### Frontend
- HTML/CSS
- JavaScript
- Responsive design

### Deployment
- Render
- Gunicorn

## How It Works

The application uses a machine learning model trained on thousands of spam and legitimate messages. It:

- Recognizes common spam patterns
- Converts text to numerical features
- Provides predictions with confidence scores
- Works on real-world messages

## Project Structure

```
spam_detection/
├── app.py                 # Main Flask application
├── model.py              # Model training script
├── model.pkl             # Trained model
├── vectorizer.pkl        # Text vectorizer
├── spam_assassin.csv     # Training dataset
├── requirements.txt      # Dependencies
├── Procfile             # Deployment config
├── templates/
│   └── index.html       # Web interface
├── static/
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
└── README.md
```

## Model Development

- `model.ipynb` - Initial model development in Jupyter notebook format
- `model.py` - Converted Python script for integration into the web application
- `app.py` - Flask application that loads the trained model and serves predictions

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/spam-detection.git
   cd spam-detection
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python app.py
   ```

4. Open browser to `http://localhost:5000`

## API

### Endpoint: `/predict`
**Method**: POST  
**Content-Type**: application/json

**Request:**
```json
{
  "message": "Your text message here"
}
```

**Response:**
```json
{
  "label": "spam",
  "confidence": 0.95
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "URGENT: You have won $1000! Click here to claim!"}'
```

## Skills Demonstrated

- Full-stack development
- Machine learning development
- Machine learning deployment
- API design
- Production deployment
- User experience design
- Responsive web development

## Development Process

1. Data preprocessing and cleaning
2. Model training with scikit-learn
3. Flask backend development
4. Frontend interface creation
5. Testing and validation
6. Deployment to Render


