# [Complementary DNA](https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python)
## Description
<div><p>Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.</p>
<p>If you want to know more <a href="http://en.wikipedia.org/wiki/DNA" target="_blank">http://en.wikipedia.org/wiki/DNA</a></p>
<p>In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).</p>
<p>More similar exercise are found here <a href="http://rosalind.info/problems/list-view/" target="_blank">http://rosalind.info/problems/list-view/</a> (source)</p>
<pre><code class="language-python"><span class="cm-variable">DNA_strand</span> (<span class="cm-string">"ATTGC"</span>) <span class="cm-comment"># return "TAACG"</span>

<span class="cm-variable">DNA_strand</span> (<span class="cm-string">"GTAT"</span>) <span class="cm-comment"># return "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">DNAStrand</span> (<span class="cm-string">"ATTGC"</span>) <span class="cm-comment">// return "TAACG"</span>

<span class="cm-variable">DNAStrand</span> (<span class="cm-string">"GTAT"</span>) <span class="cm-comment">// return "CATA" </span>
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-variable">dnaStrand</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-comment">// return "TAACG"</span>

<span class="cm-variable">dnaStrand</span>(<span class="cm-string">"GTAT"</span>) <span class="cm-comment">// return "CATA" </span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">MakeComplement</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-string">"TAACG"</span>

<span class="cm-variable">MakeComplement</span>(<span class="cm-string">"GTAT"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-string">"CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">DNA_strand</span>(<span class="cm-string">"</span><span class="cm-string">ATTGC"</span>) <span class="cm-comment">// returns "TAACG"</span>
<span class="cm-variable">DNA_strand</span>(<span class="cm-string">"</span><span class="cm-string">GTAT"</span>) <span class="cm-comment">// returns "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-tag">DNA_strand</span> (<span class="cm-string">"ATTGC"</span>) <span class="cm-comment"># return "TAACG"</span>

<span class="cm-tag">DNA_strand</span> (<span class="cm-string">"GTAT"</span>) <span class="cm-comment"># return "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-crystal"><span class="cm-variable">dna_strand</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-comment"># return "TAACG"</span>

<span class="cm-variable">dna_strand</span>(<span class="cm-string">"GTAT"</span>) <span class="cm-comment"># return "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">DnaStrand</span>.<span class="cm-variable">makeComplement</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-comment">// return "TAACG"</span>

<span class="cm-variable">DnaStrand</span>.<span class="cm-variable">makeComplement</span>(<span class="cm-string">"GTAT"</span>) <span class="cm-comment">// return "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-kotlin"><span class="cm-variable">makeComplement</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-comment">// return "TAACG"</span>

<span class="cm-variable">makeComplement</span>(<span class="cm-string">"GTAT"</span>) <span class="cm-comment">// return "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">dnaStrand</span> []        `<span class="cm-variable">shouldBe</span>` []
<span class="cm-variable">dnaStrand</span> [<span class="cm-variable-2">A</span>,<span class="cm-variable-2">T</span>,<span class="cm-variable-2">G</span>,<span class="cm-variable-2">C</span>] `<span class="cm-variable">shouldBe</span>` [<span class="cm-variable-2">T</span>,<span class="cm-variable-2">A</span>,<span class="cm-variable-2">C</span>,<span class="cm-variable-2">G</span>]
<span class="cm-variable">dnaStrand</span> [<span class="cm-variable-2">G</span>,<span class="cm-variable-2">T</span>,<span class="cm-variable-2">A</span>,<span class="cm-variable-2">T</span>] `<span class="cm-variable">shouldBe</span>` [<span class="cm-variable-2">C</span>,<span class="cm-variable-2">A</span>,<span class="cm-variable-2">T</span>,<span class="cm-variable-2">A</span>]
<span class="cm-variable">dnaStrand</span> [<span class="cm-variable-2">A</span>,<span class="cm-variable-2">A</span>,<span class="cm-variable-2">A</span>,<span class="cm-variable-2">A</span>] `<span class="cm-variable">shouldBe</span>` [<span class="cm-variable-2">T</span>,<span class="cm-variable-2">T</span>,<span class="cm-variable-2">T</span>,<span class="cm-variable-2">T</span>]
</code></pre>
<pre style="display: none;"><code class="language-clojure"><span class="cm-bracket">(</span><span class="cm-builtin">is</span> <span class="cm-bracket">(</span><span class="cm-keyword">=</span> <span class="cm-bracket">(</span><span class="cm-builtin">dna-strand</span> <span class="cm-string">"ATTGC"</span><span class="cm-bracket">)</span> <span class="cm-string">"TAACG"</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span>

<span class="cm-bracket">(</span><span class="cm-builtin">is</span> <span class="cm-bracket">(</span><span class="cm-keyword">=</span> <span class="cm-bracket">(</span><span class="cm-builtin">dna-strand</span> <span class="cm-string">"GTAT"</span><span class="cm-bracket">)</span> <span class="cm-string">"CATA"</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span>
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">dna_strand</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-comment">/* return "TAACG" */</span>
<span class="cm-variable">dna_strand</span>(<span class="cm-string">"GTAT"</span>)  <span class="cm-comment">/* return "CATA"  */</span>
</code></pre>
<pre style="display: none;"><code class="language-golang">DNAStrand("ATTGC") // returns "TAACG"

DNAStrand("GTAT") // returns "CATA"
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">dna_strand</span>(<span class="cm-string">"</span><span class="cm-string">ATTGC</span><span class="cm-string">"</span>) <span class="cm-comment">// returns "TAACG"</span>
<span class="cm-variable">dna_strand</span>(<span class="cm-string">"</span><span class="cm-string">GTAT</span><span class="cm-string">"</span>)  <span class="cm-comment">// returns "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-julia"><span class="cm-variable">dnastrand</span>(<span class="cm-string">"ATTGC</span><span class="cm-string">"</span>) <span class="cm-comment"># returns "TAACG"</span>
<span class="cm-variable">dnastrand</span>(<span class="cm-string">"GTAT</span><span class="cm-string">"</span>)  <span class="cm-comment"># returns "CATA"</span>
</code></pre>
<pre style="display: none;"><code class="language-prolog"><span class="cm-atom">dna_strand</span><span class="cm-paren">(</span><span class="cm-string">"</span><span class="cm-string">A</span><span class="cm-string">T</span><span class="cm-string">T</span><span class="cm-string">G</span><span class="cm-string">C</span><span class="cm-string">"</span><span class="cm-paren">)</span><span class="cm-comment"> </span><span class="cm-graphic">==</span><span class="cm-comment"> </span><span class="cm-string">"</span><span class="cm-string">T</span><span class="cm-string">A</span><span class="cm-string">A</span><span class="cm-string">C</span><span class="cm-string">G</span><span class="cm-string">"</span>
<span class="cm-atom">dna_strand</span><span class="cm-paren">(</span><span class="cm-string">"</span><span class="cm-string">G</span><span class="cm-string">T</span><span class="cm-string">A</span><span class="cm-string">T</span><span class="cm-string">"</span><span class="cm-paren">)</span><span class="cm-comment"> </span><span class="cm-graphic">==</span><span class="cm-comment"> </span><span class="cm-string">"</span><span class="cm-string">C</span><span class="cm-string">A</span><span class="cm-string">T</span><span class="cm-string">A</span><span class="cm-string">"</span>
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-tag">Dna</span><span class="cm-operator">.</span><span class="cm-property">dna_strand</span>(<span class="cm-string">"ATTGC"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"TAACG"</span>
<span class="cm-tag">Dna</span><span class="cm-operator">.</span><span class="cm-property">dna_strand</span>(<span class="cm-string">"GTAT"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"CATA"</span>
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">def</span> <span class="cm-def">DNA_strand</span>(<span class="cm-variable">dna</span>):
    <span class="cm-variable">compl</span> <span class="cm-operator">=</span> { <span class="cm-string">'A'</span>:<span class="cm-string">'T'</span>, <span class="cm-string">'T'</span>:<span class="cm-string">'A'</span>, <span class="cm-string">'C'</span>:<span class="cm-string">'G'</span>, <span class="cm-string">'G'</span>:<span class="cm-string">'C'</span> }
    <span class="cm-keyword">return</span> <span class="cm-string">''</span>.<span class="cm-property">join</span>(<span class="cm-variable">compl</span>[<span class="cm-variable">s</span>] <span class="cm-keyword">for</span> <span class="cm-variable">s</span> <span class="cm-keyword">in</span> <span class="cm-variable">dna</span>)</code></pre></details>