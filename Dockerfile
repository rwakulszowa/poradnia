FROM python:3-slim
RUN mkdir /code /code/production
WORKDIR /code

# Install python dependencies
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y\
    libmysqlclient-dev \
    gcc \
    build-essential \
    curl
COPY requirements/*.txt ./requirements/
RUN pip install --no-cache-dir pip wheel -U
RUN pip install --no-cache-dir -r requirements/local.txt 'django<2.0' && pip install --no-cache-dir -r requirements/test.txt 'django<2.0'
# Install NodeJS dependencies
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs
COPY package.json package-lock.json ./
RUN npm install
# Finish setup
ENTRYPOINT ["bash", "docker-entrypoint.sh"]
COPY . /code/
