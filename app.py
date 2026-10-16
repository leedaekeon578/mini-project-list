import sys

ARRIVALS = {
    "강남역": (2, 7),
    "사당역": (4, 9),
    "서울역": (1, 6),
}


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
    print(f"{station}: {first}분 후, {second}분 후")


if __name__ == "__main__":
    main()
