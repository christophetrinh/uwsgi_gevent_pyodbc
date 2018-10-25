FROM python:3.6

# cleanup
RUN apt-get update \
    && apt-get install -y  \
        apt-transport-https \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y build-essential \
    && apt-get install -y apt-utils \
    && apt-get install -y dialog


RUN pip install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools


RUN su
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit


CMD bash
