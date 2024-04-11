from typing import List
from pathlib import Path
import ollama


def main() -> None:

    prompt = "What do these pictures have in common?"
    images: List[Path] = [
        Path("./data/IMG_8549.png"),
        Path("./data/IMG_7440.png"),
        Path("./data/IMG_8712.png"),
    ]

    output: str = ""

    for response in ollama.generate(
        model="llava", prompt=prompt, images=images, stream=True
    ):
        print(".", end="", flush=True)
        if message := response.get("response", ""):
            output += message
    print("")

    print(output)


if __name__ == "__main__":
    main()
