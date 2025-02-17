# Instagram Backend Rebuild

This is a Django-based backend project that replicates some of the core functionalities of Instagram. It includes user management, posts, stories, chat, and notifications.

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


