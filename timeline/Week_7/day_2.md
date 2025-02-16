# Day 2

Today I started to add rate-limiting to the system, for security reasons , and add rate-limiting in 3 cases : 

- 100 request per day for anonymous users on every endpoint except login
- 500 request per day for authenticated users on every endpoint except login
- 10 request per hour for any user on login endpoint

After that I create new endpoint `/__docs__/` for documentation and i use swagger for write the docs on the endpoints on of the system.