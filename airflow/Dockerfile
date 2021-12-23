ARG AIRFLOW_IMAGE

FROM $AIRFLOW_IMAGE

ARG version

COPY packages.txt .
USER root
RUN if [[ -s packages.txt ]]; then \
        apt-get update -y && cat packages.txt | xargs apt-get install -y --no-install-recommends \
        && apt-get autoremove -yqq --purge \
        && rm -rf /var/lib/apt/lists/*; \
    fi

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/9/prod.list  > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get -y install --no-install-recommends \
    libsasl2-dev \
    msodbcsql17 \
    mssql-tools \
    unixodbc-dev
RUN apt-get clean

RUN echo "$version"

COPY requirements.txt .
USER airflow
RUN pip install --no-cache-dir --user -q -r requirements.txt

RUN git clone https://github.com/LCBRU/airflow_dags.git /opt/airflow/dags/

COPY webserver_config.py .