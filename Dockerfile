FROM python:3.11

ARG USERNAME
ARG PASSWORD

ENV USERNAME ${USERNAME?UsernameNotSet}
ENV PASSWORD ${PASSWORD?PasswordNotSet}

COPY bot.py .

RUN pip install --upgrade pip
RUN pip install instabot==0.108.0
RUN echo "${USERNAME} and ${PASSWORD}"

ENTRYPOINT python bot.py "${USERNAME}" "${PASSWORD}"