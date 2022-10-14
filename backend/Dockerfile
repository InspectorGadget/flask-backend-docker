FROM "python:3.9.15-slim-buster"

# Set labels
LABEL MAINTAINER="InspectorGadget <igadget28@gmail.com>"

# Copy requirements file
COPY ../requirements.txt /home/requirements.txt

# Install requirements
RUN pip install -r /home/requirements.txt

# Copy source code
COPY ../ /home

# Set working directory
WORKDIR /home

# Expose port
EXPOSE 5000

# Change the entrypoint file's permission
RUN chmod u+x ./docker/entrypoint.sh

# Run app
ENTRYPOINT [ "./docker/entrypoint.sh" ]
