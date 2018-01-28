# Bananas

## Get Bananas

Get all the bananas.

### Request

```
GET /bananas
```

### Response

```
HTTP/1.0 200 OK
Content-Type: application/json
[
  {
    "color": "brown", 
    "id": 1, 
    "name": "bojack", 
    "weight": 4.7
  }, 
  {
    "color": "yellow", 
    "id": 2, 
    "name": "todd", 
    "weight": 3.5
  }, 
  {
    "color": "green", 
    "id": 3, 
    "name": "diane", 
    "weight": 2.9
  }
]
```

## Get Banana

Get a single banana.

### Request

```
GET /bananas/1
```

### Response

```
HTTP/1.0 200 OK
Content-Type: application/json
{
  "color": "brown", 
  "id": 1, 
  "name": "bojack", 
  "weight": 4.7
}
```
