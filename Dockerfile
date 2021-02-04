FROM python:3.9-slim

RUN useradd --create-home --shell /bin/bash pipeline_user

RUN mkdir /home/pipeline_user/app

WORKDIR /home/pipeline_user/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER pipeline_user

COPY ./user_data_pipeline .

CMD ["bash"]