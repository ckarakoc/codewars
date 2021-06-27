# [Credit Card Mask](https://www.codewars.com/kata/5412509bd436bd33920011bc/train/javascript)
## Description
<div><p>Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.</p>
<p>Your task is to write a function <code>maskify</code>, which changes all but the last four characters into <code>'#'</code>.</p>
<h2 id="examples">Examples</h2>
<pre><code class="language-javascript"><span class="cm-variable">maskify</span>(<span class="cm-string">"4556364607935616"</span>) <span class="cm-operator">==</span> <span class="cm-string">"############5616"</span>
<span class="cm-variable">maskify</span>(     <span class="cm-string">"64607935616"</span>) <span class="cm-operator">==</span>      <span class="cm-string">"#######5616"</span>
<span class="cm-variable">maskify</span>(               <span class="cm-string">"1"</span>) <span class="cm-operator">==</span>                <span class="cm-string">"1"</span>
<span class="cm-variable">maskify</span>(                <span class="cm-string">""</span>) <span class="cm-operator">==</span>                 <span class="cm-string">""</span>

<span class="cm-comment">// "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">"Skippy"</span>)                                   <span class="cm-operator">==</span> <span class="cm-string">"##ippy"</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">"Nananananananananananananananana Batman!"</span>) <span class="cm-operator">==</span> <span class="cm-string">"####################################man!"</span>
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"4556364607935616"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span> <span class="cm-string">"############5616"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span>     <span class="cm-string">"64607935616"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span>      <span class="cm-string">"#######5616"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span>               <span class="cm-string">"1"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span>                <span class="cm-string">"1"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span>                <span class="cm-string">""</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span>                 <span class="cm-string">""</span>

<span class="cm-comment"># "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"Skippy"</span><span class="cm-punctuation">)</span>                                   <span class="cm-operator">==</span> <span class="cm-string">"##ippy"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"Nananananananananananananananana Batman!"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span> <span class="cm-string">"####################################man!"</span>
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">maskify</span>(<span class="cm-string">"4556364607935616"</span>) <span class="cm-operator">==</span> <span class="cm-string">"############5616"</span>
<span class="cm-variable">maskify</span>(     <span class="cm-string">"64607935616"</span>) <span class="cm-operator">==</span>      <span class="cm-string">"#######5616"</span>
<span class="cm-variable">maskify</span>(               <span class="cm-string">"1"</span>) <span class="cm-operator">==</span>                <span class="cm-string">"1"</span>
<span class="cm-variable">maskify</span>(                <span class="cm-string">""</span>) <span class="cm-operator">==</span>                 <span class="cm-string">""</span>

<span class="cm-comment"># "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">"Skippy"</span>)                                   <span class="cm-operator">==</span> <span class="cm-string">"##ippy"</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">"Nananananananananananananananana Batman!"</span>) <span class="cm-operator">==</span> <span class="cm-string">"####################################man!"</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">maskify</span> <span class="cm-string">"4556364607935616"</span> <span class="cm-builtin">==</span> <span class="cm-string">"############5616"</span>
<span class="cm-variable">maskify</span>      <span class="cm-string">"64607935616"</span> <span class="cm-builtin">==</span>      <span class="cm-string">"#######5616"</span>
<span class="cm-variable">maskify</span>                <span class="cm-string">"1"</span> <span class="cm-builtin">==</span>                <span class="cm-string">"1"</span>
<span class="cm-variable">maskify</span>                 <span class="cm-string">""</span> <span class="cm-builtin">==</span>                 <span class="cm-string">""</span>

<span class="cm-comment">-- "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span> <span class="cm-string">"Skippy"</span> <span class="cm-builtin">==</span> <span class="cm-string">"##ippy"</span>
<span class="cm-variable">maskify</span> <span class="cm-string">"Nananananananananananananananana Batman!"</span>
     <span class="cm-comment">-- "####################################man!"</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">maskify</span>(<span class="cm-string">'4556364607935616'</span>) <span class="cm-comment"># should return '############5616'</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">'64607935616'</span>)      <span class="cm-comment"># should return '#######5616'</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">'1'</span>)                <span class="cm-comment"># should return '1'</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">''</span>)                 <span class="cm-comment"># should return ''</span>

<span class="cm-comment"># "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">'Skippy'</span>)                                   <span class="cm-comment"># should return '##ippy'</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">'Nananananananananananananananana Batman!'</span>) <span class="cm-comment"># should return '####################################man!'</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Kata</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"4556364607935616"</span>); <span class="cm-comment">// should return "############5616"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"64607935616"</span>);      <span class="cm-comment">// should return "#######5616"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"1"</span>);                <span class="cm-comment">// should return "1"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">""</span>);                 <span class="cm-comment">// should return ""</span>

<span class="cm-comment">// "What was the name of your first pet?"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"Skippy"</span>);                                   <span class="cm-comment">// should return "##ippy"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"Nananananananananananananananana Batman!"</span>); <span class="cm-comment">// should return "####################################man!"</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">Maskify</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"4556364607935616"</span>); <span class="cm-comment">// should return "############5616"</span>
<span class="cm-variable">Maskify</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"64607935616"</span>);      <span class="cm-comment">// should return "#######5616"</span>
<span class="cm-variable">Maskify</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"1"</span>);                <span class="cm-comment">// should return "1"</span>
<span class="cm-variable">Maskify</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">""</span>);                 <span class="cm-comment">// should return ""</span>

<span class="cm-comment">// "What was the name of your first pet?"</span>
<span class="cm-variable">Maskify</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"Skippy"</span>);                                   <span class="cm-comment">// should return "##ippy"</span>
<span class="cm-variable">Maskify</span>.<span class="cm-variable">Maskify</span>(<span class="cm-string">"Nananananananananananananananana Batman!"</span>); <span class="cm-comment">// should return "####################################man!"</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">maskify</span>(<span class="cm-string">"</span><span class="cm-string">4556364607935616</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-variable">String</span>::<span class="cm-variable">from</span>(<span class="cm-string">"</span><span class="cm-string">############5616</span><span class="cm-string">"</span>);
<span class="cm-variable">maskify</span>(<span class="cm-string">"</span><span class="cm-string">64607935616</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-variable">String</span>::<span class="cm-variable">from</span>(<span class="cm-string">"</span><span class="cm-string">#######5616</span><span class="cm-string">"</span>);
<span class="cm-variable">maskify</span>(<span class="cm-string">"</span><span class="cm-string">1</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-variable">String</span>::<span class="cm-variable">from</span>(<span class="cm-string">"</span><span class="cm-string">1</span><span class="cm-string">"</span>);
<span class="cm-variable">maskify</span>(<span class="cm-string">"</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-variable">String</span>::<span class="cm-variable">from</span>(<span class="cm-string">"</span><span class="cm-string">"</span>);


<span class="cm-comment">// "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span>(<span class="cm-string">"</span><span class="cm-string">Skippy</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-variable">String</span>::<span class="cm-variable">from</span>(<span class="cm-string">"</span><span class="cm-string">##ippy</span><span class="cm-string">"</span>);
<span class="cm-variable">maskify</span>(<span class="cm-string">"</span><span class="cm-string">Nananananananananananananananana Batman!</span><span class="cm-string">"</span>) <span class="cm-operator">==</span><span class="cm-variable">String</span>::<span class="cm-variable">from</span>(<span class="cm-string">"</span><span class="cm-string">####################################man!</span><span class="cm-string">"</span>);
</code></pre>
<pre style="display: none;"><code class="language-swift"><span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"4556364607935616"</span><span class="cm-punctuation">)</span> <span class="cm-comment">// should return "############5616"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"64607935616"</span><span class="cm-punctuation">)</span>      <span class="cm-comment">// should return "#######5616"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"1"</span><span class="cm-punctuation">)</span>                <span class="cm-comment">// should return "1"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">""</span><span class="cm-punctuation">)</span>                 <span class="cm-comment">// should return ""</span>

<span class="cm-comment">// "What was the name of your first pet?"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"Skippy"</span><span class="cm-punctuation">)</span>                                   <span class="cm-comment">// should return "##ippy"</span>
<span class="cm-variable">maskify</span><span class="cm-punctuation">(</span><span class="cm-string">"Nananananananananananananananana Batman!"</span><span class="cm-punctuation">)</span> <span class="cm-comment">// should return "####################################man!"</span>
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-comment">// return masked string</span>
<span class="cm-keyword">function</span> <span class="cm-def">maskify</span>(<span class="cm-def">cc</span>) {
  <span class="cm-keyword">if</span> (<span class="cm-variable-2">cc</span>.<span class="cm-property">length</span> <span class="cm-operator">&lt;=</span> <span class="cm-number">4</span>) <span class="cm-keyword">return</span> <span class="cm-variable-2">cc</span>;
  <span class="cm-keyword">return</span> <span class="cm-string">'#'</span>.<span class="cm-property">repeat</span>(<span class="cm-variable-2">cc</span>.<span class="cm-property">length</span> <span class="cm-operator">-</span> <span class="cm-number">4</span>) <span class="cm-operator">+</span> <span class="cm-variable-2">cc</span>.<span class="cm-property">substring</span>(<span class="cm-variable-2">cc</span>.<span class="cm-property">length</span> <span class="cm-operator">-</span> <span class="cm-number">4</span>, <span class="cm-variable-2">cc</span>.<span class="cm-property">length</span>);
}</code></pre></details>