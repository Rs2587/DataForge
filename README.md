# DataForge — Dockerized ETL Data Pipeline

DataForge is a Python-based ETL (Extract, Transform, Load) data pipeline that processes customer data from CSV files, validates and transforms the data, loads it into MySQL, and exposes the processed data through a FastAPI REST API.

The project is containerized using Docker and Docker Compose for consistent development and deployment.

## 🚀 Project Overview

DataForge demonstrates a complete data engineering workflow:

```text
CSV File
   ↓
Extract
   ↓
Transform
   ↓
Validate
   ↓
Load into MySQL
   ↓
FastAPI
   ↓
REST API
```

## 🛠️ Technologies Used

- Python
- Pandas
- MySQL
- FastAPI
- Docker
- Docker Compose
- Pytest
- SQL
- REST API
- Git & GitHub

## 📁 Project Structure

```text
DataForge/
│
├── api/
│   ├── __init__.py
│   └── main.py
│
├── data/
│   └── raw/
│       └── customers.csv
│
├── database/
│   └── schema.sql
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── pipeline.py
│
├── tests/
│   ├── test_api.py
│   └── test_pipeline.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🔄 ETL Pipeline

### 1. Extract

The pipeline reads customer data from the CSV file using Pandas.

```text
data/raw/customers.csv
        ↓
    Extract
```

### 2. Transform

The extracted data is cleaned and transformed before loading.

```text
Raw Data
   ↓
Cleaning
   ↓
Transformation
```

### 3. Validate

The pipeline validates the processed data to ensure that it satisfies the required conditions.

```text
Transformed Data
       ↓
   Validation
       ↓
Valid Data
```

### 4. Load

The validated data is loaded into a MySQL database.

```text
Valid Data
    ↓
  MySQL
```

## 🗄️ Database

The project uses MySQL as the relational database.

Database schema:

```text
database/schema.sql
```

The application connects to MySQL using environment variables rather than hard-coded credentials.

Example:

```env
DB_PASSWORD=your_mysql_password
DB_NAME=dataforge
```

For local development, create a `.env` file based on `.env.example`.

## 🐳 Docker

Docker Compose is used to run the application services.

The project contains:

- MySQL database
- FastAPI application
- ETL service

### Start the application

```bash
docker compose up --build
```

### Run the ETL pipeline

```bash
docker compose run --rm etl
```

### Check running containers

```bash
docker compose ps
```

### View API logs

```bash
docker compose logs api
```

## 🌐 FastAPI

DataForge exposes the processed customer data through a REST API.

FastAPI documentation is available at:

```text
http://localhost:8000/docs
```

The Swagger UI can be used to test the available API endpoints.

Example:

```text
GET /customers
```

## 🧪 Testing

The project includes automated tests using Pytest.

Run tests locally:

```bash
pytest
```

Tests cover the pipeline and API functionality.

## 🔐 Environment Variables

Sensitive configuration is not stored directly in the source code.

Create a local `.env` file:

```env
DB_PASSWORD=your_mysql_password
DB_NAME=dataforge
```

The `.env` file is excluded from Git using `.gitignore`.

A safe template is provided:

```text
.env.example
```

## 💡 Key Data Engineering Concepts Demonstrated

This project demonstrates practical understanding of:

- ETL pipelines
- Data extraction
- Data transformation
- Data validation
- Relational databases
- SQL
- MySQL
- REST APIs
- FastAPI
- Docker
- Docker Compose
- Environment variables
- Automated testing
- Git and GitHub
- Modular Python project structure

## 🔮 Future Improvements

Possible improvements for a production-ready version include:

- Apache Airflow for workflow orchestration
- PostgreSQL support
- Apache Spark for large-scale processing
- Cloud deployment
- Logging and monitoring
- Data quality monitoring
- CI/CD using GitHub Actions
- API authentication
- Database migrations
- Scalable batch processing

## 👨‍💻 Author

Rajvardhan Suryavanshi

Data Science / Data Engineering Enthusiast

GitHub: https://github.com/Rs2587
