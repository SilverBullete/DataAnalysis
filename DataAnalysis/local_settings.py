import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=1000)

MY_SECRET_KEY = 'dd*avog+)5-1krq6dr3p2ho2!#hz-%w=8@xk4x%8zwyjl5av73'

