# A Flask-Docker-Nginx app

This is a demo app built with an intention to successfully deploy a flask app using docker container and then expose the flask port to a nginx load balancer which further exposes a port 80 to interact with the world.

The root app contains a docker-compose.yml file which builds individual services (flask and nginx) and further makes them available to be consumed.

Nginx app plays a vital role by proxing all the requests coming to port 80 to internally access flask app at port 8080.
This concept can be utilised for a foregrown app where there are multiple instances of the flask app and nginx works as a load balancer to proxy the requests to different servers.

## Dockerfile

Each app (flask and gninx) individaully contain their own *Dockerfile* to build the images.

## Information

The flask app is exposed at *8080*. This is only accessible by interna; services or other services on the same domain.
The nginx app is exposed at port *80*, which actually proxies all the requests to the flask app.

## How to use

Clone the project
> git@github.com:chandanky23/flask-nginx-docker.git (ssh)
> https://github.com/chandanky23/flask-nginx-docker.git (https)

Once the project is downloaded with the default project name (flaskApp or your custome project name, say X) then,
Run the following commands to build the image and start it:

1 - `cd flaskApp(or your custom project name)` to go into your project
2 - `docker-compose build` this may take a while when ran for the first time as it will pull the image to build the container, after that it will be super fast.
3 - `docker-compose up` to run the container. This will execute both the images from flask and nginx and make it available to be used.
