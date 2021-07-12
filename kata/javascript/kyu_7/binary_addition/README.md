# [Binary Addition](https://www.codewars.com/kata/551f37452ff852b7bd000139/train/javascript)
## Description
<div><p>Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.</p>
<p>The binary number returned should be a string.</p>
<p>Examples:</p>
<pre><code>add_binary(1, 1) == "10" (1 + 1 = 2 in decimal or 10 in binary)
add_binary(5, 9) == "1110" (5 + 9 = 14 in decimal or 1110 in binary)
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">addBinary</span>(<span class="cm-def">a</span>,<span class="cm-def">b</span>) {
  <span class="cm-keyword">return</span> (<span class="cm-variable-2">a</span><span class="cm-operator">+</span><span class="cm-variable-2">b</span>).<span class="cm-property">toString</span>(<span class="cm-number">2</span>);
}</code></pre></details>