sudo docker run --user=1000:1000 -e CLOWDER_URL=http://clowder:9000 -e CLOWDER_LOGIN=ruian2@illinois.edu -e CLOWDER_PASSWORD=chenghuan1996117 -it --net clowderdeployment_default -v ${PWD}:/home/clowder paleo_extractor
#sudo docker run -e CLOWDER_URL=http://clowder:9000 -e CLOWDER_LOGIN=ruian2@illinois.edu -e CLOWDER_PASSWORD=chenghuan1996117 -it --net clowderdeployment_default paleo_extractor
