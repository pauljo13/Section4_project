# Section4_project
- 프로젝트 기간 : 2023-06-14 ~ 2023-06-19
### 세션 프로젝트의 기본 요구사항
1. 데이터베이스 구축
2. 머신러닝을 포함한 API 서비스 개발 1개
3. 대시보드 내에 데이터 분석 그래프 3개

### 프로젝트 전 프로세스
1. 데이터 가져오기 Pull
    - 케글에서 당뇨환자&의료보험 데이터셋을 웹 스크래이핑한다.
2. 데이터 저장 Store
    - 당뇨환자&의료보험 데이터셋을 데이터베이스에 저장한다.
    - csv -> DB ???
3. API 서비스 개발
    - 머신러닝 모델 제작
        - 당뇨환자의 나이, 성별, BMI, 흡연을 통해 예측모델을 생성
        - 의료보험에 당뇨 가능을 추가 -> 의료보험료를 예측하는 모델을 생성
    - 머신러닝 모델을 API에 담아 서비스를 제작
        - 나이, 성별, 몸무게, 키, 흡연 사실을 받는다.
        - 몸무게와 키를 BMI로 전환
        - 받은 데이터로 당뇨 가능성을 예측
        - 나이, 성별, BMI, 흡연, 당뇨 가능성으로 미국의 의료보험료를 예측하여 반환
4. 데이터 분석용 대시보드 개발

## 파일 목록
- test.ipynb : 프로그램 제작 전 미리 실행하는 파일
- app.py :  실전 데이터 제작 프로그램
- __init__.py : 실전 과제 API 제작 파일
- CSV : CSV 파일 보관
    - diabetes-prediction-dataset.csv : 당뇨환자 데이터셋
    - medical-insurance-payout.csv : 의료보험 데이터셋
- Reference : 참고 자료 보관
    - qa.ipynb : 라이브 강의에서 나온 참고 코드

## Day 1
- 도메인 : 의료, 헬스케어
- 내용 :
    의료와 헬스케어에 관련된 데이터를 찾는데 노력함
- 문제점 :
    의료, 헬스케어 관련된 데이터들은 보안, 윤리의 문제로 인해서 접근하기가 어렵다.
    특히, 국내 데이터는 더더욱 접근하기 힘든 점이 많다.
    데이터를 찾더라도 머신러닝에 사용하기에 데이터의 컬럼이 데이터 량이 부족한 한계점을 갖는다.
- 해결 방법 :
    외국 사이트를 찾는 쪽으로 선회
    외국에서는 데이터를 구하기 쉽다. 하지만 데이터 컬럼의 질이 떨어지는 것은 동일하다.
- 2023-06-14 

## Day 2
- 도메인 : 의료, 헬스케어
- 주제 선정 : 
    당뇨병 환자 데이터를 이용하여 나이, 성별, bmi, 흡연을 이용하여 당뇨 예측한 값을 구하는 모델을 만듬
    이를 이용하여 의료 보험료 데이터에 입력하여 추가적인 당뇨 확률을 구하고 이를 통한 의료 보험료를 예측하는 모델
- 데이터 셋 사이트 :
    당뇨환자 데이터셋 : https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?resource=download
    의료보험 데이터셋 : https://www.kaggle.com/datasets/harshsingh2209/medical-insurance-payout
- 오늘 :
    - EDA
- 내용 :
    두 가지 데이터셋을 이용하여 머신러닝 모델을 제작 2가지 머신러닝 모델을 제작
    - 당뇨환자 데이터셋
        - 구조 : (100000, 9)
        - 컬럼 : 'gender', 'age', 'hypertension', 'heart_disease', 'smoking_history','bmi', 'HbA1c_level', 'blood_glucose_level', 'diabetes'
        - 결측치 : 0
        - 중복값 : 3854 -> 환자 ID가 없어서 생긴 문제로 보임, 하지만 확실할 수 없어 제거
        - Taget : diabetes -> 분류문제
    - 당뇨환자 EDA
        - gender : Other 성별 제거 후 1과 0으로 인코딩
        - smoking_history : 1과 0으로 인코딩

    - 의료보험 데이터셋
        - 구조 : (1338, 7)
        - 컬럼 : 'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'
        - 결측치 : 0
        - 중복값 : 1
        - Taget : charges -> 회귀문제
    - 의료환자 EDA
        - sex : 1과 0으로 인코딩
        - smoker : 1과 0으로 인코딩
        - region : 0 ~ 3으로 인코딩 , 지역적인 데이터로 빈부 차이나 지역-문화적인 차이를 볼 수도 있을 것으로 보이나 중요한지는 모르겠음, 상황에 따라 삭제

    - 기타 사항
        - 주요 컬럼 : 'age', 'sex'&'gender', 'bmi',('smoking_history' vs 'smoker')
        - 주요 동일 데이터형태 컬럼 : 'age', 'sex', 'bmi',
            - age : 나이
            - sex : 성별
            - bmi : 신체질량지수 = 체중(kg)/[신장(m)]^2 : 20미만(저체중),20-24(정상),25-29(과체중),30이상(비만)
        - 주요 비동일 데이터형태 컬럼 : 'smoking_history' vs 'smoker'
            - smoking_history
                - value : 'never','No Info','former','current','not current','ever'
            - smoker
                - value : no , yes

- 문제점 :
    당뇨환자 데이터셋과 의료보험 데이터셋의 흡연에 대한 컬럼 'smoking_history' vs 'smoker'의 value 값이 서로 차이가 존재한다.
    - smoking_history -> 여러가지 가능을 만들어서 비교해야 할 것으로 보임
            - 'never' 전혀 -> NO
            - 'No Info' 정보없음 -> ?
            - 'former' 이전 -> No
            - 'current' 현재 -> Yes
            - 'not current' 현재는 아님 -> No
            - 'ever' 항상 -> Yes
    - smoker :
            - no 비흡연자
            - yes 흡연자
- 해결 방법 :
    - 두 데이터를 동일한 형태로 만들어야 머신러닝 시 모델의 일관성을 갖을 수 있을 것으로 보인다.
    - smoking_history을 여러가지 가능성
        1. 100% 비흡연자 vs 한 번이라도 흡연을 했다.
        2. 현재를 기준으로 비흡연자 vs 흡연자
- 2023-06-15 

## Day 3
- 도메인 : 의료, 헬스케어
- 주제 선정 : 
    당뇨병 환자 데이터를 이용하여 나이, 성별, bmi, 흡연을 이용하여 당뇨 예측한 값을 구하는 모델을 만듬
    이를 이용하여 의료 보험료 데이터에 입력하여 추가적인 당뇨 확률을 구하고 이를 통한 의료 보험료를 예측하는 모델
- 데이터 셋 사이트 :
    당뇨환자 데이터셋 : https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?resource=download
    의료보험 데이터셋 : https://www.kaggle.com/datasets/harshsingh2209/medical-insurance-payout
- 오늘 :

- 내용 :

- 문제점 :

- 해결 방법 :
- 2023-06-16 

## Day 4
- 도메인 : 의료, 헬스케어
- 주제 선정 : 
    당뇨병 환자 데이터를 이용하여 나이, 성별, bmi, 흡연을 이용하여 당뇨 예측한 값을 구하는 모델을 만듬
    이를 이용하여 의료 보험료 데이터에 입력하여 추가적인 당뇨 확률을 구하고 이를 통한 의료 보험료를 예측하는 모델
- 데이터 셋 사이트 :
    당뇨환자 데이터셋 : https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?resource=download
    의료보험 데이터셋 : https://www.kaggle.com/datasets/harshsingh2209/medical-insurance-payout
- 오늘 :

- 내용 :

- 문제점 :

- 해결 방법 :
- 2023-06-1x 
## Day 5
- 도메인 : 의료, 헬스케어
- 주제 선정 : 
    당뇨병 환자 데이터를 이용하여 나이, 성별, bmi, 흡연을 이용하여 당뇨 예측한 값을 구하는 모델을 만듬
    이를 이용하여 의료 보험료 데이터에 입력하여 추가적인 당뇨 확률을 구하고 이를 통한 의료 보험료를 예측하는 모델
- 데이터 셋 사이트 :
    당뇨환자 데이터셋 : https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?resource=download
    의료보험 데이터셋 : https://www.kaggle.com/datasets/harshsingh2209/medical-insurance-payout
- 오늘 :

- 내용 :

- 문제점 :

- 해결 방법 :
- 2023-06-1x 