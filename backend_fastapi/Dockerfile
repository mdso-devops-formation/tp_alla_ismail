FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT ["uvicorn","main:app" ,"--reload"]