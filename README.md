# FootballFieldBooking

SOCIAL LITE (Social Network Prototype).

## Getting Started

These instructions will help you run a copy of the project on your local machine for development and testing.

### Prerequisites

Install the following tools:

- Docker
- Docker Compose

### Installation and Launch

1. **Cloning the repository**:
    ```
    git clone https://github.com/ulugbekaxtamov/social-lite.git
    ```

2. **Navigate to the project directory**:
    ```
    cd social_lite
    ```

3. **Create `.env` files using examples**:
    ```
    cat example.env > .env
    ```

4. **Run Docker Compose**:
    ```
    docker-compose up --build -d
    ```

### API Documentation

Access the Swagger documentation for API details at:

- <a href="http://127.0.0.1:8000/swagger/" target="_blank">http://127.0.0.1:8000/swagger/</a>
- <a href="http://127.0.0.1:8000/redoc/" target="_blank">http://127.0.0.1:8000/redoc/</a>

### WEB UI

Web interface:

- <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>
- <a href="http://127.0.0.1:8000/post/list/" target="_blank">http://127.0.0.1:8000/post/list/</a>

# Project Structure

This document outlines the structure of the Django project.

## Directory Structure

```

├── README.md # This file
├── docker-compose.yaml # Docker Compose configuration for development
├── Dockerfile # Dockerfile for the main server
├── requirements.txt # Python dependencies
├── .env # Environment variables
├── config # Main Django project folder
│ ├── settings.py # Import Base class here
│ └── ...
├── api/ # Django project api (deprecated)
│ ├── v1/ # api version control
├── apps/ # Django project apps
│ ├── user/ # User management app
│ ├── base/ # Manage soft deletion and default fields
│ │ ├── apps.py
│ │ ├── models.py # Base class imported here
│ │ └── ...
│ ├── post/ # Posts


......
```

## Notes

- The `api/` directory is deprecated and should be replaced by the `apps/` directory.
- The `apps/` directory contains the core Django apps for user management, booking, and football field management.
- The `base/` app handles soft deletion and default fields for other apps.

Feel free to update this structure as your project evolves.
