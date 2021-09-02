# [Counting Duplicates](https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/javascript)
## Description
<div><h3 id="count-the-number-of-duplicates">Count the number of Duplicates</h3>
<p>Write a function that will return the count of <strong>distinct case-insensitive</strong> alphabetic characters and numeric digits that occur more than 
once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.</p>
<h3 id="example">Example</h3>
<p>"abcde" -&gt; 0             <code># no characters repeats more than once</code><br/>"aabbcde" -&gt; 2           <code># 'a' and 'b'</code><br/>"aabBcde" -&gt; 2           <code># 'a' occurs twice and 'b' twice (`b` and `B`)</code><br/>"indivisibility" -&gt; 1    <code># 'i' occurs six times</code><br/>"Indivisibilities" -&gt; 2  <code># 'i' occurs seven times and 's' occurs twice</code><br/>"aA11" -&gt; 2              <code># 'a' and '1'</code><br/>"ABBA" -&gt; 2              <code># 'A' and 'B' each occur twice</code></p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">duplicateCount</span>(<span class="cm-def">text</span>){
  <span class="cm-keyword">let</span> <span class="cm-def">counter</span> <span class="cm-operator">=</span> {}
  <span class="cm-variable">Array</span>.<span class="cm-property">from</span>(<span class="cm-variable-2">text</span>.<span class="cm-property">toLowerCase</span>()).<span class="cm-property">forEach</span>(<span class="cm-def">c</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">counter</span>[<span class="cm-variable-2">c</span>] <span class="cm-operator">?</span> <span class="cm-variable-2">counter</span>[<span class="cm-variable-2">c</span>] <span class="cm-operator">+=</span> <span class="cm-number">1</span> : <span class="cm-variable-2">counter</span>[<span class="cm-variable-2">c</span>] <span class="cm-operator">=</span> <span class="cm-number">1</span>);
  <span class="cm-keyword">return</span> <span class="cm-variable">Object</span>.<span class="cm-property">values</span>(<span class="cm-variable-2">counter</span>).<span class="cm-property">filter</span>(<span class="cm-def">a</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">a</span> <span class="cm-operator">&gt;</span> <span class="cm-number">1</span>).<span class="cm-property">length</span>;
}</code></pre></details>