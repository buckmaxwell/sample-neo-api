# Sample NeoAPI Project


This project is to give you an idea of how you can leverage [NeoAPI](https://github.com/buckmaxwell/neoapi) in your projects. 

## Getting started

NOTE: Before you test drive this sample API you'll have to get started by installing neo4j on your computer.  It is free to use and kicks ass. http://neo4j.com/

```sh
$ neo4j start
$ export NEO4J_REST_URL=http://<u>:<p>@localhost:7474/db/data
$ # set to location of neo4j instance
$ export BASE_API_URL=http://localhost:10200/v1
$ # This will prefix the endpoints of your api
$ # If it is incorrect, links returned by th api will not work.
$ # NOTE: This is the best place to add a version number ie. /v1
$ 
$ pip install neoapi
$ 
$ python sample_api.py
```
 
### And your off!!

To give this super fly API a test drive open up [Post Man](https://www.getpostman.com/) or [Advance Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=en-US) and try some of the following requests out.  If you get bored with these, read the full [json api specification](http://jsonapi.org/) to see all the neat requests you can make.  This will allow you to discover how to manipulate relationships, paginate, use the includes clause, and all sorts of awesome cheese.

## Example Requests

## Resource Methods

### POST /users

Add a new resource.

URL: http://localhost:10200/users

Request:

```http
Accept: application/vnd.api+json
```

```json
{
  "data": {
    "type": "users",
    "attributes": {
      "email": "ryan@gmail.com",
      "password": "ryan",
      "gender": "m"
    },
    "relationships": {
      "mom": {
        "data": {
          "type": "users",
          "id": "sarah@gmail.com"
        }
      }
    }
  }
}
```

Response:
##### 201 CREATED
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 992 
Location: http://localhost:10200/v1/users/maxbuckdeveloper@gmail.com 
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

```json
{
  "data": {
    "attributes": {
      "active": true, 
      "created": "Sun, 27 Sep 2015 16:54:19 GMT", 
      "email": "ryan@gmail.com", 
      "gender": "m", 
      "id": "ryan@gmail.com", 
      "type": "users", 
      "updated": "Sun, 27 Sep 2015 16:54:19 GMT"
    }, 
    "id": "ryan@gmail.com", 
    "relationships": {
      "friends": {
        "data": [], 
        "links": {
          "related": "http://localhost:10200/v1/users/ryan@gmail.com/friends", 
          "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/friends"
        }
      }, 
      "mom": {
        "data": {
          "id": "sarah@gmail.com", 
          "type": "users"
        }, 
        "links": {
          "related": "http://localhost:10200/v1/users/ryan@gmail.com/mom", 
          "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/mom"
        }
      }
    }, 
    "type": "users"
  }, 
  "links": {
    "self": "http://localhost:10200/v1/users/ryan@gmail.com"
  }
} 
```

### PATCH /users/< id >

Modify an existing resource.

URL: http://localhost:10200/users/ryan@gmail.com

Request:

```http
Accept: application/vnd.api+json
```
```json
{
   "data": {
      "type": "users",
      "attributes": {
         "password": "muchHarderPasswordToGuess"
      }
   }
}
```

Response:
##### 200 OK
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 992 
Location: http://localhost:10200/v1/users/maxbuckdeveloper@gmail.com 
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

```json
{
  "data": {
    "attributes": {
      "active": true, 
      "created": "Sun, 27 Sep 2015 16:54:19 GMT", 
      "email": "ryan@gmail.com", 
      "gender": "m", 
      "id": "ryan@gmail.com", 
      "type": "users", 
      "updated": "Sun, 27 Sep 2015 17:18:38 GMT"
    }, 
    "id": "ryan@gmail.com", 
    "relationships": {
      "friends": {
        "data": [], 
        "links": {
          "related": "http://localhost:10200/v1/users/ryan@gmail.com/friends", 
          "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/friends"
        }
      }, 
      "mom": {
        "data": {
          "id": "sarah@gmail.com", 
          "type": "users"
        }, 
        "links": {
          "related": "http://localhost:10200/v1/users/ryan@gmail.com/mom", 
          "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/mom"
        }
      }
    }, 
    "type": "users"
  }, 
  "links": {
    "self": "http://localhost:10200/v1/users/ryan@gmail.com"
  }
} 
```

### DELETE /users/< id >

Deactivate an existing resource.

URL: http://localhost:10200/users/maxbuckdeveloper@gmail.com

Request:

```http
Accept: application/vnd.api+json
```

Response:
##### 204 NO CONTENT
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 0
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

### GET /users/\<id>

Fetch an existing resource.

URL: http://localhost:10200/users/ryan@gmail.com?include=mom*

**More info on the **include** parameter can be found [here](http://jsonapi.org/format/#fetching-includes)*

Request:

```http
Accept: application/vnd.api+json
```

Response:
##### 200 OK
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 1050
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```
```json
{
  "data": {
    "attributes": {
      "active": true, 
      "created": "Sun, 27 Sep 2015 16:54:19 GMT", 
      "email": "ryan@gmail.com", 
      "gender": "m", 
      "id": "ryan@gmail.com", 
      "type": "users", 
      "updated": "Sun, 27 Sep 2015 17:18:38 GMT"
    }, 
    "id": "ryan@gmail.com", 
    "relationships": {
      "friends": {
        "data": [], 
        "links": {
          "related": "http://localhost:10200/v1/users/ryan@gmail.com/friends", 
          "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/friends"
        }
      }, 
      "mom": {
        "data": {
          "id": "sarah@gmail.com", 
          "type": "users"
        }, 
        "links": {
          "related": "http://localhost:10200/v1/users/ryan@gmail.com/mom", 
          "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/mom"
        }
      }
    }, 
    "type": "users"
  }, 
  "included": [
    {
      "attributes": {
        "active": true, 
        "created": "Sun, 27 Sep 2015 16:54:19 GMT", 
        "email": "sarah@gmail.com", 
        "gender": "f", 
        "id": "sarah@gmail.com", 
        "type": "users", 
        "updated": "Sun, 27 Sep 2015 16:54:19 GMT"
      }, 
      "id": "sarah@gmail.com", 
      "relationships": {
        "friends": {
          "data": [], 
          "links": {
            "related": "http://localhost:10200/v1/users/sarah@gmail.com/friends", 
            "self": "http://localhost:10200/v1/users/sarah@gmail.com/relationships/friends"
          }
        }, 
        "mom": {
          "data": null, 
          "links": {
            "related": "http://localhost:10200/v1/users/sarah@gmail.com/mom", 
            "self": "http://localhost:10200/v1/users/sarah@gmail.com/relationships/mom"
          }
        }
      }, 
      "type": "users"
    }
  ], 
  "links": {
    "self": "http://localhost:10200/v1/users/ryan@gmail.com"
  }
}
```

### GET /users

Fetch a resource collection

URL: http://localhost:10200/users?page[offset]=0&page[limit]=1*

**More info on **pagination** can be found [here](http://jsonapi.org/format/#fetching-pagination)* 

Request:

```http
Accept: application/vnd.api+json
```

Response:
##### 200 OK
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 1061
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```
```json
{
  "data": [
    {
      "attributes": {
        "active": true, 
        "created": "Sun, 27 Sep 2015 16:54:19 GMT", 
        "email": "max@gmail.com", 
        "gender": "m", 
        "id": "max@gmail.com", 
        "type": "users", 
        "updated": "Sun, 27 Sep 2015 16:54:19 GMT"
      }, 
      "id": "max@gmail.com", 
      "relationships": {
        "friends": {
          "data": [], 
          "links": {
            "related": "http://localhost:10200/v1/users/max@gmail.com/friends", 
            "self": "http://localhost:10200/v1/users/max@gmail.com/relationships/friends"
          }
        }, 
        "mom": {
          "data": null, 
          "links": {
            "related": "http://localhost:10200/v1/users/max@gmail.com/mom", 
            "self": "http://localhost:10200/v1/users/max@gmail.com/relationships/mom"
          }
        }
      }, 
      "type": "users"
    }
  ], 
  "links": {
    "first": "http://localhost:10200/v1/users?page[offset]=0&page[limit]=1", 
    "last": "http://localhost:10200/v1/users?page[offset]=2&page[limit]=1", 
    "next": "http://localhost:10200/v1/users?page[offset]=1&page[limit]=1", 
    "self": "http://localhost:10200/v1/users?page[offset]=0&page[limit]=1"
  }
}
```
## Relationship Methods

### POST /users/\<id>/relationships/friends*

Add an item to a relationship collection.

****Note:** use POST for collections with MANY items, otherwise use PATCH*


URL: http://localhost:10200/users/ryan@gmail.com/relationships/friends

Request:

```http
Accept: application/vnd.api+json
```

```json
{
  "data": [
    {
      "type": "users",
      "id": "max@gmail.com",
      "meta": {
        "met": "space camp"
      }
    }
  ]
}
```
Response:
##### 204 NO CONTENT
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 0
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

### PATCH /users/\<id>/relationships/mom

This method does a total replace on a relationship.  It should therefore be used to create relationships with cardinality <= 1.  It can also be used to delete all relationships.


URL: http://localhost:10200/v1/users/ryan@gmail.com/relationships/mom

Request to create:
```http
Accept: application/vnd.api+json
```

```json
{
"data":{"type":"users", "id":"sarah@gmail.com"}
}
```

Request to delete:
```http
Accept: application/vnd.api+json
```
```json
{
"data":null
}
```

Response:
##### 204 NO CONTENT
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 0
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

### DELETE /users/\<id>/relationships/friends

Use this method to delete certain relationships contained in the body.  Only the relationships in the body will be deleted.  This method is only for collections with cardinality > 1.

URL: http://localhost:10200/v1/users/ryan@gmail.com/relationships/friends

Request:
```http
Accept: application/vnd.api+json
```

```json
{
  "data": [
    {
      "type": "users",
      "id": "max@gmail.com"
    }
  ]
}
```

Response:
##### 204 NO CONTENT
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 0
Date: Tue, 15 Sep 2015 04:31:28 GMT
```

### PATCH /users/\<id>/relationships/friends

On collections with cardinality > 1 use this method to delete all existing items in that collection.

URL: http://localhost:10200/v1/users/ryan@gmail.com/relationships/friends

Request:
```http
Accept: application/vnd.api+json
```
```json
{
"data": []
}
```

Response:
##### 204 NO CONTENT
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 0
Date: Tue, 15 Sep 2015 04:31:28 GMT
```

### GET /users/\<id>/relationships/friends

Fetch a relationship.

URL: http://localhost:10200/v1/users/max@gmail.com/relationships/friends

Request:
```http
Accept: application/vnd.api+json
```

```json
{
  "data": [
    {
      "id": "ben@gmail.com", 
      "meta": {
        "created": "Sun, 27 Sep 2015 18:16:47 GMT", 
        "met": "space camp", 
        "type": "friend", 
        "updated": "Sun, 27 Sep 2015 18:16:47 GMT"
      }, 
      "type": "users"
    }, 
    {
      "id": "erik@gmail.com", 
      "meta": {
        "created": "Sun, 27 Sep 2015 18:16:47 GMT", 
        "met": "taco tuesday party", 
        "type": "friend", 
        "updated": "Sun, 27 Sep 2015 18:16:47 GMT"
      }, 
      "type": "users"
    }, 
    {
      "id": "ryan@gmail.com", 
      "meta": {
        "created": "Sun, 27 Sep 2015 18:16:47 GMT", 
        "met": "at atheist revival", 
        "type": "friend", 
        "updated": "Sun, 27 Sep 2015 18:16:47 GMT"
      }, 
      "type": "users"
    }
  ], 
  "included": [
    {
      "attributes": {
        "active": true, 
        "created": "Sun, 27 Sep 2015 18:16:47 GMT", 
        "email": "ben@gmail.com", 
        "gender": "m", 
        "id": "ben@gmail.com", 
        "type": "users", 
        "updated": "Sun, 27 Sep 2015 18:16:47 GMT"
      }, 
      "id": "ben@gmail.com", 
      "relationships": {
        "friends": {
          "data": [
            {
              "id": "max@gmail.com", 
              "type": "users"
            }
          ], 
          "links": {
            "related": "http://localhost:10200/v1/users/ben@gmail.com/friends", 
            "self": "http://localhost:10200/v1/users/ben@gmail.com/relationships/friends"
          }
        }, 
        "mom": {
          "data": null, 
          "links": {
            "related": "http://localhost:10200/v1/users/ben@gmail.com/mom", 
            "self": "http://localhost:10200/v1/users/ben@gmail.com/relationships/mom"
          }
        }
      }, 
      "type": "users"
    }, 
    {
      "attributes": {
        "active": true, 
        "created": "Sun, 27 Sep 2015 18:16:47 GMT", 
        "email": "erik@gmail.com", 
        "gender": "m", 
        "id": "erik@gmail.com", 
        "type": "users", 
        "updated": "Sun, 27 Sep 2015 18:16:47 GMT"
      }, 
      "id": "erik@gmail.com", 
      "relationships": {
        "friends": {
          "data": [
            {
              "id": "max@gmail.com", 
              "type": "users"
            }
          ], 
          "links": {
            "related": "http://localhost:10200/v1/users/erik@gmail.com/friends", 
            "self": "http://localhost:10200/v1/users/erik@gmail.com/relationships/friends"
          }
        }, 
        "mom": {
          "data": null, 
          "links": {
            "related": "http://localhost:10200/v1/users/erik@gmail.com/mom", 
            "self": "http://localhost:10200/v1/users/erik@gmail.com/relationships/mom"
          }
        }
      }, 
      "type": "users"
    }, 
    {
      "attributes": {
        "active": true, 
        "created": "Sun, 27 Sep 2015 16:54:19 GMT", 
        "email": "ryan@gmail.com", 
        "gender": "m", 
        "id": "ryan@gmail.com", 
        "type": "users", 
        "updated": "Sun, 27 Sep 2015 17:18:38 GMT"
      }, 
      "id": "ryan@gmail.com", 
      "relationships": {
        "friends": {
          "data": [
            {
              "id": "max@gmail.com", 
              "type": "users"
            }
          ], 
          "links": {
            "related": "http://localhost:10200/v1/users/ryan@gmail.com/friends", 
            "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/friends"
          }
        }, 
        "mom": {
          "data": null, 
          "links": {
            "related": "http://localhost:10200/v1/users/ryan@gmail.com/mom", 
            "self": "http://localhost:10200/v1/users/ryan@gmail.com/relationships/mom"
          }
        }
      }, 
      "type": "users"
    }
  ], 
  "links": {
    "first": "http://localhost:10200/v1/users/max@gmail.com/relationships/friends?page[offset]=0&page[limit]=20", 
    "last": "http://localhost:10200/v1/users/max@gmail.com/relationships/friends?page[offset]=0&page[limit]=20", 
    "related": "http://localhost:10200/v1/users/max@gmail.com/friends", 
    "self": "http://localhost:10200/v1/users/max@gmail.com/relationships/friends?page[offset]=0&page[limit]=20"
  }
}
```







