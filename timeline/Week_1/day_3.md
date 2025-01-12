# Day 3

Today we will going to talk about each tool that we will use 
to re-build instagram.

### Python

python is a high-level programming language that we 
will use to write code using it.

### Django

Django is a backend framework that we will use it 
to write system logic and deal with db and do any logic staff.


### PostgreSQL

SQL database that we will use it to save personal inframation like
user info , posts and all the data of the system.


### JWT

Json Web Token, We will use it for tokenization and generate 
the access and refresh token, And by this token the client could 
access the data.


### Celery

we will use celery for implementing the background tasks which is 
heavy and can make the main server become slow


### Redis

The main usage of redis on this project is for two reasons,First reason is to do caching and the secend reason that to use it 
as a message broker.


### Web Socket

Beacuse there is some real-time actions like sending notifications and chating between users we will use web socket protocol for do these staff.

### Daphne

A web server that we will use it to run our django project throw it, Because this web server support web socket protocol and http protocol. 


### Nginx

Nginx do a lot of staff and we will use it to act as a load balancer.


### GraphQL

As we know the instagram use GrqhQL which is a type of APIs but has some good advantages, we will use it for only in the posts endpoints.

### REST APIs

This is also a one type of a types of APIs and all the system will depends on it only the posts section.


### Docker

A tool that we will use it to run all theses services on it