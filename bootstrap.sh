#!/usr/bin/env bash

apt-get update
apt-get upgrade

apt-get install -y python3
apt-get install -y python3-pip

python3 --version
pip3 --version
pip --version

pip install --upgrade pip --user
pip install --upgrade pip
pip --version



# install spaCy
pip3 install -U spacy

# download spaCy models
python3 -m spacy download en
python3 -m spacy download xx

# download all spaCy training models
python3 -m spacy download xx_ent_wiki_sm

# download spaCy english training models
python3 -m spacy download en_core_web_sm
python3 -m spacy download en_core_web_md
python3 -m spacy download en_core_web_lg
python3 -m spacy download en_vectors_web_lg

# install NLTK
pip3 install -U nltk
python3 -m nltk.downloader all

# install numpy
pip3 install -U numpy

# command to test db connection
# psql -h localhost -p 5432 -U postgres feedback

# command to run application using gunicorn3
#gunicorn3 feedbackaware.wsgi:application     --bind 127.0.0.1:8080     --workers 4


if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi
