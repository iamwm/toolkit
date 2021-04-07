#!/bin/bash
wget -c https://github.com/davisking/dlib/archive/v19.17.tar.gz
tar -xzvf v19.17.tar.gz
cd dlib-19.17/ || exit 1
mkdir build
cd build || exit 1
cmake ..
cmake --build .
echo 'dlib installed'

# then install setup.py
cd ..
### Ubuntu
# apt-get install python3.6-dev
python3 setup.py install
pip3 install face_recognition==1.2.3
echo 'face_recognition installed'
exit 0
