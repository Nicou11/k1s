# K1S
- https://hub.docker.com/_/httpd

# 빌드
$ sudo docker build -t my-apache2 .

# 실행
$ sudo docker run -dit --name my-running-app -p 8949:80 my-apache2

# 컨테이너 안으로 접속
$ sudo docker exec -it my-running-app bash

