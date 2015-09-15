# Sample NeoAPI Project


This project is to give you an idea of how you can leverage [NeoAPI](https://github.com/buckmaxwell/neoapi) in your projects. 

## Getting started

NOTE: Before you test drive this sample API you'll have to get started by installing neo4j on your computer.  It is free to use and kicks ass. http://neo4j.com/

```sh
$ neo4j start
$ export NEO4J_REST_URL=http://<u>:<p>@localhost:7474/db/data
$ # set to location of neo4j instance
$ export BASE_API_URL=http://localhost:10200
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

### POST /users
URL: http://localhost:10200/users

Request:

```http
Accept: application/vnd.api+json
```

```json
	{
		"data":
		{
		    "type":"users",
		    "attributes":
		    {
		        "email": "maxbuckdeveloper@gmail.com",
		        "password":"max",
		        "gender": "m"
		    }
		}
	}

```

Response:
##### 201 CREATED
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 992 
Location: http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com 
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

```json
	{
		"data": {
		    "attributes": {
				"active": true, 
				"created": "Tue, 15 Sep 2015 00:28:29 GMT", 
				"email": "maxbuckdeveloper@gmail.com", 
				"gender": "m", 
				"id": "maxbuckdeveloper@gmail.com", 
				"updated": "Tue, 15 Sep 2015 00:28:29 GMT"
			}, 
			"id": "maxbuckdeveloper@gmail.com", 
			"relationships": {
				"friends": {
					"data": [], 
					"links": {
						"related": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/friends", 
						"self": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/relationships/friends"
					}
				}, 
				"mom": {
				"data": null, 
				"links": {
				  "related": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/mom", 
				  "self": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/relationships/mom"
				}
				}
				}, 
			"type": "users"
			}, 
	  "links": {
	    "self": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com"
	  }
	}
```

### PATCH /users/< id >

URL: http://localhost:10200/users/maxbuckdeveloper@gmail.com

Request:

```http
Accept: application/vnd.api+json
```
```json
	{
			"data":
			{
			    "type":"users",
			    "attributes":
			    {
			        "password":"MUCHharderPasswordTOGuess"
			    },
			    "relationships":
			    { 
			          "friends": {
			              "data":[
                          	{"type":"users", "id":"billgates@apple.com"}, 								{"type":"users", "id":"stevewozniak@mictosoft.com"}
                          ]
			           },
			           "mom": {
			               "data": {"type":"users", "id":"christina@gmail.com"}
			           }
			    }
			}
		}
```

Response:
##### 200 OK
```http
Content-Type: application/vnd.api+json; charset=utf-8 
Content-Length: 992 
Location: http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com 
Date: Tue, 15 Sep 2015 04:31:28 GMT 
```

```json
	{
		  "data": {
		    "attributes": {
		      "active": true, 
		      "created": "Tue, 15 Sep 2015 00:28:29 GMT", 
		      "email": "maxbuckdeveloper@gmail.com", 
		      "gender": "m", 
		      "id": "maxbuckdeveloper@gmail.com", 
		      "updated": "Tue, 15 Sep 2015 01:08:09 GMT"
		    }, 
		    "id": "maxbuckdeveloper@gmail.com", 
		    "relationships": {
		      "friends": {
		        "data": [
		          {
		            "id": "billgates@apple.com", 
		            "type": "users"
		          }, 
		          {
		            "id": "stevewozniak@mictosoft.com", 
		            "type": "users"
		          }
		        ], 
		        "links": {
		          "related": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/friends", 
		          "self": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/relationships/friends"
		        }
		      }, 
		      "mom": {
		        "data": {
		          "id": "christina@gmail.com", 
		          "type": "users"
		        }, 
		        "links": {
		          "related": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/mom", 
		          "self": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com/relationships/mom"
		        }
		      }
		    }, 
		    "type": "users"
		  }, 
		  "links": {
		    "self": "http://localhost:5000/v1/users/maxbuckdeveloper@gmail.com"
		  }
		}
```

### DELETE /users/< id >

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

### GET /users/< id >
URL: http://localhost:10200/users/billgates@apple.com?include=friends

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
		      "created": "Tue, 15 Sep 2015 00:28:29 GMT", 
		      "email": "billgates@apple.com", 
		      "gender": "m", 
		      "id": "billgates@apple.com", 
		      "updated": "Tue, 15 Sep 2015 01:34:08 GMT"
		    }, 
		    "id": "billgates@apple.com", 
		    "relationships": {
		      "friends": {
		        "data": [
		          {
		            "id": "stevewozniak@mictosoft.com", 
		            "type": "users"
		          }
		        ], 
		        "links": {
		          "related": "http://localhost:5000/v1/users/billgates@apple.com/friends", 
		          "self": "http://localhost:5000/v1/users/billgates@apple.com/relationships/friends"
		        }
		      }, 
		      "mom": {
		        "data": null, 
		        "links": {
		          "related": "http://localhost:5000/v1/users/billgates@apple.com/mom", 
		          "self": "http://localhost:5000/v1/users/billgates@apple.com/relationships/mom"
		        }
		      }
		    }, 
		    "type": "users"
		  }, 
		  "included": [
		    {
		      "attributes": {
		        "active": true, 
		        "created": "Tue, 15 Sep 2015 00:28:29 GMT", 
		        "email": "stevewozniak@mictosoft.com", 
		        "gender": "m", 
		        "id": "stevewozniak@mictosoft.com", 
		        "updated": "Tue, 15 Sep 2015 00:28:29 GMT"
		      }, 
		      "id": "stevewozniak@mictosoft.com", 
		      "relationships": {
		        "friends": {
		          "data": [
		            {
		              "id": "billgates@apple.com", 
		              "type": "users"
		            }
		          ], 
		          "links": {
		            "related": "http://localhost:5000/v1/users/stevewozniak@mictosoft.com/friends", 
		            "self": "http://localhost:5000/v1/users/stevewozniak@mictosoft.com/relationships/friends"
		          }
		        }, 
		        "mom": {
		          "data": null, 
		          "links": {
		            "related": "http://localhost:5000/v1/users/stevewozniak@mictosoft.com/mom", 
		            "self": "http://localhost:5000/v1/users/stevewozniak@mictosoft.com/relationships/mom"
		          }
		        }
		      }, 
		      "type": "users"
		    }
		  ], 
		  "links": {
		    "self": "http://localhost:5000/v1/users/billgates@apple.com"
		  }
		}
```

### GET /users
URL: http://localhost:10200/users?page[offset]=0&page[limit]=1

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
		        "created": "Tue, 15 Sep 2015 00:28:29 GMT", 
		        "email": "billgates@apple.com", 
		        "gender": "f", 
		        "id": "billgates@apple.com", 
		        "updated": "Tue, 15 Sep 2015 00:28:29 GMT"
		      }, 
		      "id": "billgates@apple.com", 
		      "relationships": {
		        "friends": {
		          "data": [], 
		          "links": {
		            "related": "http://localhost:5000/v1/users/billgates@apple.com/friends", 
		            "self": "http://localhost:5000/v1/users/billgates@apple.com/relationships/friends"
		          }
		        }, 
		        "mom": {
		          "data": null, 
		          "links": {
		            "related": "http://localhost:5000/v1/users/billgates@apple.com/mom", 
		            "self": "http://localhost:5000/v1/users/billgates@apple.com/relationships/mom"
		          }
		        }
		      }, 
		      "type": "users"
		    }
		  ], 
		  "links": {
		    "first": "http://localhost:5000/v1/users?page[offset]=0&page[limit]=1", 
		    "last": "http://localhost:5000/v1/users?page[offset]=6&page[limit]=1", 
		    "next": "http://localhost:5000/v1/users?page[offset]=1&page[limit]=1", 
		    "self": "http://localhost:5000/v1/users?page[offset]=0&page[limit]=1"
		  }
		}
```



### DELETE /users/< id>/relationships/friends/< id>


And of course, the inevitable end of steve and bills friendship.  Both bill and steve will still exist as users after this operation, but their relationship will be no more.

URL: http://localhost:10200/users/billgates@apple.com/relationships/friends/stevewozniak@mictosoft.com

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




