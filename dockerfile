## Base Image
FROM  python:3.12


# WorkDir

WORKDIR /myfastapi

COPY requirements.txt .

## run
RUN pip install --no-cache-dir -r requirements.txt

## Copy
COPY . .

# Port Expose
EXPOSE 8000


CMD [ "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000" "--reload" ]