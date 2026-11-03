"""
스터디 출석부 (attend.py)
- 외부 라이브러리 없이 파이썬 표준 기능만 사용합니다.
- 기능: 1) 출석 추가(날짜·이름)  2) 출석 목록 보기  3) 종료
- 출석 기록은 attendance.csv 파일에 저장되어, 프로그램을 껐다 켜도 남습니다.
"""

import csv
import os
from datetime import datetime

# 출석 기록을 저장할 파일 이름
DATA_FILE = "attendance.csv"


def load_records():
    """저장된 출석 기록을 파일에서 읽어 리스트로 돌려줍니다."""
    records = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:  # [날짜, 이름] 형태만 받음
                    records.append(row)
    return records


def save_record(date, name):
    """출석 한 줄(날짜, 이름)을 파일 맨 뒤에 덧붙여 저장합니다."""
    with open(DATA_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, name])


def add_attendance():
    """사용자에게 날짜와 이름을 입력받아 출석을 추가합니다."""
    date = input("날짜를 입력하세요 (예: 2024-05-20, 비우면 오늘 날짜): ").strip()
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")  # 입력이 없으면 오늘 날짜

    name = input("이름을 입력하세요: ").strip()
    if name == "":
        print("이름이 비어 있어 출석을 추가하지 않았습니다.\n")
        return

    save_record(date, name)
    print(f"출석이 추가되었습니다: {date} - {name}\n")


def show_list():
    """저장된 출석 기록을 보기 좋게 출력합니다."""
    records = load_records()
    if not records:
        print("아직 출석 기록이 없습니다.\n")
        return

    print("\n===== 출석 목록 =====")
    print(f"{'번호':<4} {'날짜':<12} {'이름'}")
    print("-" * 28)
    for i, (date, name) in enumerate(records, start=1):
        print(f"{i:<4} {date:<12} {name}")
    print(f"총 {len(records)}건\n")


def main():
    """메뉴를 보여주고 사용자의 선택을 처리하는 반복 루프입니다."""
    while True:
        print("===== 스터디 출석부 =====")
        print("1. 출석 추가")
        print("2. 출석 목록 보기")
        print("3. 종료")
        choice = input("원하는 번호를 입력하세요: ").strip()

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("출석부를 종료합니다. 수고하셨습니다!")
            break
        else:
            print("1, 2, 3 중에서 입력해 주세요.\n")


if __name__ == "__main__":
    main()

