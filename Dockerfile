FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir \
    fastapi uvicorn[standard] sqlalchemy pymysql alembic python-dotenv pydantic \
    python-jose email-validator cryptography \
    "passlib==1.7.4" "bcrypt==3.2.2"

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
