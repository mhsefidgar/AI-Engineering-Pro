# HTTP

HTTP is the application protocol behind most backend APIs.

## Core concepts

- Request: method, URL, headers, optional body
- Response: status code, headers, optional body
- Methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- Status classes: `2xx` success, `3xx` redirection, `4xx` client error, `5xx` server error
- Headers carry metadata such as content type, authorization, caching, and correlation IDs.

## Backend request lifecycle

```text
Client -> DNS/TLS -> server -> router -> middleware -> handler -> service -> database
                                                              -> response
```

## Production concerns

Use HTTPS, explicit timeouts, structured errors, request IDs, input validation, rate limiting, and safe logging. Do not log passwords, access tokens, or API keys.

## Exercise

Design a `POST /users` request and document its request body, success response, validation failures, and authentication requirements.