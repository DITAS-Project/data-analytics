# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

Kubernetes API

The Kubernetes v1 [API](https://kubernetes.io/docs/reference/using-api/api-overview/) is required to extract compute metrics of the cluster.

Heketi API

The Heketi [API](https://github.com/heketi/heketi/blob/master/docs/api/api.md) is required to extract the usage metrics of GlusterFS volumes. As Kubernetes does not provide a native solution for that, such APIs are needed on top of the Kubernetes cluster. The endpoint format configured is:

```
hostname/api/v1/namespaces/kube-system/services/heketi:8080/proxy/metrics
```

## Configuration

The needed configuration files are: 

```
/etc/ditas/vdc/data-analytics.json
```
and
```
/opt/blueprint/blueprint.json
```

The Data Analytics gets information about all infrastructure Kubernetes masters from the `COOKBOOK_APPENDIX`, it then matches the information provided in the GET request (`infraId`) with the available infrastructure names. The endpoints are expected to be available on port `9999`.

The `data-analytics.json` file is expected to contain information about the ElasticSearch endpoint:

```
{
    "Port":8080,
    "ElasticSearchURL":"{{.elasticsearch_url}}"
}
```
The index name is compiled in the format:

```python
'{}-*'.format(infraId)
```

Where `infraId` is a query paramter to the metrics GET call.

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://hostname:8080/data-analytics/ui/
```

Your Swagger definition lives here:

```
http://hostname:8080/data-analytics/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
