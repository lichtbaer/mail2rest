FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install imap_tools

COPY ./app /app
EXPOSE 80
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]