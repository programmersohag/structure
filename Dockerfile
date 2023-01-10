# Dockerfile,Image,Container
FROM python:3.9

#add all files
ADD . .
COPY  requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt
CMD ["python","/src/run.py"]