<b> Basic Docker with python API</b>
---
This Repo contains Basic Hello world program. with api and docker file.

Getting Started
---
Make sure You have installed Docker Desktop If no install using this link.
https://www.docker.com/products/docker-desktop/  
Once install run this cmd to confirm  
<code>docker</code>  
To build Docker Image.  
<code>
docker build --tag basic-python-docker:v0.1 .
</code>  
Once Image build run this cmd to check image build successfully.  
<code>docker images</code>  
Once Confirmed. we can run this image using this cmd.  
<code>docker run -p 5000:5000 python-docker </code>  
the above cmd <code>5000:5000</code> left side is the which port the want to run in our local
