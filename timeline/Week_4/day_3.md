# Day 3

Today i create a lot of staff like create two endpoints :

1. endpoint for update post by id
2. endpoint for get user posts by username

And write a `timeline` logic for each get all posts request,The timeline posts are filter the posts by the user following then order it by latest and most liked posts.

I implement caching for posts by using redis for cache, And use pagination in some endpoints.

Then After doing all theses staff i wrote test file for posts app and check all thing is running correctly