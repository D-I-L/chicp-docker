# chicp-docker
CHiCP installation using Docker containers

For Ubuntu

Install Docker and Docker-compose. Follow instruction <a href='https://docs.docker.com/engine/installation/linux/ubuntulinux/'>here</a>

Follow the steps:
docker-compose build
docker-compose up postgres    # creates webuser role
docker stop $(docker ps -q)
docker-compose up

Ensure that you have the elasticsearch data in the right place, as pointed by config file (elasticsearch.yml) 
path.repo: ['/usr/share/elasticsearch/repo']
path.data: ['/usr/share/elasticsearch/data']
