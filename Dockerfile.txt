FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /dockercap/app.py
ADD . /dockercap
WORKDIR /dockercap
RUN pip install Flask==1.0.2
EXPOSE 8000
CMD ["python", "app.py"]