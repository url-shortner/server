# Url shortner server github repository입니다.

## local 환경에서 db를 수정하고 테스트해야할 때

    - manage.py의 main함수 밑에
    ```
        os.environ.setdefault('CROSS_ENV','development')os.environ.setdefault('CROSS_ENV','development')
    ```
    
    위와 같이 작성하여야 수정사항이 반영됩니다.
