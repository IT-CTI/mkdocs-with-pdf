import re

html = """
    <pre class="mermaid"><code>graph LR
    A[Start] --&gt; B{Error?};
    B --&gt;|Yes| C[Hmm...];
    C --&gt; D[Debug];
    D --&gt; B;
    B ----&gt;|No| E[Yay!];</code></pre>
"""
mermaid_regex = r'<pre class="mermaid"><code>(.*?)</code></pre>'
mermaid_matches = re.findall(mermaid_regex, html, flags=re.DOTALL)
print(mermaid_matches)
