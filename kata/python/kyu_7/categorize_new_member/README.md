# [Categorize New Member](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python)
## Description
<div><p>The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.</p>
<p>To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.</p>
<h2 id="input">Input</h2>
<p>Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.</p>
<p>Note for F#: The input will be of (int list list)
which is a List&lt;List&gt;</p>
<h3 id="example-input">Example Input</h3>
<pre><code class="language-python">[[<span class="cm-number">18</span>, <span class="cm-number">20</span>],[<span class="cm-number">45</span>, <span class="cm-number">2</span>],[<span class="cm-number">61</span>, <span class="cm-number">12</span>],[<span class="cm-number">37</span>, <span class="cm-number">6</span>],[<span class="cm-number">21</span>, <span class="cm-number">21</span>],[<span class="cm-number">78</span>, <span class="cm-number">9</span>]]
</code></pre>
<pre style="display: none;"><code class="language-ruby">[[<span class="cm-number">18</span>, <span class="cm-number">20</span>],[<span class="cm-number">45</span>, <span class="cm-number">2</span>],[<span class="cm-number">61</span>, <span class="cm-number">12</span>],[<span class="cm-number">37</span>, <span class="cm-number">6</span>],[<span class="cm-number">21</span>, <span class="cm-number">21</span>],[<span class="cm-number">78</span>, <span class="cm-number">9</span>]]
</code></pre>
<pre style="display: none;"><code class="language-javascript">[[<span class="cm-number">18</span>, <span class="cm-number">20</span>],[<span class="cm-number">45</span>, <span class="cm-number">2</span>],[<span class="cm-number">61</span>, <span class="cm-number">12</span>],[<span class="cm-number">37</span>, <span class="cm-number">6</span>],[<span class="cm-number">21</span>, <span class="cm-number">21</span>],[<span class="cm-number">78</span>, <span class="cm-number">9</span>]]
</code></pre>
<pre style="display: none;"><code class="language-haskell">[(<span class="cm-number">18</span>, <span class="cm-number">20</span>),(<span class="cm-number">45</span>, <span class="cm-number">2</span>),(<span class="cm-number">61</span>, <span class="cm-number">12</span>),(<span class="cm-number">37</span>, <span class="cm-number">6</span>),(<span class="cm-number">21</span>, <span class="cm-number">21</span>),(<span class="cm-number">78</span>, <span class="cm-number">9</span>)]
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-keyword">new</span> <span class="cm-type">int</span>[][] {<span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">18</span>, <span class="cm-number">20</span>}, <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">45</span>, <span class="cm-number">2</span>}, <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">61</span>, <span class="cm-number">12</span>}, <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">37</span>, <span class="cm-number">6</span>}, <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">21</span>, <span class="cm-number">21</span>}, <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">78</span>, <span class="cm-number">9</span>}}
</code></pre>
<pre style="display: none;"><code class="language-fsharp">[[<span class="cm-number">18</span>; <span class="cm-number">20</span>];[<span class="cm-number">45</span>; <span class="cm-number">2</span>];[<span class="cm-number">61</span>; <span class="cm-number">12</span>];[<span class="cm-number">37</span>; <span class="cm-number">6</span>];[<span class="cm-number">21</span>; <span class="cm-number">21</span>];[<span class="cm-number">78</span>; <span class="cm-number">9</span>]]
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable-3">vec!</span>[(<span class="cm-number">45</span>, <span class="cm-number">12</span>), (<span class="cm-number">55</span>,<span class="cm-number">21</span>), (<span class="cm-number">19</span>, <span class="cm-operator">-</span><span class="cm-number">2</span>), (<span class="cm-number">104</span>, <span class="cm-number">20</span>)])
</code></pre>
<pre style="display: none;"><code class="language-groovy">[<span class="cm-keyword">new</span> <span class="cm-variable">Tuple</span>(<span class="cm-number">45</span>, <span class="cm-number">12</span>), <span class="cm-keyword">new</span> <span class="cm-variable">Tuple</span>(<span class="cm-number">55</span>,<span class="cm-number">21</span>), <span class="cm-keyword">new</span> <span class="cm-variable">Tuple</span>(<span class="cm-number">19</span>, <span class="cm-operator">-</span><span class="cm-number">2</span>), <span class="cm-keyword">new</span> <span class="cm-variable">Tuple</span>(<span class="cm-number">104</span>, <span class="cm-number">20</span>)]
</code></pre>
<h2 id="output">Output</h2>
<p>Output will consist of a list of string values (in Haskell: <code>Open</code> or <code>Senior</code>) stating whether the respective member is to be placed in the senior or open category.</p>
<h3 id="example-output">Example Output</h3>
<pre><code class="language-python">[<span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>]
</code></pre>
<pre style="display: none;"><code class="language-ruby">[<span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>]
</code></pre>
<pre style="display: none;"><code class="language-javascript">[<span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>]
</code></pre>
<pre style="display: none;"><code class="language-haskell">[<span class="cm-variable-2">Open</span>, <span class="cm-variable-2">Open</span>, <span class="cm-variable-2">Senior</span>, <span class="cm-variable-2">Open</span>, <span class="cm-variable-2">Open</span>, <span class="cm-variable-2">Senior</span>]
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-keyword">new</span> <span class="cm-type">string</span>[] {<span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>}
</code></pre>
<pre style="display: none;"><code class="language-fsharp">[<span class="cm-string">"Open"</span>; <span class="cm-string">"Open"</span>; <span class="cm-string">"Senior"</span>; <span class="cm-string">"Open"</span>; <span class="cm-string">"Open"</span>; <span class="cm-string">"Senior"</span>]
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable-3">vec!</span>[<span class="cm-string">"</span><span class="cm-string">Open</span><span class="cm-string">"</span>, <span class="cm-string">"</span><span class="cm-string">Senior</span><span class="cm-string">"</span>, <span class="cm-string">"</span><span class="cm-string">Open</span><span class="cm-string">"</span>, <span class="cm-string">"</span><span class="cm-string">Senior</span><span class="cm-string">"</span>]
</code></pre>
<pre style="display: none;"><code class="language-groovy">[<span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>, <span class="cm-string">"Open"</span>, <span class="cm-string">"Senior"</span>]
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">def</span> <span class="cm-def">open_or_senior</span>(<span class="cm-variable">data</span>):
    <span class="cm-keyword">return</span> [<span class="cm-string">'Senior'</span> <span class="cm-keyword">if</span> <span class="cm-variable">age</span> <span class="cm-operator">&gt;</span> <span class="cm-number">54</span> <span class="cm-keyword">and</span> <span class="cm-variable">handicap</span> <span class="cm-operator">&gt;</span> <span class="cm-number">7</span> <span class="cm-keyword">else</span> <span class="cm-string">'Open'</span> <span class="cm-keyword">for</span> <span class="cm-variable">age</span>, <span class="cm-variable">handicap</span> <span class="cm-keyword">in</span> <span class="cm-variable">data</span>]</code></pre></details>