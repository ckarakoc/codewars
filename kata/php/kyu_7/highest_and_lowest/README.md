# [Highest and Lowest](https://www.codewars.com/kata/554b4ac871d6813a03000035/train/php)
## Description
<div><p>In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.</p>
<p><strong>Example:</strong></p>
<pre><code class="language-php"><span class="cm-variable">highAndLow</span>(<span class="cm-string">"</span><span class="cm-string">1 2 3 4 5"</span>);  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"</span><span class="cm-string">1 2 -3 4 5"</span>); <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"</span><span class="cm-string">1 9 3 4 -5"</span>); <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Kata</span>.<span class="cm-variable">HighAndLow</span>(<span class="cm-string">"1 2 3 4 5"</span>);  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">HighAndLow</span>(<span class="cm-string">"1 2 -3 4 5"</span>); <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">HighAndLow</span>(<span class="cm-string">"1 9 3 4 -5"</span>); <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-fsharp"><span class="cm-variable">highAndLow</span> <span class="cm-string">"1 2 3 4 5"</span>  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span> <span class="cm-string">"1 2 -3 4 5"</span> <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span> <span class="cm-string">"1 9 3 4 -5"</span> <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 3 4 5"</span>);  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 -3 4 5"</span>); <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 9 3 4 -5"</span>); <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 3 4 5"</span>);  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 -3 4 5"</span>); <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 9 3 4 -5"</span>); <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 3 4 5"</span>);  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 -3 4 5"</span>); <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 9 3 4 -5"</span>); <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">highAndLow</span><span class="cm-punctuation">(</span><span class="cm-string">"1 2 3 4 5"</span><span class="cm-punctuation">)</span>  <span class="cm-comment"># return "5 1"</span>
<span class="cm-variable">highAndLow</span><span class="cm-punctuation">(</span><span class="cm-string">"1 2 -3 4 5"</span><span class="cm-punctuation">)</span> <span class="cm-comment"># return "5 -3"</span>
<span class="cm-variable">highAndLow</span><span class="cm-punctuation">(</span><span class="cm-string">"1 9 3 4 -5"</span><span class="cm-punctuation">)</span> <span class="cm-comment"># return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-comment"># return "5 1"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-comment"># return "5 -3"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-comment"># return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-comment"># return "5 1"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-comment"># return "5 -3"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-comment"># return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-crystal"><span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-comment"># return "5 1"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-comment"># return "5 -3"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-comment"># return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-r"><span class="cm-variable">high_and_low</span>(<span class="cm-string">"</span><span class="cm-string">1 2 3 4 5"</span>)  <span class="cm-comment"># return "5 1"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"</span><span class="cm-string">1 2 -3 4 5"</span>) <span class="cm-comment"># return "5 -3"</span>
<span class="cm-variable">high_and_low</span>(<span class="cm-string">"</span><span class="cm-string">1 9 3 4 -5"</span>) <span class="cm-comment"># return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">highAndLow</span> <span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-variable">#</span> <span class="cm-builtin">return</span> <span class="cm-string">"5 1"</span>
<span class="cm-variable">highAndLow</span> <span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-variable">#</span> <span class="cm-builtin">return</span> <span class="cm-string">"5 -3"</span>
<span class="cm-variable">highAndLow</span> <span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-variable">#</span> <span class="cm-builtin">return</span> <span class="cm-string">"9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-golang">HighAndLow("1 2 3 4 5")  // return "5 1"
HighAndLow("1 2 -3 4 5") // return "5 -3"
HighAndLow("1 9 3 4 -5") // return "9 -5"
</code></pre>
<pre style="display: none;"><code class="language-kotlin"><span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-comment">// return "5 1"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-comment">// return "5 -3"</span>
<span class="cm-variable">highAndLow</span>(<span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-comment">// return "9 -5"</span>
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">high_and_low</span>(<span class="cm-string">"1 2 3 4 5"</span>)  <span class="cm-comment"># return "5 1"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">high_and_low</span>(<span class="cm-string">"1 2 -3 4 5"</span>) <span class="cm-comment"># return "5 -3"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">high_and_low</span>(<span class="cm-string">"1 9 3 4 -5"</span>) <span class="cm-comment"># return "9 -5"</span>
</code></pre>
<p><strong>Notes:</strong></p>
<ul>
<li>All numbers are valid <code>Int32</code>, no <em>need</em> to validate them.</li>
<li>There will always be at least one number in the input string.</li>
<li>Output string must be two numbers separated by a single space, and highest number is first.</li>
</ul>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">highAndLow</span>(<span class="cm-variable-2">$numbers</span>) {
  <span class="cm-variable-2">$numbers_arr</span> <span class="cm-operator">=</span> <span class="cm-builtin">explode</span>(<span class="cm-string">"</span> <span class="cm-string">"</span>, <span class="cm-variable-2">$numbers</span>);
  <span class="cm-keyword">return</span> <span class="cm-builtin">max</span>(<span class="cm-variable-2">$numbers_arr</span>) . <span class="cm-string">"</span> <span class="cm-string">"</span> . <span class="cm-builtin">min</span>(<span class="cm-variable-2">$numbers_arr</span>);
}</code></pre></details>