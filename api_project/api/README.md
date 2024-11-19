# Django REST Framework Token Authentication Setup

This document outlines the steps to configure token-based authentication.


# 1. Token Creation
Tokens are created when a user registers or logs in. I implemented a token retrieval endpoint using DRF’s built-in view:

# python
# from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
  ]


# 2. Token Usage
Clients must include the user's token in the Authorization header of their requests to access protected resources. The format should be:

# Authorization: Token <user_token_here>

For example, using curl:
# curl -X GET http://localhost:8000/api/your-endpoint/ -H "Authorization: Token <your_token>"
