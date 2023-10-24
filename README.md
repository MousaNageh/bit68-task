# Bit68 Task

Task built by Django, Django Rest framework, PostgreSQL database, nginx and docker 
- providing following features:
  - User registration
  - User login
  - Package table in admin panel only
  - All users could add to subscribe to more than one package
  - Subscription by make order with one or more packages


## Backend dependencies

- [docker](https://docs.docker.com/get-docker/)

## Run Application

#### 1) get a clone from repo or just download it
#### 2) create `.env` file in root directory  
#### 3) Copy `env_files/.env.local` to `.env`
#### 4) run docker compose :

- run the following commnand to build images and run containers
```sh
docker-composer up 
 ```
- or for docker detached mode run :
```sh
docker-composer up --build  -d
 ```
- or for newer vision of docker 
```sh
docker composer up
 ```
### base_url : `http://127.0.0.1:9999`
### admin panel url : `http://127.0.0.1:9999/admin`
### postman collection `bit68.postman_collection.json` in root directory
  - you can import it using postman application, it contains all endpoints 
## APIS

#### register API
- endpoint `POST`: `{{base_url}}/api/oauth/register`
- payload :
```json
{
    "full_name": "user full name",
    "email": "user full email",
    "password": "user password",
    "re_password": "user confirm password"
}
```
- response sample :
```json
{
    "full_name": "test name",
    "email": "test@test.com"
}
```
- notes :
  - all fields are required 
  - password must be at least 8 digits and contains lowercase, uppercase letters,special characters and digits 


#### login API
- endpoint `POST` : `{{base_url}}/api/oauth/login`
- payload :
```json
{
    "email": "user email",
    "password": "user password"
}
```
- response sample :
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDc2MzY2MywiaWF0IjoxNjk4MTcxNjYzLCJqdGkiOiJmZGIzMTMzODcwNzA0YjFkYTMzNDhhZWNiNDIzNmJjZSIsInVzZXJfaWQiOjMsImVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsImZ1bGxfbmFtZSI6Im1vdXNhIG5hZ2VoIn0.M1Wge4zS_r0SDTganoiLM5JQCttvjTKftuth5LiFrlk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwNzYzNjYzLCJpYXQiOjE2OTgxNzE2NjMsImp0aSI6Ijc2NDY4MjVhNDExNTQ2YzJiNTRlYjRmNWFmMGJjY2EyIiwidXNlcl9pZCI6MywiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiZnVsbF9uYW1lIjoibW91c2EgbmFnZWgifQ.dv9UIo903dW4VO-n8vS9UQL5DoXU5Kp50jTZC1XxT4A"
}
```
- notes :
  - refresh token expires after 1 month
  - access token expires every 20 minutes


#### get new access token py refresh token API
- endpoint `POST` : `{{base_url}}/api/oauth/refresh-token`
- payload :
```json
{
    "refresh": "refresh token"
}
```
- response sample :
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MTczMTE0LCJpYXQiOjE2OTgwODcxODksImp0aSI6IjE5NjNiZTlmZjdkNTQ0ZGJiN2E3ZTU3MzUzMTk0YTU4IiwidXNlcl9pZCI6MywiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiZnVsbF9uYW1lIjoibW91c2EgbmFnZWgifQ.eLFbINHkQsQS1uFBw5iod2y9kbmYa4qHkszpN7SjKbI"
}
```

#### package list API
- endpoint `GET` : `{{base_url}}/api/packages/?ordering={optinal}&keyword={optinal}`
- response sample:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "package 1",
            "price": 3443.0
        }
    ]
}
```
- notes :
  - this api required authentication using access token  
  - query parameters `ordering` and `keyword` are optional to pass them
  - if `ordering` is passed the value should be `-price` or `price`:
    - `ordering=-price` is descending order for package
    - `ordering=price` is ascending order for package
  - if `keyword` if passed , will be used to search in packages names

#### user subscription list API
- endpoint `GET` : `{{base_url}}/api/packages/subscription`
- response sample:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "package": {
                "id": 1,
                "name": "fgdgf",
                "price": 3443.0
            }
        }
    ]
}
```
- notes :
  - this api required authentication using access token

#### create  user subscription list API
- endpoint `POST` : `{{base_url}}/api/packages/subscription`
- payload:
```json
{
    "packages": [package_id_1,package_id_2,...]
}
```
- response sample:
```json
{"created": "packages has been created"}
```
- notes :
  - this api required authentication using access token
  - user can can not subscribe to the same package twice  
  - packages ids in the payload must be existed 