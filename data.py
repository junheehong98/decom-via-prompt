import os
import requests

# 데이터 디렉토리 경로 설정 (원하는 디렉토리 경로로 변경 가능)
DATA_DIR = 'hotpot_data'

# 다운로드할 파일들의 URL
urls = {
    'hotpot_train_v1.json': 'http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_train_v1.1.json',
    'hotpot_dev_distractor_v1.json': 'http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_distractor_v1.json'
}

# 디렉토리가 존재하지 않으면 생성
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 파일 다운로드 및 저장
for filename, url in urls.items():
    response = requests.get(url)
    
    # 파일을 {DATA_DIR}에 저장
    file_path = os.path.join(DATA_DIR, filename)
    
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    print(f"{filename}이(가) {DATA_DIR}에 성공적으로 저장되었습니다.")
