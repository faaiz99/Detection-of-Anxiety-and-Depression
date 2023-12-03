FROM tiangolo/uvicorn-gunicorn:python3.10


# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade -r requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx


# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# CMD ["uvicorn", "app.main:app","--reload","--host", "0.0.0.0", "--port", "8000"]

CMD ["gunicorn", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0", "--port", "8000"]