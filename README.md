# opencv

## requirements

```bash
# python3 support
$ sudo apt-get install python3-dev python3-numpy

# GTK support
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
$ sudo apt-get install libgtk-3-dev
```

## build opencv
```bash
$ git clone https://github.com/opencv/opencv.git
$ cd opencv
$ mkdir build
$ cd build

# set python path
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D PYTHON3_LIBRARY=/home/youjin2/venvs/py3/lib/python3.6/config-3.6m-x86_64-linux-gnu/libpython3.6m.a \
    -D PYTHON3_INCLUDE_DIR=/home/youjin2/venvs/py3/include/python3.6m \
    -D PYTHON3_EXECUTABLE=/home/youjin2/venvs/py3/bin/python \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=ON ..

$ make -j 8
$ sudo make install

# create symbolc link in user's virtualenv (change opencv path appropriately)
$ cd /home/youjin2/venvs/py3/lib/python3.6/site-packages
$ ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.cpython-36m-x86_64-linux-gnu.so cv2.so
```

## Issues
___
Python (for build): /usr/bin/python2.7 -- this only means, that py27 will be run to generate the
wrappers ,but it will still build them for python3.5 (most likely,because thisis the only python
with a proper numpy on your box)
___
* https://answers.opencv.org/question/183004/install-opencv3-with-python3python3-numpy/
* https://medium.com/coding-experiences/setting-up-opencv3-with-python3-on-macos-84be7909e28d


## img sources
https://github.com/dltpdn/insightbook.opencv_project_python
