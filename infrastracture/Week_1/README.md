# Day 1

First day i searched about the instagram stack which is [Here](https://stackshare.io/instagram/instagram).
Then i Read [This Article](https://medium.com/@kevinljy7/designing-the-backend-of-instagram-305f7a99067b) which
has more usefull informations about designing the instagram in the backend.

> NOTE : instgram was monolithic and after that changed to become a microservices architecture. 

# Instagram Stack in the Back-end ( Not All )
  
- **Python** : Hight level programming language
- **Django** : Back-end framework to build the core of instagram
- **PostgreSQL** : SQL Databases
- **Redis** : In-Memory db used for caching 
- **Gunicorn** : Web server that runs django.
- **Nginx** : Web server that runs on the os and forward the request to gunicorn
- **Celery** : Tool for running the background tasks.
- **RabbitMQ** : Act as a message broker.

### And there is more things you can found it all [from here](https://medium.com/@shaini4020/instagram-tech-stack-f19ddd4dcc0d) 