Running feature flipper Private API locally
---

We can run the feature flipper private API locally for development

### Usage

```
make start-ff-private-api
make stop-ff-private-api
```

#### Steps:
* Set the aws credentials for Stormcloud
* Run make start-ff-private-api
* Access the endpoint @ http://localhost:8080/2015-03-31/functions/function/invocations
* Stop the server with ctl+c or Run make stop-ff-private-api

#### Testing the ff endpoint:
Get all sets
```
curl --location --request GET 'http://localhost:5000/sets'
```

GET all features in a set
```
curl --location --request GET 'http://localhost:5000/set/STAGE-assets-default'
```


