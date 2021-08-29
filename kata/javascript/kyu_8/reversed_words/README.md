# [Reversed Words](https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/javascript)
## Description
<div><p>Complete the solution so that it reverses all of the words within the string passed in. </p>
<p>Example:</p>
<pre><code>"The greatest victory is that which requires no battle" --&gt; "battle no requires which that is victory greatest The"
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">reverseWords</span>(<span class="cm-def">str</span>){
  <span class="cm-keyword">return</span> <span class="cm-variable-2">str</span>.<span class="cm-property">split</span>(<span class="cm-string">' '</span>).<span class="cm-property">reverse</span>().<span class="cm-property">join</span>(<span class="cm-string">' '</span>);
}</code></pre></details>