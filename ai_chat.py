import json
import urllib.request
import urllib.error


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def ask_ai(question):

    if not question:
        return "Please ask me something."

    data = {
        "model": MODEL_NAME,
        "prompt": f"Answer briefly and directly in 2-3 sentences:\n\n{question}",
        "stream": False,
        "keep_alive": "10m",
     "options": {
    "num_predict": 300
}
    }

    try:

        request = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with urllib.request.urlopen(
            request,
            timeout=180
        ) as response:

            result = json.loads(
                response.read().decode("utf-8")
            )

        answer = result.get(
            "response",
            ""
        ).strip()

        if not answer:
            return "AI returned an empty response."

        return answer

    except urllib.error.URLError as e:
        return f"Could not connect to Ollama: {e}"

    except TimeoutError:
        return "AI took too long to respond."

    except Exception as e:
        return f"AI error: {e}"
