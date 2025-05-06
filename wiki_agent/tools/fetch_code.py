import logging
import os
from pathlib import Path

from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FetchFileTree(BaseModel):
    class Result(BaseModel):
        paths: list[str]

    result: Result


class FetchCode(BaseModel):
    class Result(BaseModel):
        path: str
        code: str | None
        note: str | None
        start: int | None
        end: int | None

    result: Result


def fetch_file_tree() -> FetchFileTree:
    """
    Fetches the file tree of the source directory and returns the result.

    Returns:
        dict: A dictionary containing the status and the fetched file tree.
    """
    source_dir = Path(os.getenv('SOURCE_DIR', os.getcwd()))
    exclude_ext = [".pyc"]

    def children(target: str) -> list[str]:
        child_paths = []
        for p in Path(target).iterdir():
            if p.is_dir():
                child_paths = child_paths + children(p)
            elif p.name.endswith(tuple(exclude_ext)):
                logger.debug(f"skipping {p}")
                continue
            else:
                child_paths.append(str(p).replace(str(source_dir) + "/", ''))
        return child_paths

    project_paths = children(source_dir)

    return FetchFileTree(
        result=FetchFileTree.Result(
            paths=project_paths
        )
    )


def fetch_source_code(file_or_dir_path: str, offset: int = 0, limit: int = 10_000) -> FetchCode:
    """
    Fetches the code from the specified file path and returns the result.

    Args:
        file_or_dir_path (str): The path to the file or directory to be fetched.
        offset (int): The offset to start reading the code from.
        limit (int): The maximum number of characters to read.
    Returns:
        dict: A dictionary containing the status and the fetched code.
    """
    source_dir = Path(os.getenv('SOURCE_DIR', os.getcwd()))
    target_path = Path(source_dir, file_or_dir_path)

    result = FetchCode.Result(path=file_or_dir_path, code=None, note=None, start=None, end=None)
    if target_path.exists():
        if not target_path.is_file():
            result.note = "not a file"
        else:
            try:
                file = open(target_path, "r", encoding="utf-8")
                target_code = file.read()[offset:offset + limit]
                result.code = target_code
                result.start = offset
                result.end = offset + len(target_code)
            except Exception as e:
                result.note = "load error"
    else:
        result.note = "not found"
    return FetchCode(result=result)


if __name__ == '__main__':
    path = "fetch_code.py"  # "tools/fetch_code.py"
    file_tree = fetch_file_tree()
    source_code = fetch_source_code(path)
    print(f"{file_tree=}")
    print(f"{source_code=}")
