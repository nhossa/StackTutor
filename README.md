# Vocab AI Coach

A FastAPI backend microservice that simplifies difficult English words using dictionary APIs and AI language models.

## Overview

Vocab AI Coach is a RESTful API service designed to help users expand their vocabulary by providing simplified definitions and contextual examples of complex English words. The service integrates with external dictionary APIs and AI language models to transform formal definitions into easily understandable explanations.

## Features

- Fetch formal dictionary definitions from external APIs
- Simplify complex definitions using AI language models
- Generate contextual example sentences
- Save user vocabulary for future reference and review
- User-specific vocabulary tracking and management
- RESTful API architecture
- Docker containerization for easy deployment

## Architecture

The service follows a microservice architecture pattern:

```
Client Request
    |
    v
FastAPI Application
    |
    +---> Dictionary API Service (External)
    |
    +---> AI Language Model Service (OpenAI/Anthropic)
    |
    +---> Database Layer (SQLite/PostgreSQL)
    |
    v
JSON Response
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Docker (optional, for containerized deployment)
- API keys for dictionary and AI services

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Vocab-Coach.git
cd Vocab-Coach

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the application
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Define a Word

```http
POST /api/v1/define
Content-Type: application/json

{
  "word": "serendipity"
}
```

Response:
```json
{
  "word": "serendipity",
  "formal_definition": "The occurrence and development of events by chance in a happy or beneficial way",
  "simple_definition": "Finding something good by accident or luck",
  "example": "Finding a $20 bill in your old jacket is pure serendipity",
  "timestamp": "2025-11-18T12:00:00Z"
}
```

### Save Vocabulary

```http
POST /api/v1/vocabulary
Content-Type: application/json

{
  "user_id": "user123",
  "word": "serendipity"
}
```

### Retrieve User Vocabulary

```http
GET /api/v1/vocabulary/{user_id}
```

Response:
```json
{
  "user_id": "user123",
  "words": [
    {
      "word": "serendipity",
      "saved_at": "2025-11-18T12:00:00Z",
      "review_count": 0
    }
  ],
  "total": 1
}
```

## Project Structure

```
Vocab-Coach/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # Database configuration
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── define.py        # Definition endpoints
│   │   └── vocabulary.py    # Vocabulary management endpoints
│   └── services/
│       ├── __init__.py
│       ├── dictionary.py    # Dictionary API integration
│       └── ai_service.py    # AI model integration
├── tests/
│   └── test_api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Technology Stack

- FastAPI - Web framework
- SQLAlchemy - ORM
- SQLite/PostgreSQL - Database
- OpenAI API - AI language model
- Pydantic - Data validation
- Docker - Containerization

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
DICTIONARY_API_KEY=your_dictionary_api_key
DATABASE_URL=sqlite:///./vocab.db
API_PORT=8000
LOG_LEVEL=INFO
```

## Docker Deployment

```bash
# Build the image
docker build -t vocab-coach:latest .

# Run with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f
```

## Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## API Documentation

Once the application is running, access the interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

Project Repository: https://github.com/YOUR_USERNAME/Vocab-Coach

--Author: Naim Hossain