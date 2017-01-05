FROM python:2.7

MAINTAINER Ralph Brecheisen <ralph.brecheisen@gmail.com>

COPY sshd_config /dev/ssh-install.sh /root/

ARG AUTH_KEY

RUN /root/ssh-install.sh