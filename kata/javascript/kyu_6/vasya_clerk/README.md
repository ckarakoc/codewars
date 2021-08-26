# [Vasya - Clerk](https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/javascript)
## Description
<div><p>The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single <code>100</code>, <code>50</code> or <code>25</code> dollar bill. An "Avengers" ticket costs <code>25 dollars</code>.</p>
<p>Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line. </p>
<p>Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?</p>
<p>Return <code>YES</code>, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return <code>NO</code>.</p>
<h3 id="examples">Examples:</h3>



<pre><code class="language-javascript"><span class="cm-variable">tickets</span>([<span class="cm-number">25</span>, <span class="cm-number">25</span>, <span class="cm-number">50</span>]) <span class="cm-comment">// =&gt; YES </span>
<span class="cm-variable">tickets</span>([<span class="cm-number">25</span>, <span class="cm-number">100</span>]) <span class="cm-comment">// =&gt; NO. Vasya will not have enough money to give change to 100 dollars</span>
<span class="cm-variable">tickets</span>([<span class="cm-number">25</span>, <span class="cm-number">25</span>, <span class="cm-number">50</span>, <span class="cm-number">50</span>, <span class="cm-number">100</span>]) <span class="cm-comment">// =&gt; NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)</span>
</code></pre>






</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">tickets</span>(<span class="cm-def">peopleInLine</span>) {
  <span class="cm-keyword">let</span> <span class="cm-def">change</span> <span class="cm-operator">=</span> { <span class="cm-number cm-property">25</span>: <span class="cm-number">0</span>, <span class="cm-number cm-property">50</span>:<span class="cm-number">0</span>, <span class="cm-number cm-property">100</span>:<span class="cm-number">0</span> }
  <span class="cm-keyword">for</span> (<span class="cm-keyword">const</span> <span class="cm-def">m</span> <span class="cm-keyword">of</span> <span class="cm-variable-2">peopleInLine</span>) {
    <span class="cm-variable-2">change</span>[<span class="cm-variable-2">m</span>]<span class="cm-operator">++</span>;
    <span class="cm-keyword">let</span> <span class="cm-def">count</span> <span class="cm-operator">=</span> <span class="cm-variable-2">m</span>;
    <span class="cm-keyword">while</span> (<span class="cm-variable-2">count</span> <span class="cm-operator">&gt;</span> <span class="cm-number">50</span> <span class="cm-operator">&amp;&amp;</span> <span class="cm-variable-2">change</span>[<span class="cm-number">50</span>]) {
      <span class="cm-variable-2">count</span> <span class="cm-operator">-=</span> <span class="cm-number">50</span>;
      <span class="cm-variable-2">change</span>[<span class="cm-number">50</span>]<span class="cm-operator">--</span>;
    }
    <span class="cm-keyword">while</span> (<span class="cm-variable-2">count</span> <span class="cm-operator">&gt;</span> <span class="cm-number">25</span> <span class="cm-operator">&amp;&amp;</span> <span class="cm-variable-2">change</span>[<span class="cm-number">25</span>]) {
      <span class="cm-variable-2">count</span> <span class="cm-operator">-=</span> <span class="cm-number">25</span>;
      <span class="cm-variable-2">change</span>[<span class="cm-number">25</span>]<span class="cm-operator">--</span>;
    }
    <span class="cm-keyword">if</span> (<span class="cm-variable-2">count</span> <span class="cm-operator">!==</span> <span class="cm-number">25</span>) <span class="cm-keyword">return</span> <span class="cm-string">"NO"</span>;
  }
  <span class="cm-keyword">return</span> <span class="cm-string">"YES"</span>;
}</code></pre></details>