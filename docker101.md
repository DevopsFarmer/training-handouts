# run container
docker run -d -p 5001:5000 python-flask-app:v1

## run coaniner in tty and interacitve mode. Helps in debugging
docker run -it busybox:latest


# list container (running)
docker ps

## stop container
# docker stop <container id>


## list all the container(stopped/running/creatting)
docker ps --all


## start a container in stopped state
docker start <container id>


## removing the container
docker rm <container id>  # remove stopped container
docker rm -f  <container id> # force delete the container(running or stopped)


bonus: how to remove all the containers from system - 
```
docker ps --all |awk '{print $1}' | xargs docker rm
```


## working with images
### list images on local machine
docker images
docker pull <imagename> # download image from default docker registry
docker push <imagename:tag> # uploads image to default docker registry

docker pull devopsfarm/python-flask-app:latest
docker run -d -p 5001:5000 devopsfarm/python-flask-app:latest

docker build -- build a docker images
### remove images
docker image rm <imageid>

## get logs of the running/stopped contaienr
docker logs ba9f9fdf59b7 -f

### Excerise

Create node js hello world application
Run the app on local machine
Access the application from browser

Containerize the image (create Dockerfile)
Build the image
Run the image locally and with port forwarding.
Access the application

Login to dockerhub and create repository for nodejs application
Retag the docker image on local to dockerhub imagename
Push the image to dockerhub


Run the container from dockerhub image on any other system. (playground docker)

