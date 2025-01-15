import json

# 파일 경로 설정
train_file = 'data/hotpot-all/train.json'
dev_file = 'data/hotpot-all/dev.json'


def print_first_n_entries(file_path, n):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(f"\nFirst {n} entries of {file_path}:")

        if isinstance(data, list):  # 리스트 형식일 경우
            for entry in data[:n]:
                print(json.dumps(entry, indent=4))
        elif isinstance(data, dict):  # 딕셔너리 형식일 경우
            keys = list(data.keys())[:n]
            for key in keys:
                print(f"Key: {key}")
                print(json.dumps(data[key], indent=4))
        else:
            print("Unsupported data format.")


# train.json의 처음 몇 줄 출력
print_first_n_entries(train_file, 5)

# dev.json의 처음 몇 줄 출력
print_first_n_entries(dev_file, 5)
