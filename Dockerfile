FROM python:3.5

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

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

