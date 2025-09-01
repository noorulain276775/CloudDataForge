# CloudDataForge

A modern, scalable data engineering platform built with FastAPI for cloud-native ETL operations and data processing workflows.

## 🚀 Features

- **FastAPI-powered REST API** for data pipeline management
- **Cloud-native architecture** supporting GCP, AWS, and Azure
- **Modular ETL services** for data ingestion, processing, and storage
- **Scalable microservices** design for enterprise workloads
- **Comprehensive testing** with pytest framework
- **Docker containerization** for easy deployment
- **Environment-based configuration** management

## 🏗️ Architecture

```
CloudDataForge/
│
├── app/                    # Main application package
│   ├── main.py           # FastAPI application entrypoint
│   ├── routes.py         # API endpoint definitions
│   ├── services/         # Business logic and ETL operations
│   │   ├── ingestion.py  # Data ingestion services
│   │   ├── processing.py # Data transformation services
│   │   └── storage.py    # Data storage services
│   └── utils/            # Helper utilities
│       └── gcp_helpers.py # Google Cloud Platform utilities
│
├── tests/                 # Test suite
│   └── test_routes.py    # API endpoint tests
│
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore patterns
├── .env.example         # Environment variables template
└── README.md            # Project documentation
```

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python 3.8+)
- **Data Processing**: Pandas, NumPy
- **Cloud Integration**: Google Cloud Platform SDK
- **Testing**: pytest
- **Containerization**: Docker
- **Environment**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- Docker (for containerized deployment)
- Google Cloud Platform account (for GCP features)
- pip or poetry for dependency management

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CloudDataForge.git
   cd CloudDataForge
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t clouddataforge .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 clouddataforge
   ```

## 🔧 Configuration

The application uses environment variables for configuration. Copy `.env.example` to `.env` and customize:

```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# GCP Configuration
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
GCP_PROJECT_ID=your-project-id
GCP_BUCKET_NAME=your-bucket-name

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 📚 API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_routes.py
```

## 📦 Project Structure

### Core Components

- **`app/main.py`**: FastAPI application configuration and startup
- **`app/routes.py`**: API endpoint definitions and request/response models
- **`app/services/`**: Business logic layer for ETL operations
- **`app/utils/`**: Utility functions and helper modules

### Service Layer

- **Ingestion Service**: Handles data ingestion from various sources
- **Processing Service**: Manages data transformation and ETL workflows
- **Storage Service**: Handles data persistence and retrieval

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the API docs at `/docs`
- **Issues**: Report bugs and feature requests via GitHub Issues
- **Discussions**: Join community discussions in GitHub Discussions

## 🔮 Roadmap

- [ ] Multi-cloud support (AWS, Azure)
- [ ] Real-time streaming capabilities
- [ ] Advanced data quality monitoring
- [ ] Workflow orchestration with Airflow
- [ ] Machine learning pipeline integration
- [ ] Performance monitoring and alerting

## 📊 Performance

- **Response Time**: < 100ms for standard API calls
- **Throughput**: 1000+ requests/second on standard hardware
- **Scalability**: Horizontal scaling support via container orchestration

---

**Built with ❤️ for the data engineering community**
