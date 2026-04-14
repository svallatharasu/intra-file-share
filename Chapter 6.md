# JWT Authentication and Authorization
# Back Story

1. Bearer Token Based Authentication
- User always send the Base64 Password: `Authorization: Bearer <token>`
- Server Store and Client Side Store
- Problems:
    - Less Secure.
    - Easy to intercept without HTTPS.
- Authentication = weak
- Authorization = almost none
- Stateful

--- * --- * --- * --- * ---

2. Session-Based Authentication
- User logs in
- Server creates session
- Stores session in DB/memory
- Send the session ID
- Client sends cookie on every request
- Stateful

( Facebook - Effective use )
- Scalable - nightmaire

--- * --- * --- * --- * ---

3. Token-Based Authentication
- Server gives a token to the client after login.
- Client sends token in headers.

`Authorization: Bearer abc123token`

Advantages:
- Stateless (no session storage)
- Good for APIs

Problems:
- No standard format
- Tokens often random strings
- Server still needs DB lookup

--- * --- * --- * --- * ---

4. OAuth - Delegated Authorization
- Users can login via:
    - Google
    - Facebook

--- * --- * --- * --- * ---

5. JWT Era
- To solve:
    - Stateless authentication
    - Scalable Systems
    - Microservices communication    

{
  "user_id": 123,
  "role": "admin",
  "exp": 1712345678
}

# JWT vs Session

| Feature | JWT | Session |
|---------|-----|---------|
| Stateless | Yes | No |
| Scalable | Yes | No |
| Microservices | Yes | No |
| Storage | Client | Server |
| Security | Good | Better |
| Performance | Better | Good |

# JWT Structure

```
Header.Payload.Signature
```

## Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

## Payload
```json
{
  "user_id": 123,
  "role": "admin",
  "exp": 1712345678
}
```

## Signature
```
HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

# JWT Verification

1. Decode Header
2. Decode Payload
3. Verify Signature
4. Check Expiration
5. Check Claims

# JWT Flow

1. User Login
2. Server Create JWT
3. Client Store JWT
4. Client Send JWT in Header
5. Server Verify JWT
6. Server Send Response

# JWT Security

1. Use HTTPS
2. Use Short Expiration Time
3. Use Refresh Tokens
4. Use Blacklist
5. Use Strong Secret Key

# JWT Best Practices

1. Use Short Expiration Time
2. Use Refresh Tokens
3. Use Blacklist
4. Use Strong Secret Key
5. Use HTTPS
6. Use JWT Libraries
7. Use JWT Validation
8. Use JWT Logging
9. Use JWT Monitoring
10. Use JWT Security

# JWT Libraries

- PyJWT
- python-jose
- authlib
- fastjwt
- pyjwt-async

# JWT Validation

1. Decode Header
2. Decode Payload
3. Verify Signature
4. Check Expiration
5. Check Claims

# JWT Logging

1. Log JWT Creation
2. Log JWT Verification
3. Log JWT Expiration
4. Log JWT Blacklist
5. Log JWT Security

# JWT Monitoring

1. Monitor JWT Creation
2. Monitor JWT Verification
3. Monitor JWT Expiration
4. Monitor JWT Blacklist
5. Monitor JWT Security

# JWT Security

1. Use HTTPS
2. Use Short Expiration Time
3. Use Refresh Tokens
4. Use Blacklist
5. Use Strong Secret Key
6. Use JWT Validation
7. Use JWT Logging
8. Use JWT Monitoring
9. Use JWT Security
10. Use JWT Best Practices

# JWT Example

```python
import jwt
import time

secret = "secret"

# Create JWT
jwt_token = jwt.encode(
    {
        "user_id": 123,
        "role": "admin",
        "exp": time.time() + 3600
    },
    secret,
    algorithm="HS256"
)

# Verify JWT
decoded_token = jwt.decode(jwt_token, secret, algorithms=["HS256"])

print(decoded_token)
```

# JWT vs Session

| Feature | JWT | Session |
|---------|-----|---------|
| Stateless | Yes | No |
| Scalable | Yes | No |
| Microservices | Yes | No |
| Storage | Client | Server |
| Security | Good | Better |
| Performance | Better | Good |

# General JWT Flow:

1. Create_JWT_Config ex: Config
2. Create_Token_Function
3. Login API - Create and Pass the password to the end user.
4. Verify Token Function
5. Protected Route - Check the token is valid or not.

# FastAPI Implemetation
1. Transport - how token is sent (Bearer Header)
2. Strategy - how token is created/verified (JWT)
3. Backend - combines both.

```python

from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

# 1. Transport - how token is sent (Bearer Header)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# 2. Strategy - how token is created/verified (JWT)
jwt_strategy = JWTStrategy(secret="secret", lifetime_seconds=3600)

# 3. Backend - combines both.
auth_backend = AuthenticationBackend(
    name="jwt", # Label
    transport=bearer_transport, # Bearer Transport
    get_strategy=lambda: jwt_strategy, # JWT Strategy
)
```
# AuthenticationBackend combines how the token is sent (BearerTransport) and how it is validated (JWTStrategy).

User registers
→ via get_register_router
User logs in
→ via get_auth_router
→ gets JWT
User accesses protected routes
→ via get_users_router

# Connection of Database Management + User Management
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)