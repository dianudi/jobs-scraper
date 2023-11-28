FROM python:alpine

LABEL version="1.0.0"
LABEL description="Jobs scraper from various social media and websites."

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "" ]