# Dockerfile,Image,Container
FROM python:3.9
#add all files
ADD . .
COPY  requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt
CMD ["python","/src/run.py"]