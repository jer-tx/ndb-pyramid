FROM gcr.io/google-appengine/python

# Create a virtualenv for dependencies. This isolates these packages from
# system-level packages.
# Use -p python3 or -p python3.7 to select python version. Default is version 2.
RUN virtualenv /env -p python3

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV PYTHONUNBUFFERED 0
# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt /app/requirements.txt
ADD gcp-iam-key.json /app/gcp-iam-key.json
ENV GOOGLE_APPLICATION_CREDENTIALS /app/gcp-iam-key.json
RUN pip install -r /app/requirements.txt

# Add the application source code.
ADD . /app

# Run a WSGI server to serve the application. gunicorn must be declared as
# a dependency in requirements.txt.
RUN pip install -e .

CMD pserve development.ini
