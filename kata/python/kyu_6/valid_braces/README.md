# [Valid Braces](https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python)
## Description
<div><p>Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return <code>true</code> if the string is valid, and <code>false</code> if it's invalid.</p>
<p>This Kata is similar to the <a href="https://www.codewars.com/kata/valid-parentheses" target="_blank">Valid Parentheses</a> Kata, but introduces new characters: brackets <code>[]</code>, and curly braces <code>{}</code>. Thanks to <code>@arnedag</code> for the idea!</p>
<p>All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: <code>()[]{}</code>. </p>
<h3 id="what-is-considered-valid">What is considered Valid?</h3>
<p>A string of braces is considered valid if all braces are matched with the correct brace.</p>
<h2 id="examples">Examples</h2>
<pre><code>"(){}[]"   =&gt;  True
"([{}])"   =&gt;  True
"(}"       =&gt;  False
"[(])"     =&gt;  False
"[({})](]" =&gt;  False
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">def</span> <span class="cm-def">validBraces</span>(<span class="cm-variable">string</span>):
    <span class="cm-variable">braces</span> <span class="cm-operator">=</span> [<span class="cm-string">"{}"</span>, <span class="cm-string">"[]"</span>, <span class="cm-string">"()"</span>]
    <span class="cm-keyword">for</span> <span class="cm-variable">_</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-builtin">int</span>(<span class="cm-builtin">len</span>(<span class="cm-variable">string</span>) <span class="cm-operator">/</span> <span class="cm-number">2</span>)):
        <span class="cm-keyword">for</span> <span class="cm-variable">brace</span> <span class="cm-keyword">in</span> <span class="cm-variable">braces</span>:
            <span class="cm-variable">string</span> <span class="cm-operator">=</span> <span class="cm-variable">string</span>.<span class="cm-property">replace</span>(<span class="cm-variable">brace</span>, <span class="cm-string">''</span>)
        <span class="cm-keyword">if</span> <span class="cm-keyword">not</span> <span class="cm-variable">string</span>:
            <span class="cm-keyword">return</span> <span class="cm-keyword">True</span>
    <span class="cm-keyword">return</span> <span class="cm-keyword">False</span></code></pre></details>