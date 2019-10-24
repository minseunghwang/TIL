- # Python Dictionary

  ## 1. 기본기

  - 가장 많이 사용되는 자료형 + 웹 개발 하면서 마주칠 가능성이 가장 높음

  - 딕셔너리는 기본적으로

     

    ```
    Key
    ```

    와

     

    ```
    Value
    ```

     

    구조!

    - Key : `string`, `integer`, `float`, `boolean` 가능! 하지만 `list`, `dictionary`는 안된다.
    - Value: 모든 자료형 가능. `list`와 `dictionary`도 가능하다.

  ### 1.1 딕셔너리 만들기

  ```
  # 1
  lunch = {
      '중국집': '032'
  }
  
  # 2
  lunch = dict(중국집='032')
  ```

  ### 1.2 딕셔너리 내용 추가하기

  ```
  lunch['분식집'] = '02'
  ```

  ### 1.3 딕셔너리 내용 가져오기 (2가지)

  ```
  artists = {
      '아티스트': {
          '민수': '민수는 혼란스럽다',
          '아이유': '좋은날'
      }
  }
  # 민수의 대표곡은?
  print(artists["아티스트"]["민수"])
  print(artists.get("아티스트").get("민수"))
  ```

  ### 1.4 딕셔너리 반복문 활용하기

  ```
  # 1.4.1 기본 활용
  for key in lunch:
      print(key)          # key 출력됨
      print(lunch[key])   # key로 value 추출 
  
  # 1.4.2 .items : Key, Value 모두 가져오기
  for key, value in lunch.items():
      print(key, value)
  
  # 1.4.3 .values : Value만 가져오기
  for value in lunch.values():
      print(value)
      #=> 031, 032
  
  # 1.4.4 .keys : Key만 가져오기
  for key in lunch.keys():
      print(key)
      #=> 중국집, 분식집
  ```

  ### 1.5 연습문제

  - [문제 소스코드](https://bit.do/yeoksam_python_33)
  - [해설 소스코드](https://bit.do/yeoksam_answer)

  ## 2. 실습 문제

  > 이정도 하면 딕셔너리에서 데이터 뽑아오기 문제 없음. ~~딕셔너리 마스터 ㅎ................~~

  - 문제 소스코드
    - 딕셔너리 내용 가져오기
    - 딕셔너리 반복문 활용하기
    - list in 활용
  - [해설 소스코드](https://bit.do/yeoksam_answer)