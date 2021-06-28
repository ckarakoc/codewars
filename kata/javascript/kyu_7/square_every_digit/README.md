# [Square Every Digit](https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript)
## Description
<div><p>Welcome. In this kata, you are asked to square every digit of a number and concatenate them.</p>
<p>For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.</p>
<p><strong>Note:</strong> The function accepts an integer and returns an integer</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">squareDigits</span>(<span class="cm-def">num</span>){
  <span class="cm-variable">res</span> <span class="cm-operator">=</span> <span class="cm-string">''</span>;
  <span class="cm-keyword">for</span> (<span class="cm-variable">c</span> <span class="cm-keyword">of</span> <span class="cm-variable-2">num</span>.<span class="cm-property">toString</span>())
    <span class="cm-variable">res</span> <span class="cm-operator">+=</span> <span class="cm-variable">String</span>(<span class="cm-variable">c</span><span class="cm-operator">**</span><span class="cm-number">2</span>);
  <span class="cm-keyword">return</span> <span class="cm-variable">Number</span>(<span class="cm-variable">res</span>);
}</code></pre></details>