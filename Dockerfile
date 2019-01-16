FROM python:3

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - \
   && apt update \
   && apt install -y nodejs

COPY requirements.txt package.json package-lock.json /tmp/
RUN cd /tmp \
   && npm install \
   && pip install -r requirements.txt

COPY . /app
RUN mv /tmp/node_modules /app/node_modules
