# Day 2

Today I worked in posts, i create posts app then i build the Post and PostImage models in posts/models.py file, i use my db [schema](https://drawsql.app/teams/test-1748/diagrams/instagram) to create the models.

After creating the models i build the serializers which i will use it for posts and posts images endpoints,Then i create a custom permission object called IsPostOwner for using it as a permission for any change by the owner of the post.

The endpoints which i created today : 

1. get all posts
2. retrive post by id
3. delete post by id
4. create post

