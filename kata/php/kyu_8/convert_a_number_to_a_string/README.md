# [Convert a Number to a String!](https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/php)
## Description
<div><p>We need a function that can transform a number into a string.</p>
<p>What ways of achieving this do you know?</p>
<h4 id="examples">Examples:</h4>
<pre><code>123 --&gt; "123"
999 --&gt; "999"
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">numberToString</span>(<span class="cm-variable-2">$num</span>){
  <span class="cm-keyword">return</span> <span class="cm-string">"</span><span class="cm-variable-2">$num</span><span class="cm-string">"</span>; <span class="cm-comment">// strval($num) or cast to string, i.e. (string) $num</span>
}</code></pre></details>