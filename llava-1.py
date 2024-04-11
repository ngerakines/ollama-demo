from typing import List
from pathlib import Path
import ollama


def main() -> None:

    prompt = "What is the subject of this picture?"
    images: List[Path] = [Path("./data/IMG_8215.png")]

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
