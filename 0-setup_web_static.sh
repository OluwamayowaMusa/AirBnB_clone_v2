#!/usr/bin/env bash
# Sets up web servers for the deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo cat << EOF | sudo tee /data/web_static/releases/test/index.html
<!DOCTYPE html>
<hmtl>
  <head>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>
EOF
sudo ln -s -f /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
