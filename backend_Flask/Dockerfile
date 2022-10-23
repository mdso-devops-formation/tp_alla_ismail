FROM python:3.10
WORKDIR /app
COPY . .
RUN python -m pip install -r requirements.txt
EXPOSE 3000
CMD ["uvicorn","main:main" ,"--reload"]