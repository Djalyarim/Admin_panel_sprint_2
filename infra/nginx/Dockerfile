FROM nginx:1.19.2

WORKDIR .
RUN rm /etc/nginx/conf.d/default.conf
# ADD config/nginx-site.conf /etc/nginx/conf.d/nginx.conf
# COPY nginx.conf /etc/nginx/
COPY conf.d /etc/nginx/conf.d
# COPY static /code/static/