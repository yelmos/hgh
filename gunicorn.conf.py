workers = 8 # 进程数量
worker_class = "gevent" # 采⽤gevent库，⽀持异步处理请求，提⾼吞吐量
bind = "127.0.0.1:8888" # 监听IP放宽，以便于Docker之间、Docker和宿主机之间的通信
