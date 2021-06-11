# [Thinkful - String Drills: Repeater](https://www.codewars.com/kata/585a1a227cb58d8d740001c3/train/python)
## Description
<div><p>Write a function named <code>repeater()</code> that takes two arguments (a string and a number), and returns a new string where the input string is repeated that many times.</p>
<h2 id="example">Example:</h2>
<pre><code class="language-cpp"><span class="cm-variable">Repeater</span>.<span class="cm-variable">repeat</span>(<span class="cm-string">"a"</span>, <span class="cm-number">5</span>)
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">repeater</span>(<span class="cm-string">"a"</span>, <span class="cm-number">5</span>)
</code></pre>
<p>should return</p>
<pre><code class="language-cpp"><span class="cm-string">"aaaaa"</span>
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-string">"aaaaa"</span>
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">def</span> <span class="cm-def">repeater</span>(<span class="cm-variable">string</span>, <span class="cm-variable">n</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">string</span><span class="cm-operator"> * </span><span class="cm-variable">n</span></code></pre></details>