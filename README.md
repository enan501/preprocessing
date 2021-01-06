# preprocessing
preprocessing tool for video learning  

***  
## How to Install
```
pip install -r requirments.txt
```

## How to Use
### 1. edit videocutter.py
  * 4번째 줄 path 변수에 데이터셋이 위치한 폴더 경로 입력
    > path = "/Users/enan/Projects/2020-02/grad-project/data"
### 2. write trim_list.txt
  * 데이터셋이 위치한 폴더에 trim_list.txt 작성  
    > folder:[folder명]  
    > type:[webcam or phone]  
    > file:[file명]  
    > mm:ss:ms-mm:ss:ms [category]  # mm:ss:ms = 분:초:밀리초  
    > mm:ss:ms-mm:ss:ms [category]  
    > file:[file명]  
    > mm:ss:ms-mm:ss:ms [category]  
    > mm:ss:ms-mm:ss:ms [category]  
    > . . .   
### 3. run videocutter.py
   ```python videocutter.py```
### 4. check result
   ```[1에서 입력한 path]/cheating/[category]/[webcam or phone]/[index]_[file명] 파일로 저장됨```
 
