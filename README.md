# Instagram Backend Rebuild

This is a Django-based backend project that replicates some of the core functionalities of Instagram. It includes user management, posts, stories, chat, and notifications.

## Tools in this project
- **Python :** Hight level programming language
- **Django :**  Back-end framework.
- **PostgreSQL :** SQL Databases
- **Redis :** No-SQL db used for caching and message broker
- **Gunicorn :** WSGI HTTP Server.
- **Nginx :** Web server that runs on the os and forward the request to Django server and use it as load balancer
- **Celery :** Tool for running the background tasks.
- **Celery Beat :** Implement periodic tasks.
- **JWT :** Used for tokenization
- **REST APIs :** Used for create REST endpoints on the system except posts endpoints.
- **GraphQL :** Type of APIs but i use it only in posts endpoints.
- **Daphne :** Daphne is a HTTP, HTTP2 and WebSocket protocol server.
- **Docker :** for continarize the project and run multiple images on it.


## Features

- **User Management**: Register, login, and manage user profiles.
- **Posts**: Create, read, update, and delete posts.
- **Stories**: Upload and view stories that disappear after 24 hours.
- **Chat**: Real-time messaging between users.
- **Notifications**: Get notified about new followers and likes.

## API Documentation

The API documentation is available using Swagger UI. You can access it at the following endpoint:

[`http://localhost/__docs__/`](http://localhost/__docs__/)




## API Endpoints
- **User Management:** `api/v1/user/`
- **Posts:** `api/v1/posts/`
- **Stories:** `api/v1/story/`
- **Chat:** `api/v1/chat/`
- **Notifications:** `api/v1/notifications/`


## Web Socket Endpoints 
- **Chat:** `/ws/chat/<chat_id>/`
- **Notificaion:** `/ws/notificaions/`



## Setting Env file

1. Create `.env` file in code/core folder
2. set theses variables : 
    ```bash
    FB_CLIENT_ID = ""
    FB_CLIENT_SECRET = ""
    FRONTEND_END_SERVER_REDIRECT_URL = "http://localhost:8000/"
    
    # You can use these variable with its values
    REDIS_URL = "redis://redis:6379"
    CELERY_BROKER_URL = "redis://redis:6379/1"
    CELERY_RESULT_BACKEND = "redis://redis:6379/2"
    ```

## Installation

> NOTE: You must have docker to run this project.

To set up this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RadwanHegazy/instagram
    ```
    ```bash
    cd instagram/code/core
    ```


2. **Running Via Docker**
    ```bash
    docker-compose up
    ```


