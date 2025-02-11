# Day 4

Today I start in the implementation of the notificaion system

**First** I init the `notifications` app and integerated it with the project , Then i create the Notification model in models.py and write the table and fields depeneds on the DrawSQL shema.

**Secend** I build the serializer for notificaions model

**Third** I build two endpoints :

1. get all user notifications
2. delete notification by notificaion id

> `NOTE`: Before starts in creating the delete endpoint i create custom permission for check if the deleted notification reciver has the same request.user

**Fourth** I write the test files for the two endpoints i created for checking it's worked successfully