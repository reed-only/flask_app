##########################################################
FROM python:3.6.3
##########################################################
ENV PROJECT_DIR=/opt/flask_app \
    TERM=XTERM
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
# Preload requirements to take advance of caching
ADD ./requirements.txt $PROJECT_DIR/requirements.txt
RUN pip3 install -r $PROJECT_DIR/requirements.txt
ADD . $PROJECT_DIR
