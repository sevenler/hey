[group:tornados]
programs=hey-0, hey-1

[program:hey-0]
command=python /data/hey/app.py --port=8010
directory=/data/hey/
user=www-data
autorestart=true
redirect_stderr=true
stdout_logfile=/data/log/supervisor/tornado/hey-0.log
loglevel=info

[program:hey-1]
command=python /data/hey/app.py --port=8011
directory=/data/hey/
user=www-data
autorestart=true
redirect_stderr=true
stdout_logfile=/data/log/supervisor/tornado/hey-1.log
loglevel=info

[supervisord]
