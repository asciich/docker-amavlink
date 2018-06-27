FROM asciich/python2_pipgcc

MAINTAINER Reto Hasler <reto.hasler@asciich.ch>

RUN sed -i 's/, int,/, unsigned int,/' /usr/include/assert.h && \
    pip install git+https://github.com/asciich/flightcontroller.git/#subdirectory=tools/amavlink
