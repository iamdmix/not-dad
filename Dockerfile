FROM python:3.11-alpine
RUN apk update && \
apk upgrade && \
apk add bash
USER root
COPY req.txt /root/req.txt
COPY gen_flag /root/gen_flag
COPY main.py /root/main.py
COPY templates /root/templates
RUN chmod +x /root/gen_flag
# RUN /bin/bash /root/gen_flag c0f{something_somethin}
WORKDIR /root
EXPOSE 8080
RUN pip install -r req.txt
CMD ["python", "main.py"]