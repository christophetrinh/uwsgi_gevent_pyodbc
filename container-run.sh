apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

apt-get update \
    && apt-get install -y msodbcsql17 \
    && apt-get install -y mssql-tools \
    && apt-get install -y unixodbc-dev

# import an sql proc
/opt/mssql-tools/bin/sqlcmd -S mssql -U sa -P MyP@ssw0rd -i /app/mssql/procs.sql

pip install uwsgi==2.0.17.1

pip install -r /app/requirements.txt

bash
