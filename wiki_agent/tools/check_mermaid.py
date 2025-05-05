import subprocess

from pydantic import BaseModel


class Result(BaseModel):
    status: str
    stderr: str | None = None


def check_mermaid_format(code: str) -> str:
    """
    Checks if the given text contains valid mermaid syntax.

    Args:
        code (str): The text to check.

    Returns:
        Result: A Result object containing the status of the check.
    """
    print("Checking mermaid format...")
    process_result = subprocess.run(
        f"echo '{code}' | npx @mermaid-js/mermaid-cli -e svg -i - -o -",
        shell=True,
        capture_output=True,
        text=True
    )
    return Result(
        status="Valid mermaid syntax" if process_result.returncode == 0 else "Invalid mermaid syntax",
        stderr=process_result.stderr
    )


if __name__ == '__main__':
    mermaid_code = """
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
    """
    result = check_mermaid_format(mermaid_code)
    print(result)
