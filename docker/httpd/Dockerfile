FROM httpd:2.4

ARG REPO_URL=https://github.com/Nicou11/Nicou11.github.io.git

COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "git"]
RUN git clone ${REPO_URL} /usr/local/apache2/blog
#RUN ["git", "clone", "https://github.com/Nicou11/Nicou11.github.io.git", "/usr/local/apache2/blog"]

