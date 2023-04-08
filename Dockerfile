# Install dependencies
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache bash postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# Create app directory and user
RUN adduser -D appuser
RUN mkdir /app /vol
SHELL ["bash", "-c"]
RUN chown -R appuser:appuser /app \
    && chown -R appuser:appuser /vol
USER appuser
WORKDIR /app

# Copy source code and install dependencies
COPY ./requirements.txt /app/requirements.txt
ENV PATH $PATH:/home/appuser/.local/bin
RUN python -m pip install --upgrade pip

# Activate virtual environment and install dependencies
SHELL ["bash", "-c"]
RUN pip install -r requirements.txt \
    && pip install debugpy

# remove all the temporary packages
# USER root
# RUN apk del .tmp-build-deps
# USER appuser

# Copy and set up media and static files directory
COPY . /app/
SHELL ["bash", "-c"]
RUN mkdir -p /vol/web/media /vol/web/static \
    && chmod -R 755 /vol/web


# Set working directory to Django app
WORKDIR /app/src
