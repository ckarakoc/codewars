# [Replace With Alphabet Position](https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python)
## Description
<div><p>Welcome.</p>
<p>In this kata you are required to, given a string, replace every letter with its position in the alphabet.</p>
<p>If anything in the text isn't a letter, ignore it and don't return it.</p>
<p><code>"a" = 1</code>, <code>"b" = 2</code>, etc.</p>
<h2 id="example">Example</h2>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">alphabetPosition</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>)
</code></pre>
<pre><code class="language-python"><span class="cm-variable">alphabet_position</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>)
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">alphabet_position</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>)
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Kata</span>.<span class="cm-variable">AlphabetPosition</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>)
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">alphabet_position</span>(<span class="cm-string">'The sunset sets at twelve o\' clock.'</span>);
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">alphabet_position</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>);
</code></pre>
<pre style="display: none;"><code class="language-nasm"><span class="cm-tag">text:</span>  <span class="cm-tag">db</span>  <span class="cm-string">"The</span> sunset <span class="cm-keyword">sets</span> at twelve o<span class="cm-string">'</span> clock.<span class="cm-string">"</span>,<span class="cm-number">0</span>h0

<span class="cm-tag">main:</span>
    <span class="cm-keyword">mov</span> <span class="cm-builtin">rdi</span>, text
    <span class="cm-keyword">call</span> alphabet_position
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">alphabet_position</span>(<span class="cm-string">"</span><span class="cm-string">The sunset sets at twelve o' clock.</span><span class="cm-string">"</span>)
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-variable">alphabetPosition</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>)
</code></pre>
<pre style="display: none;"><code class="language-groovy"><span class="cm-variable">Kata</span>.<span class="cm-property">alphabetPosition</span>(<span class="cm-string">"The sunset sets at twelve o' clock."</span>)
</code></pre>
<p>Should return <code>"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"</code> (as a string)</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">import</span> <span class="cm-variable">re</span>
<span class="cm-keyword">def</span> <span class="cm-def">alphabet_position</span>(<span class="cm-variable">text</span>):
    <span class="cm-keyword">return</span> <span class="cm-string">' '</span>.<span class="cm-property">join</span>(<span class="cm-builtin">str</span>(<span class="cm-builtin">ord</span>(<span class="cm-variable">c</span>) <span class="cm-operator">-</span> <span class="cm-number">96</span>) <span class="cm-keyword">for</span> <span class="cm-variable">c</span> <span class="cm-keyword">in</span> <span class="cm-variable">re</span>.<span class="cm-property">sub</span>(<span class="cm-string">'[^a-zA-Z]'</span>, <span class="cm-string">''</span>, <span class="cm-variable">text</span>.<span class="cm-property">lower</span>()))</code></pre></details>