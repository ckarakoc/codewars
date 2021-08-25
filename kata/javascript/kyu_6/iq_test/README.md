# [IQ Test](https://www.codewars.com/kata/552c028c030765286c00007d/train/javascript)
## Description
<div><p>Bob is preparing to pass IQ test. The most frequent task in this test is <code>to find out which one of the given numbers differs from the others</code>. Bob observed that one number usually differs from the others in <strong>evenness</strong>. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.</p>
<p><code>!</code> Keep in mind that your task is to help Bob solve a <code>real IQ test</code>, which means indexes of the elements start from <code>1 (not 0)</code></p>
<h2 id="examples">Examples:</h2>

<pre><code class="language-javascript"><span class="cm-variable">iqTest</span>(<span class="cm-string">"2 4 7 8 10"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-number">3</span> <span class="cm-comment">// Third number is odd, while the rest of the numbers are even</span>

<span class="cm-variable">iqTest</span>(<span class="cm-string">"1 2 1 1"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-number">2</span> <span class="cm-comment">// Second number is even, while the rest of the numbers are odd</span>
</code></pre>




</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">iqTest</span>(<span class="cm-def">numbers</span>){
  <span class="cm-variable">let arr</span> <span class="cm-operator">=</span> <span class="cm-variable-2">numbers</span>.<span class="cm-property">split</span>(<span class="cm-string">' '</span>).<span class="cm-property">map</span>(<span class="cm-def">n</span> <span class="cm-operator">=&gt;</span> <span class="cm-operator">+</span><span class="cm-variable-2">n</span>);
  <span class="cm-keyword">if</span> (<span class="cm-variable">arr</span>.<span class="cm-property">length</span> <span class="cm-operator">&lt;</span> <span class="cm-number">3</span>) <span class="cm-keyword">return</span> <span class="cm-number">1</span>;
  <span class="cm-keyword">for</span> (<span class="cm-keyword">let</span> <span class="cm-def">i</span> <span class="cm-operator">=</span> <span class="cm-number">1</span>; <span class="cm-variable-2">i</span> <span class="cm-operator">&lt;</span> <span class="cm-variable">arr</span>.<span class="cm-property">length</span>; <span class="cm-variable-2">i</span><span class="cm-operator">++</span>){
    <span class="cm-keyword">let</span> <span class="cm-def">sum</span> <span class="cm-operator">=</span> <span class="cm-variable">arr</span>[<span class="cm-variable-2">i</span><span class="cm-operator">-</span><span class="cm-number">1</span>] <span class="cm-operator">+</span> <span class="cm-variable">arr</span>[<span class="cm-variable-2">i</span>];
    <span class="cm-keyword">if</span> (<span class="cm-variable-2">sum</span> <span class="cm-operator">%</span> <span class="cm-number">2</span> <span class="cm-operator">===</span> <span class="cm-number">0</span>) <span class="cm-keyword">continue</span>;
    <span class="cm-keyword">let</span> <span class="cm-def">diff</span> <span class="cm-operator">=</span> <span class="cm-variable">arr</span>.<span class="cm-property">slice</span>(<span class="cm-variable-2">i</span><span class="cm-operator">-</span><span class="cm-number">2</span>)[<span class="cm-number">0</span>];
    <span class="cm-keyword">if</span> ((<span class="cm-variable">arr</span>[<span class="cm-variable-2">i</span><span class="cm-operator">-</span><span class="cm-number">1</span>] <span class="cm-operator">+</span> <span class="cm-variable-2">diff</span>) <span class="cm-operator">%</span> <span class="cm-number">2</span> <span class="cm-operator">===</span> <span class="cm-number">1</span>) <span class="cm-keyword">return</span> <span class="cm-variable-2">i</span>;
    <span class="cm-keyword">if</span> ((<span class="cm-variable">arr</span>[<span class="cm-variable-2">i</span>] <span class="cm-operator">+</span> <span class="cm-variable-2">diff</span>) <span class="cm-operator">%</span> <span class="cm-number">2</span> <span class="cm-operator">===</span> <span class="cm-number">1</span>) <span class="cm-keyword">return</span> <span class="cm-variable-2">i</span><span class="cm-operator">+</span><span class="cm-number">1</span>;
  }
  <span class="cm-keyword">return</span> <span class="cm-atom">null</span>;
}</code></pre></details>