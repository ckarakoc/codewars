# [A Needle in the Haystack](https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python)
## Description
<div><p>Can you find the needle in the haystack?</p>
<p>Write a function <code>findNeedle()</code> that takes an <code>array</code> full of junk but containing one <code>"needle"</code></p>
<p>After your function finds the needle it should return a message (as a string) that says:</p>
<p><code>"found the needle at position "</code> plus the <code>index</code> it found the needle, so: </p>
<pre><code class="language-python"><span class="cm-variable">find_needle</span>([<span class="cm-string">'hay'</span>, <span class="cm-string">'junk'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'moreJunk'</span>, <span class="cm-string">'needle'</span>, <span class="cm-string">'randomJunk'</span>])
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">find_needle</span>([<span class="cm-string">'hay'</span>, <span class="cm-string">'junk'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'moreJunk'</span>, <span class="cm-string">'needle'</span>, <span class="cm-string">'randomJunk'</span>])
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-variable">find_needle</span>([<span class="cm-string">'hay'</span>, <span class="cm-string">'junk'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'moreJunk'</span>, <span class="cm-string">'needle'</span>, <span class="cm-string">'randomJunk'</span>])
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">findNeedle</span>([<span class="cm-string">'hay'</span>, <span class="cm-string">'junk'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'moreJunk'</span>, <span class="cm-string">'needle'</span>, <span class="cm-string">'randomJunk'</span>])
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-variable">findNeedle</span>([<span class="cm-string">'hay'</span>, <span class="cm-string">'junk'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'hay'</span>, <span class="cm-string">'moreJunk'</span>, <span class="cm-string">'needle'</span>, <span class="cm-string">'randomJunk'</span>])
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">findNeedle</span>(<span class="cm-keyword">new</span> <span class="cm-type">Object</span>[] {<span class="cm-string">"hay"</span>, <span class="cm-string">"junk"</span>, <span class="cm-string">"hay"</span>, <span class="cm-string">"hay"</span>, <span class="cm-string">"moreJunk"</span>, <span class="cm-string">"needle"</span>, <span class="cm-string">"randomJunk"</span>})
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">findNeedle</span> [<span class="cm-string">"hay"</span>, <span class="cm-string">"junk"</span>, <span class="cm-string">"hay"</span>, <span class="cm-string">"hay"</span>, <span class="cm-string">"moreJunk"</span>, <span class="cm-string">"needle"</span>, <span class="cm-string">"randomJunk"</span>]
</code></pre>
<pre style="display: none;"><code class="language-racket"><span class="cm-bracket">(</span><span class="cm-variable">find-needle</span> <span class="cm-atom">'</span><span class="cm-atom">(</span><span class="cm-atom">"</span><span class="cm-atom">hay"</span> <span class="cm-atom">"</span><span class="cm-atom">junk"</span> <span class="cm-atom">"</span><span class="cm-atom">hay"</span> <span class="cm-atom">"</span><span class="cm-atom">hay"</span> <span class="cm-atom">"</span><span class="cm-atom">moreJunk"</span> <span class="cm-atom">"</span><span class="cm-atom">needle"</span><span class="cm-atom">,</span><span class="cm-atom">"</span><span class="cm-atom">randomJunk"</span><span class="cm-atom">)</span><span class="cm-bracket">)</span>
</code></pre>
<p>should return <code>"found the needle at position 5"</code></p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">def</span> <span class="cm-def">find_needle</span>(<span class="cm-variable">haystack</span>):
    <span class="cm-keyword">return</span> <span class="cm-string">f"found the needle at position </span>{<span class="cm-variable">haystack</span>.<span class="cm-property">index</span>(<span class="cm-string">'needle'</span>)}<span class="cm-string">"</span></code></pre></details>