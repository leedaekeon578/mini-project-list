import sys

ARRIVALS = {
    "강남역": ((2, "혼잡"), (7, "여유")),
    "사당역": ((4, "보통"), (9, "보통")),
    "서울역": ((1, "여유"), (6, "혼잡")),
}

CROWD_LEVEL = {"여유": 0, "보통": 1, "혼잡": 2}


def recommend(first, second):
    extra_wait = second[0] - first[0]
    calmer = CROWD_LEVEL[second[1]] < CROWD_LEVEL[first[1]]
    if calmer and extra_wait <= 5:
        return "한 대 보내세요"
    return "바로 타세요"


def main():
    if len(sys.argv) < 2:
        print("사용법: uv run app.py <역 이름> | --all")
        sys.exit(1)

    station = sys.argv[1]
    if station == "--all":
        for name, (first, second) in ARRIVALS.items():
            print(f"{name}: {first}분 후, {second}분 후")
        return

    if station not in ARRIVALS:
        print(f"등록되지 않은 역입니다: {station}")
        print("지원 역: " + ", ".join(ARRIVALS))
        sys.exit(1)

    first, second = ARRIVALS[station]
    print(f"{station}: {first[0]}분 후, {second[0]}분 후")
    print(f"추천: {recommend(first, second)}")


if __name__ == "__main__":
    main()
