FROM python:3
ADD SubjectDetection.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python3", "SubjectDetection.py" ]