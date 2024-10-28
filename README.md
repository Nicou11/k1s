# K1S
- https://hub.docker.com/_/httpd


## BUILD & RUN
```bash

# 빌드
$ sudo docker build -t my-apache2 .

# 실행
$ sudo docker run -dit --name my-running-app -p 8949:80 my-apache2

# 컨테이너 안으로 접속
$ sudo docker exec -it my-running-app bash
```

## nginx_lb 연결
```bash

# default.conf 수정
server blog-1:80;
server blog-2:80;
server blog-3:80;

# 실행
$ sudo docker run -d --name blog-1 --rm blog
$ sudo docker run -d --name blog-2 --rm blog
$ sudo docker run -d --name blog-3 --rm blog

# lb 연결
$ sudo docker run -d --name nginx_lb -p 8949:80 --link blog-1 --link blog-2 --link blog-3 --rm lb

```

