from app.application import SinoBuilderApplication


def main():

    app = SinoBuilderApplication()

    status = app.status()

    print("🐉 Sino Builder AI")

    print(
        "Version:",
        status["version"]
    )

    print(
        "Status:",
        status["status"]
    )

    print("\nEngines:")

    for engine in status["engines"]:

        print(
            "✅",
            engine
        )


if __name__ == "__main__":

    main()
