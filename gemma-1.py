import asyncio
import ollama


async def main() -> None:
    client = ollama.AsyncClient()

    messages = []

    while True:

        if request_content := input(">>> "):
            if request_content == "exit":
                break

            messages.append({"role": "user", "content": request_content})

        response_content = ""
        async for response in await client.chat(
            model="gemma:7b", messages=messages, stream=True
        ):
            if response["done"]:
                messages.append({"role": "assistant", "content": response_content})
                print("")
                print(response_content)
                print("")

            if message := response.get("message", {}):
                if content := message.get("content", ""):
                    response_content += content
                    print(".", end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
