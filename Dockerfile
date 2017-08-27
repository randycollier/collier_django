FROM python:3.5

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

RUN apt-get update ; apt-get --assume-yes install binutils libproj-dev gdal-bin

RUN wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
RUN tar -xjf geos-3.4.2.tar.bz2
RUN cd geos-3.4.2; ./configure; make; make install

RUN wget http://download.osgeo.org/gdal/1.11.0/gdal-1.11.0.tar.gz
RUN tar -xzf gdal-1.11.0.tar.gz
RUN cd gdal-1.11.0; ./configure; make; make install


ENV APP_ROOT /src

WORKDIR ${APP_ROOT}

RUN mkdir /logs
RUN mkdir /config

ADD config/requirements.pip /config/
RUN pip install -r /config/requirements.pip

# Copy project files
COPY . /src

RUN chmod +x /src/docker-entrypoint.sh

EXPOSE 8080

CMD ["/src/docker-entrypoint.sh", "-n"]

