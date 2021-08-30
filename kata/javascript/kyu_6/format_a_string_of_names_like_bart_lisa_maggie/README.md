# [Format a string of names like 'Bart, Lisa & Maggie'.](https://www.codewars.com/kata/53368a47e38700bd8300030d/train/javascript)
## Description
<div><p>Given: an array containing hashes of names</p>
<p>Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.</p>
<p>Example:</p>


<pre><code class="language-javascript"><span class="cm-variable">list</span>([ {<span class="cm-property">name</span>: <span class="cm-string">'Bart'</span>}, {<span class="cm-property">name</span>: <span class="cm-string">'Lisa'</span>}, {<span class="cm-property">name</span>: <span class="cm-string">'Maggie'</span>} ])
<span class="cm-comment">// returns 'Bart, Lisa &amp; Maggie'</span>

<span class="cm-variable">list</span>([ {<span class="cm-property">name</span>: <span class="cm-string">'Bart'</span>}, {<span class="cm-property">name</span>: <span class="cm-string">'Lisa'</span>} ])
<span class="cm-comment">// returns 'Bart &amp; Lisa'</span>

<span class="cm-variable">list</span>([ {<span class="cm-property">name</span>: <span class="cm-string">'Bart'</span>} ])
<span class="cm-comment">// returns 'Bart'</span>

<span class="cm-variable">list</span>([])
<span class="cm-comment">// returns ''</span>
</code></pre>

<p>Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">list</span>(<span class="cm-def">names</span>){
  <span class="cm-keyword">return</span> <span class="cm-variable-2">names</span>.<span class="cm-property">map</span>(<span class="cm-def">p</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">p</span>.<span class="cm-property">name</span>).<span class="cm-property">join</span>(<span class="cm-string">', '</span>).<span class="cm-property">replace</span>(<span class="cm-string-2">/,(?=[^,]*$)/</span>, <span class="cm-string">' &amp;'</span>); <span class="cm-comment">// (?= ...) === look-ahead</span>
}</code></pre></details>