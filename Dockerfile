# Dockerfile,Image,Container

FROM python:3.9

ADD src/run.py .

COPY  requirements.txt ./src/requirements.txt

RUN pip install -r /src/requirements.txt

CMD ["python","/run.py"]