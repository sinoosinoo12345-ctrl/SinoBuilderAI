from doctor.checks import run_all_checks


def main():

    print("=" * 55)
    print("          SinoBuilderAI Doctor")
    print("=" * 55)
    print()

    passed = 0

    for item in run_all_checks():

        if item["ok"]:
            passed += 1

            print(f"✅ {item['name']}")
            print(f"   {item['version']}")

        else:

            print(f"❌ {item['name']}")
            print(f"   Reason : {item['reason']}")
            print(f"   Fix    : {item['fix']}")

        print()

    print("=" * 55)

    print(f"Health : {passed}/6")

    if passed == 6:
        print("STATUS : READY ✅")
    else:
        print("STATUS : WARNING ⚠")

    print("=" * 55)


if __name__ == "__main__":
    main()
