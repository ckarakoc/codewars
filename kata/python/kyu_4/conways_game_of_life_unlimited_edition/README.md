# [Conway's Game of Life  - Unlimited Edition](https://www.codewars.com/kata/52423db9add6f6fc39000354/train/python)
## Description
<div><p>Given a 2D array and a number of generations, compute n timesteps of <a href="http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Conway's Game of Life</a>.</p>
<p>The rules of the game are:</p>
<ol>
<li>Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.</li>
<li>Any live cell with more than three live neighbours dies, as if by overcrowding.</li>
<li>Any live cell with two or three live neighbours lives on to the next generation.</li>
<li>Any dead cell with exactly three live neighbours becomes a live cell.</li>
</ol>
<p>Each cell's neighborhood is the 8 cells immediately around it (i.e. <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">Moore Neighborhood</a>). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return <code>[[]]</code>.)</p>
<p>For illustration purposes, 0 and 1 will be represented as <code>░░</code> and <code>▓▓</code> blocks respectively (PHP, <strong>C</strong>: plain black and white squares). You can take advantage of the <code>htmlize</code> function to get a text representation of the universe, e.g.:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">console</span>.<span class="cm-property">log</span>(<span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>));
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">console</span><span class="cm-punctuation">.</span><span class="cm-property">log</span> <span class="cm-variable">htmlize</span><span class="cm-punctuation">(</span><span class="cm-variable">cells</span><span class="cm-punctuation">)</span>
</code></pre>
<pre><code class="language-python">def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)

<span class="cm-builtin">print</span>(<span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>))
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">trace</span> (<span class="cm-variable">htmlize</span> <span class="cm-variable">cells</span>)
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">System</span>.<span class="cm-variable">out</span>.<span class="cm-variable">println</span>(<span class="cm-variable">LifeDebug</span>.<span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>));
</code></pre>
<pre style="display: none;"><code class="language-swift"><span class="cm-variable">print</span><span class="cm-punctuation">(</span><span class="cm-variable">htmlize</span><span class="cm-punctuation">(</span><span class="cm-variable">cells</span><span class="cm-punctuation">)</span><span class="cm-punctuation">)</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-keyword">echo</span> <span class="cm-variable">htmlize</span>(<span class="cm-variable-2">$cells</span>) . <span class="cm-string">"</span><span class="cm-string">\r\n"</span>;
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-type">char</span> <span class="cm-type">&ast;</span><span class="cm-variable">universe</span> <span class="cm-operator">=</span> <span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>, <span class="cm-variable">rows</span>, <span class="cm-variable">columns</span>);
<span class="cm-variable">printf</span>(<span class="cm-variable">universe</span>);
<span class="cm-variable">free</span>(<span class="cm-variable">universe</span>);
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">from</span> <span class="cm-variable">copy</span> <span class="cm-keyword">import</span> <span class="cm-variable">deepcopy</span>
<span class="cm-keyword">import</span> <span class="cm-variable">sys</span>

<span class="cm-keyword">def</span> <span class="cm-def">get_generation</span>(<span class="cm-variable">cells</span>, <span class="cm-variable">generations</span>):
    <span class="cm-keyword">if</span> <span class="cm-builtin">len</span>(<span class="cm-variable">cells</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>:
        <span class="cm-keyword">return</span> []
    <span class="cm-variable">curr_gen</span> <span class="cm-operator">=</span> <span class="cm-variable">deepcopy</span>(<span class="cm-variable">cells</span>)
    <span class="cm-variable">next_gen</span> <span class="cm-operator">=</span> <span class="cm-variable">deepcopy</span>(<span class="cm-variable">cells</span>)
    <span class="cm-keyword">for</span> <span class="cm-variable">_</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">0</span>, <span class="cm-variable">generations</span>):
        <span class="cm-variable">next_gen</span> <span class="cm-operator">=</span> <span class="cm-variable">grow</span>(<span class="cm-variable">next_gen</span>, <span class="cm-number">1</span>) 
        <span class="cm-variable">curr_gen</span> <span class="cm-operator">=</span> <span class="cm-variable">deepcopy</span>(<span class="cm-variable">next_gen</span>) 
        <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">0</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">curr_gen</span>)):
            <span class="cm-keyword">for</span> <span class="cm-variable">y</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">0</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">curr_gen</span>[<span class="cm-variable">x</span>])):
                    <span class="cm-variable">count</span> <span class="cm-operator">=</span> <span class="cm-variable">count_neighbours</span>(<span class="cm-variable">curr_gen</span>, <span class="cm-variable">x</span>, <span class="cm-variable">y</span>)
                    <span class="cm-keyword">if</span> <span class="cm-variable">curr_gen</span>[<span class="cm-variable">x</span>][<span class="cm-variable">y</span>] <span class="cm-operator">==</span> <span class="cm-number">1</span>: <span class="cm-comment"># Alive</span>
                        <span class="cm-keyword">if</span> <span class="cm-variable">count</span> <span class="cm-operator">&lt;</span> <span class="cm-number">2</span> <span class="cm-keyword">or</span> <span class="cm-variable">count</span> <span class="cm-operator">&gt;</span> <span class="cm-number">3</span>:
                            <span class="cm-variable">next_gen</span>[<span class="cm-variable">x</span>][<span class="cm-variable">y</span>] <span class="cm-operator">=</span> <span class="cm-number">0</span> <span class="cm-comment"># Dies</span>
                    <span class="cm-keyword">elif</span> <span class="cm-variable">count</span> <span class="cm-operator">==</span> <span class="cm-number">3</span>: <span class="cm-comment"># Dead </span>
                        <span class="cm-variable">next_gen</span>[<span class="cm-variable">x</span>][<span class="cm-variable">y</span>] <span class="cm-operator">=</span> <span class="cm-number">1</span> <span class="cm-comment"># Revives              </span>
        <span class="cm-variable">next_gen</span> <span class="cm-operator">=</span> <span class="cm-variable">trim</span>(<span class="cm-variable">next_gen</span>)
    <span class="cm-keyword">return</span> <span class="cm-variable">next_gen</span>

<span class="cm-keyword">def</span> <span class="cm-def">grow</span>(<span class="cm-variable">arr</span>, <span class="cm-variable">n</span>):
    <span class="cm-variable">row</span> <span class="cm-operator">=</span> <span class="cm-builtin">len</span>(<span class="cm-variable">arr</span>) <span class="cm-operator">+</span> <span class="cm-number">2</span><span class="cm-operator">&ast;</span><span class="cm-variable">n</span>
    <span class="cm-variable">col</span> <span class="cm-operator">=</span> <span class="cm-builtin">len</span>(<span class="cm-variable">arr</span>[<span class="cm-number">0</span>]) <span class="cm-operator">+</span> <span class="cm-number">2</span><span class="cm-operator">&ast;</span><span class="cm-variable">n</span>
    <span class="cm-variable">res</span> <span class="cm-operator">=</span> [[<span class="cm-number">0</span> <span class="cm-keyword">for</span> <span class="cm-variable">_</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">col</span>)] <span class="cm-keyword">for</span> <span class="cm-variable">_</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">row</span>)]
    <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">n</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">res</span>) <span class="cm-operator">-</span> <span class="cm-variable">n</span>):
        <span class="cm-keyword">for</span> <span class="cm-variable">y</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">n</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">res</span>[<span class="cm-number">0</span>]) <span class="cm-operator">-</span> <span class="cm-variable">n</span>):
            <span class="cm-variable">res</span>[<span class="cm-variable">x</span>][<span class="cm-variable">y</span>] <span class="cm-operator">=</span> <span class="cm-variable">arr</span>[<span class="cm-variable">x</span><span class="cm-operator">-</span><span class="cm-variable">n</span>][<span class="cm-variable">y</span><span class="cm-operator">-</span><span class="cm-variable">n</span>]
    <span class="cm-keyword">return</span> <span class="cm-variable">res</span>
    
<span class="cm-keyword">def</span> <span class="cm-def">trim</span>(<span class="cm-variable">arr</span>):
    <span class="cm-variable">minRow</span>, <span class="cm-variable">minCol</span>, <span class="cm-variable">maxRow</span>, <span class="cm-variable">maxCol</span> <span class="cm-operator">=</span> <span class="cm-variable">sys</span>.<span class="cm-property">maxsize</span>, <span class="cm-variable">sys</span>.<span class="cm-property">maxsize</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span>
    <span class="cm-keyword">for</span> <span class="cm-variable">row</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">0</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">arr</span>)):
        <span class="cm-keyword">for</span> <span class="cm-variable">col</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">0</span>, <span class="cm-builtin">len</span>(<span class="cm-variable">arr</span>[<span class="cm-number">0</span>])):
            <span class="cm-keyword">if</span> <span class="cm-variable">arr</span>[<span class="cm-variable">row</span>][<span class="cm-variable">col</span>] <span class="cm-operator">==</span> <span class="cm-number">1</span>:
                <span class="cm-keyword">if</span> <span class="cm-variable">row</span> <span class="cm-operator">&lt;</span> <span class="cm-variable">minRow</span>: 
                    <span class="cm-variable">minRow</span> <span class="cm-operator">=</span> <span class="cm-variable">row</span>
                <span class="cm-keyword">if</span> <span class="cm-variable">row</span> <span class="cm-operator">&gt;</span> <span class="cm-variable">maxRow</span>:
                    <span class="cm-variable">maxRow</span> <span class="cm-operator">=</span> <span class="cm-variable">row</span>
                <span class="cm-keyword">if</span> <span class="cm-variable">col</span> <span class="cm-operator">&lt;</span> <span class="cm-variable">minCol</span>:
                    <span class="cm-variable">minCol</span> <span class="cm-operator">=</span> <span class="cm-variable">col</span>
                <span class="cm-keyword">if</span> <span class="cm-variable">col</span> <span class="cm-operator">&gt;</span> <span class="cm-variable">maxCol</span>:
                    <span class="cm-variable">maxCol</span> <span class="cm-operator">=</span> <span class="cm-variable">col</span>
    <span class="cm-keyword">return</span> [[<span class="cm-variable">arr</span>[<span class="cm-variable">row</span>][<span class="cm-variable">col</span>] <span class="cm-keyword">for</span> <span class="cm-variable">col</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">minCol</span>, <span class="cm-variable">maxCol</span><span class="cm-operator">+</span><span class="cm-number">1</span>)] <span class="cm-keyword">for</span> <span class="cm-variable">row</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">minRow</span>, <span class="cm-variable">maxRow</span><span class="cm-operator">+</span><span class="cm-number">1</span>)]

<span class="cm-keyword">def</span> <span class="cm-def">count_neighbours</span>(<span class="cm-variable">cells</span>, <span class="cm-variable">x</span>, <span class="cm-variable">y</span>):
    <span class="cm-builtin">sum</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
    <span class="cm-keyword">for</span> <span class="cm-variable">i</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-operator">-</span><span class="cm-number">1</span>, <span class="cm-number">2</span>):
        <span class="cm-keyword">for</span> <span class="cm-variable">j</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-operator">-</span><span class="cm-number">1</span>, <span class="cm-number">2</span>):
            <span class="cm-keyword">if</span> <span class="cm-number">0</span> <span class="cm-operator">&lt;=</span> <span class="cm-variable">x</span><span class="cm-operator">+</span><span class="cm-variable">i</span> <span class="cm-operator">&lt;</span> <span class="cm-builtin">len</span>(<span class="cm-variable">cells</span>) <span class="cm-keyword">and</span> <span class="cm-number">0</span> <span class="cm-operator">&lt;=</span> <span class="cm-variable">y</span><span class="cm-operator">+</span><span class="cm-variable">j</span> <span class="cm-operator">&lt;</span> <span class="cm-builtin">len</span>(<span class="cm-variable">cells</span>[<span class="cm-variable">x</span><span class="cm-operator">+</span><span class="cm-variable">i</span>]):
                <span class="cm-builtin">sum</span> <span class="cm-operator">+=</span> <span class="cm-variable">cells</span>[<span class="cm-variable">x</span><span class="cm-operator">+</span><span class="cm-variable">i</span>][<span class="cm-variable">y</span><span class="cm-operator">+</span><span class="cm-variable">j</span>]
    <span class="cm-keyword">return</span> <span class="cm-builtin">sum</span> <span class="cm-operator">-</span> <span class="cm-variable">cells</span>[<span class="cm-variable">x</span>][<span class="cm-variable">y</span>]</code></pre></details>