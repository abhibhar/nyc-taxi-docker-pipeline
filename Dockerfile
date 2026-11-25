FROM python:3.13-slim
RUN pip install pandas
WORKDIR /code
COPY app.py .
RUN mkdir output
ENTRYPOINT ["python", "app.py"]