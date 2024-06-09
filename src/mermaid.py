import streamlit.components.v1 as components

MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs"


def mermaid(code: str, height: int = 500) -> str:
    components.html(
        f"""
        <pre class="mermaid" style="height: {height}px;">
            {code}
        </pre>

        <script type="module">
            import mermaid from '{MERMAID_URL}';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=height,
    )
    return ""
