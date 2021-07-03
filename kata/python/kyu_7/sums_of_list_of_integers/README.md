# [Sums of List of Integers](https://www.codewars.com/kata/60e05af1c2f51e000da1a2d2/train/python)
## Description
<div><p>Given an array of integers, give all possible ways the integers can be added to a certain value. </p>
<ul>
<li>The output should be a list of lists containing all correct sums.</li>
<li>The resulting list should not contain duplicates.</li>
<li>The resulting sums should be in increasing order (i.e. sorted)</li>
</ul>
<p>Example:</p>
<pre><code>Give sums to 12:
   ✓ [1,2,3,3,5,7] =&gt; [5, 7], [2, 3, 7], [1, 3, 3, 5]
   X [1,2,3,3,5,7] =&gt; [7, 5], [2, 3, 7], [1, 3, 3, 5]
   X [1,2,3,3,5,7] =&gt; [7, 5], [2, 3, 7], [2, 3, 7], [1, 3, 3, 5]
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">import</span> <span class="cm-variable">itertools</span>

<span class="cm-keyword">def</span> <span class="cm-def">equals_sum</span>(<span class="cm-variable">num_arr</span>, <span class="cm-variable">total</span>):
    <span class="cm-variable">res</span> <span class="cm-operator">=</span> []
    <span class="cm-keyword">for</span> <span class="cm-variable">i</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">num_arr</span>) <span class="cm-operator">+</span> <span class="cm-number">1</span>):
        <span class="cm-keyword">for</span> <span class="cm-variable">c</span> <span class="cm-keyword">in</span> <span class="cm-variable">itertools</span>.<span class="cm-property">combinations</span>(<span class="cm-variable">num_arr</span>, <span class="cm-variable">i</span>):
            <span class="cm-keyword">if</span> <span class="cm-builtin">sum</span>(<span class="cm-variable">c</span>) <span class="cm-operator">==</span> <span class="cm-variable">total</span>:
                <span class="cm-variable">res</span>.<span class="cm-property">append</span>(<span class="cm-builtin">list</span>(<span class="cm-variable">c</span>))
                <span class="cm-variable">res</span>[<span class="cm-operator">-</span><span class="cm-number">1</span>].<span class="cm-property">sort</span>()
    <span class="cm-variable">res</span> <span class="cm-operator">=</span> <span class="cm-builtin">list</span>(<span class="cm-variable">k</span> <span class="cm-keyword">for</span> <span class="cm-variable">k</span>,<span class="cm-variable">_</span> <span class="cm-keyword">in</span> <span class="cm-variable">itertools</span>.<span class="cm-property">groupby</span>(<span class="cm-variable">res</span>))
    <span class="cm-keyword">return</span> <span class="cm-variable">res</span></code></pre></details>