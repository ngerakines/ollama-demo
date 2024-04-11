from typing import List, Optional, Sequence, AnyStr
import ollama


def produce(
    model: str = "",
    prompt: str = "",
    images: Optional[Sequence[AnyStr]] = None,
    options: Optional[ollama.Options] = None,
) -> str:
    output: str = ""
    for response in ollama.generate(
        stream=True,
        model=model,
        prompt=prompt,
        images=images,
        options=options,
    ):
        print(response)
        # print(".", end="", flush=True)
        output += response.get("response", "")
    print("")

    print(output)


def main() -> None:
    produce(
        model="codellama:7b-code",
        prompt="You are an expert programmer that writes simple, concise code and explanations. Write a python function to generate the 5th fibonacci number.",
    )
    input("Press Enter to continue...")

    prefix = '''def remove_non_ascii(s: str) -> str:
    """ '''

    suffix = """
        return result
    """

    produce(
        model="codellama:7b-code",
        prompt=f"<PRE> {prefix} <SUF>{suffix} <MID>",
        options={
            "num_predict": 128,
            "temperature": 0,
            "top_p": 0.9,
            "stop": ["<EOT>"],
        },
    )


if __name__ == "__main__":
    main()
