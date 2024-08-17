```bash
> git clone "https://github.com/RvTechiNNovate/face_recog_dlib_file.git"
```
Cloning into 'face_recog_dlib_file'... <br>
remote: Enumerating objects: 15, done. <br>
remote: Counting objects: 100% (15/15), done. <br>
remote: Compressing objects: 100% (12/12), done. <br>
remote: Total 15 (delta 1), reused 12 (delta 0), pack-reused 0 (from 0) <br>
Receiving objects: 100% (15/15), 9.61 MiB | 8.44 MiB/s, done. <br>
Resolving deltas: 100% (1/1), done. <br>


```bash
> cd face_recog_dlib_file
```


```bash
face_recog_dlib_file> pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
```
Collecting dlib==19.22.99 <br>
  Downloading https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl (3.0 MB) 
     ---------------------------------------- 3.0/3.0 MB 13.5 MB/s eta 0:00:00 <br>
Installing collected packages: dlib <br>
Successfully installed dlib-19.22.99 <br>


```bash
face_recog_dlib_file> pip list
```
| Package        | Version   |
|----------------|-----------|
|  aiohttp       | 3.8.4     |
|  aiosignal     | 1.3.1     |
|  async-timeout | 4.0.2     |
|  dlib          | 19.22.99  |
|  frozenlist    | 1.3.3     |
|  multidict     | 6.0.4     |
|  openai        | 0.27.4    |
|  pip           | 23.0.1    |
|  setuptools    | 65.5.0    |
|  yarl          | 1.9.1     |


```bash
face_recog_dlib_file> pip install cmake
```
Collecting cmake <br>
  Using cached cmake-3.30.2-py3-none-win_amd64.whl (35.6 MB) <br>
Installing collected packages: cmake <br>
Successfully installed cmake-3.30.2 <br>


```bash
face_recog_dlib_file> pip install face-recognition
```
Collecting face-recognition
<br>   Using cached face_recognition-1.3.0-py2.py3-none-any.whl (15 kB)
<br> Collecting numpy
<br>   Downloading numpy-2.0.1-cp310-cp310-win_amd64.whl (16.6 MB)
    ---------------------------------------- 16.6/16.6 MB 54.7 MB/s eta 0:00:00
<br> Requirement already satisfied: dlib>=19.7 in c:\users\littl\appdata\local\programs\python\python310\lib\site-packages (from face-recognition) (19.22.99)
<br> Collecting Pillow
<br>   Downloading pillow-10.4.0-cp310-cp310-win_amd64.whl (2.6 MB)
    ---------------------------------------- 2.6/2.6 MB 79.5 MB/s eta 0:00:00
<br> Collecting face-recognition-models>=0.3.0
<br>   Using cached face_recognition_models-0.3.0.tar.gz (100.1 MB)
<br>   Preparing metadata (setup.py) ... done
<br> Collecting Click>=6.0
<br>   Using cached click-8.1.7-py3-none-any.whl (97 kB)
<br> Collecting colorama
<br>   Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
<br> Installing collected packages: face-recognition-models, Pillow, numpy, colorama, Click, face-recognition
<br>   DEPRECATION: face-recognition-models is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
<br>   Running setup.py install for face-recognition-models ... done
<br> Successfully installed Click-8.1.7 Pillow-10.4.0 colorama-0.4.6 face-recognition-1.3.0 face-recognition-models-0.3.0 numpy-2.0.1


```bash
face_recog_dlib_file> pip list
```
|Package                 | Version  |
|----------------------- | ---------|
|aiohttp                 | 3.8.4    |
|aiosignal               | 1.3.1    |
|async-timeout           | 4.0.2    |
|click                   | 8.1.7    |
|cmake                   | 3.30.2   |
|colorama                | 0.4.6    |
|dlib                    | 19.22.99 |
|face-recognition        | 1.3.0    |
|face-recognition-models | 0.3.0    |
|frozenlist              | 1.3.3    |
|multidict               | 6.0.4    |
|numpy                   | 2.0.1    |
|openai                  | 0.27.4   |
|pillow                  | 10.4.0   |
|pip                     | 23.0.1   |
|setuptools              | 65.5.0   |
|yarl                    | 1.9.1    |
