# Number of worker processes
workers = 4  # Typically 2-4 times the number of CPU cores

# Worker class (determines how requests are handled)
worker_class = 'gthread'  # Other options: 'sync', 'gevent', 'eventlet'

# Number of threads per worker (useful for I/O-bound tasks)
threads = 2  # Adjust as needed

# Bind address and port
bind = '0.0.0.0:8000'  # Adjust to your desired port

# Maximum requests a worker can handle before being restarted
max_requests = 500  # Helps avoid memory leaks
max_requests_jitter = 50  # Adds randomness to restart timing

# Timeout for worker processes
timeout = 30  # Adjust based on your app's characteristics

# Log level (controls logging verbosity)
loglevel = 'info'

# Log output (standard output for simplicity)
accesslog = '-'
errorlog = '-'

# Process name (helps identify processes in a process manager)
proc_name = 'my_flask_app'