# 部署

### Docker部署
```
docker build -t clockin:v1 .

docker run --name clock_server_v1 -p 9090:8000 -d clockin:v1 bash

浏览器运行:
http://localhost:9090/


docker run -d \
  --name clock_server_v4 \
  --mount source=myvol,target=/app \
  -p 9092:8000 -d clockin:v1 bash
```