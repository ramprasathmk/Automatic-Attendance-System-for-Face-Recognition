```bash
> git clone "https://github.com/RvTechiNNovate/face_recog_dlib_file.git"
```

```
Cloning into 'face_recog_dlib_file'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 15 (delta 1), reused 12 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (15/15), 9.61 MiB | 8.44 MiB/s, done.
Resolving deltas: 100% (1/1), done.
```


```bash
> cd face_recog_dlib_file
```


```bash
face_recog_dlib_file> pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
```

```
Collecting dlib==19.22.99
  Downloading https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl (3.0 MB) 
     ---------------------------------------- 3.0/3.0 MB 13.5 MB/s eta 0:00:00
Installing collected packages: dlib
Successfully installed dlib-19.22.99
```


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

```
Collecting cmake
  Using cached cmake-3.30.2-py3-none-win_amd64.whl (35.6 MB)
Installing collected packages: cmake
Successfully installed cmake-3.30.2
```


```bash
face_recog_dlib_file> pip install face-recognition
```

```
Collecting face-recognition
   Using cached face_recognition-1.3.0-py2.py3-none-any.whl (15 kB)
 Collecting numpy
   Downloading numpy-2.0.1-cp310-cp310-win_amd64.whl (16.6 MB)
    ---------------------------------------- 16.6/16.6 MB 54.7 MB/s eta 0:00:00
 Requirement already satisfied: dlib>=19.7 in c:\users\littl\appdata\local\programs\python\python310\lib\site-packages (from face-recognition) (19.22.99)
 Collecting Pillow
   Downloading pillow-10.4.0-cp310-cp310-win_amd64.whl (2.6 MB)
    ---------------------------------------- 2.6/2.6 MB 79.5 MB/s eta 0:00:00
 Collecting face-recognition-models>=0.3.0
   Using cached face_recognition_models-0.3.0.tar.gz (100.1 MB)
   Preparing metadata (setup.py) ... done
 Collecting Click>=6.0
   Using cached click-8.1.7-py3-none-any.whl (97 kB)
 Collecting colorama
   Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
 Installing collected packages: face-recognition-models, Pillow, numpy, colorama, Click, face-recognition
   DEPRECATION: face-recognition-models is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
   Running setup.py install for face-recognition-models ... done
 Successfully installed Click-8.1.7 Pillow-10.4.0 colorama-0.4.6 face-recognition-1.3.0 face-recognition-models-0.3.0 numpy-2.0.1
```


```bash
face_recog_dlib_file> pip list
```
| Package                 | Version  |
|-------------------------|----------|
| aiohttp                 | 3.8.4    |
| aiosignal               | 1.3.1    |
| async-timeout           | 4.0.2    |
| click                   | 8.1.7    |
| cmake                   | 3.30.2   |
| colorama                | 0.4.6    |
| dlib                    | 19.22.99 |
| face-recognition        | 1.3.0    |
| face-recognition-models | 0.3.0    |
| frozenlist              | 1.3.3    |
| multidict               | 6.0.4    |
| numpy                   | 2.0.1    |
| openai                  | 0.27.4   |
| pillow                  | 10.4.0   |
| pip                     | 23.0.1   |
| setuptools              | 65.5.0   |
| yarl                    | 1.9.1    |
