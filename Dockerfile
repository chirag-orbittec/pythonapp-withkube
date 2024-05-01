#From python 3.11 stable image
FROM python:3.11.9-bullseye

#Install poetry in the container


RUN pip install poetry

#Copy farmeasy folder to the container
COPY app.py /app/
COPY pyproject.toml /app/
COPY poetry.lock /app/
# Install the dependencies from poetry.lock
# Set the working directory in the container
WORKDIR /app/

RUN poetry install --no-dev


# Expose the port the app runs on
EXPOSE 8000


# Run the app
CMD ["poetry", "run", "python", "app.py"]
