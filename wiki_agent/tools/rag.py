import itertools

import faiss
import numpy as np
import ollama

from wiki_agent.tools.fetch_code import fetch_file_tree, fetch_source_code


def _setup_index() -> (None, list[str]):
    def chunk_text(path: str, max_size: int = 1024, overlap: int = 128) -> list[str]:
        text = fetch_source_code(path).result.code
        if text is None:
            return []
        print(f"{path=} {len(text)=}")

        def get_chunk(i: int) -> str:
            start = max(i - overlap, 0)
            end = min(i + max_size + overlap, len(text))
            return f"File: {path}, Line: {start}-{end}\n----\n" + text[start:end]

        return [get_chunk(i) for i in range(0, len(text), max_size)]

    target_texts = list(itertools.chain.from_iterable([
        chunk_text(path)
        for path in fetch_file_tree().result.paths
    ]))
    target_embeds = [
        ollama.embeddings(model='nomic-embed-text', prompt=text).embedding
        for text in target_texts
    ]

    index: None = faiss.IndexFlatL2(768)
    index.add(x=np.array(target_embeds).astype('float32'))
    return index, target_texts


(index, target_texts) = _setup_index()


def search_source_code(keyword: str) -> list[str]:
    in_embeds = [
        ollama.embeddings(model='nomic-embed-text', prompt=keyword).embedding
    ]
    D, I = index.search(x=np.array(in_embeds).astype('float32'), k=3)
    return [target_texts[i] for i in I[0]]


if __name__ == '__main__':
    keyword = "RAGに関して"
    print(search_source_code(keyword))
