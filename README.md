In this Django project, I have implemented a custom user model and a JWT (JSON Web Token) authentication system to handle user registration and login.

The project has the following endpoints:

    /api/register/: This endpoint allows users to register by sending a POST request with the email, password, first name, and last name of the new user in the request body. Upon successful registration, the endpoint returns the serialized data for the new user.

    /api/login/: This endpoint allows users to login by sending a POST request with the email and password of the user in the request body. Upon successful login, the endpoint returns a JWT token and the serialized data for the user.

    /api/logout/: This endpoint allows users to logout by sending a POST request with a valid JWT token in the Authorization header. Upon successful logout, the token is invalidated and the endpoint returns an empty response.# drf-jwt-custom-auth
