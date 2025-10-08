# API Clientes

This is a FastAPI application to manage clients.

## Prerequisites

* Docker
* Docker Compose

## How to run the project

1. Clone the repository.
2. Create a `.env` file with the following content:

```
DATABASE_URL=postgresql://root:utec@db/api_clientes
```

3. Run the following command to start the application:

```
docker-compose up -d
```

The API will be available at `http://{to be defined}:8000`.

## API Endpoints

### GET /api/clientes/lookup

This endpoint allows you to look up a client's ID by their DNI.

**Parameters:**

* `dni` (query parameter, string, required): The DNI of the client to look up. It must be an 8-digit string.

**Responses:**

* **200 OK:** If the client is found, the response will be a JSON object with the client's ID.

```json
{
  "id": 100001
}
```

* **404 Not Found:** If the client is not found.

```json
{
  "detail": "Client not found"
}
```

* **422 Unprocessable Entity:** If the `dni` parameter is invalid.

```json
{
  "detail": [
    {
      "loc": [
        "query",
        "dni"
      ],
      "msg": "ensure this value has at most 8 characters",
      "type": "value_error.any_str.max_length",
      "ctx": {
        "limit_value": 8
      }
    }
  ]
}
```
