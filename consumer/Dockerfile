FROM okteto/python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
EXPOSE 8080
CMD ["python", "app.py" ]