# [Count the Digit](https://www.codewars.com/kata/566fc12495810954b1000030/train/java)
## Description
<div><p>Take an integer <code>n (n &gt;= 0)</code> and a digit <code>d (0 &lt;= d &lt;= 9)</code> as an integer. </p>
<p>Square all numbers <code>k (0 &lt;= k &lt;= n)</code> between 0 and n. </p>
<p>Count the numbers of digits <code>d</code> used in the writing of all the <code>k**2</code>. </p>
<p>Call <code>nb_dig</code> (or nbDig or ...) the function taking <code>n</code> and <code>d</code> as parameters and returning this count.</p>
<h4 id="examples">Examples:</h4>

<pre><code>n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

nb_dig(25, 1) returns 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
</code></pre>
<p>Note that <code>121</code> has twice the digit 1.</p>
</div><details><summary>Solution</summary><pre><code><span class="cm-keyword">public</span> <span class="cm-keyword">class</span> <span class="cm-def">CountDig</span> {
    <span class="cm-keyword">public</span> <span class="cm-keyword">static</span> <span class="cm-type">int</span> <span class="cm-variable">nbDig</span>(<span class="cm-type">int</span> <span class="cm-variable">n</span>, <span class="cm-type">int</span> <span class="cm-variable">d</span>) {
        <span class="cm-type">int</span> <span class="cm-variable">count</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>;
        <span class="cm-keyword">for</span> (<span class="cm-type">int</span> <span class="cm-variable">i</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>; <span class="cm-variable">i</span> <span class="cm-operator">&lt;=</span> <span class="cm-variable">n</span>; <span class="cm-variable">i</span><span class="cm-operator">++</span>)
          <span class="cm-variable">count</span> <span class="cm-operator">+=</span> <span class="cm-type">Integer</span>.<span class="cm-variable">toString</span>(<span class="cm-variable">i</span><span class="cm-operator">*</span><span class="cm-variable">i</span>).<span class="cm-variable">chars</span>().<span class="cm-variable">filter</span>(<span class="cm-variable">ch</span> <span class="cm-operator">-&gt;</span> <span class="cm-variable">ch</span> <span class="cm-operator">==</span> <span class="cm-type">Character</span>.<span class="cm-variable">forDigit</span>(<span class="cm-variable">d</span>, <span class="cm-number">10</span>)).<span class="cm-variable">count</span>();
        <span class="cm-keyword">return</span> <span class="cm-variable">count</span>;
    }
}</code></pre></details>