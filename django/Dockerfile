FROM ubuntu:14.04

# System requirements installation

RUN apt-get update && \
	apt-get install -y libxml2-dev libxslt1-dev python3-dev python3-setuptools python3.4 build-essential python3-pip nginx libpq-dev mysql-client libmysqlclient-dev curl postgresql-client && \
	apt-get --assume-yes install -f libjpeg-dev zlib1g-dev && \
	ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib && \
	ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib && \
	ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# Encoding fix for correct UTF handling in python packages

RUN sudo locale-gen "en_US.UTF-8"
ENV LC_CTYPE "en_US.UTF-8"
ENV LC_NUMERIC "en_US.UTF-8"
ENV LC_TIME "en_US.UTF-8"
ENV LC_COLLATE "en_US.UTF-8"
ENV LC_MONETARY "en_US.UTF-8"
ENV LC_MESSAGES "en_US.UTF-8"
ENV LC_PAPER "en_US.UTF-8"
ENV LC_NAME "en_US.UTF-8"
ENV LC_ADDRESS "en_US.UTF-8"
ENV LC_TELEPHONE "en_US.UTF-8"
ENV LC_MEASUREMENT "en_US.UTF-8"
ENV LC_IDENTIFICATION "en_US.UTF-8"
RUN locale

# Python packages installation

COPY ./src/requirements.txt /opt/app/requirements.txt
COPY ./src/requirements-develop.txt /opt/app/requirements-develop.txt
RUN pip3 install -r /opt/app/requirements.txt

# Copying application code into container

COPY ./src/ /opt/app/

WORKDIR /opt/app

# Creating secret application code if not exists

RUN if [ ! -f secret_key.txt ]; then openssl rand -base64 32 > secret_key.txt; fi

# Collecting static files

RUN python3 /opt/app/manage.py collectstatic --settings=project.settings_production --noinput

# Nginx setup

RUN rm /etc/nginx/sites-enabled/default;
COPY ./deploy/backend-nginx.conf /etc/nginx/sites-enabled/

# Start uwsgi and nginx

COPY ./deploy/start_in_docker.sh /opt/app/start_in_docker.sh
COPY ./deploy/uwsgi_params /opt/app/
RUN chmod +x start_in_docker.sh;
CMD ./start_in_docker.sh;

EXPOSE 80
