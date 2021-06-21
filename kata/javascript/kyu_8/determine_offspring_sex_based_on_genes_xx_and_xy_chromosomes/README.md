# [Determine offspring sex based on genes XX and XY chromosomes](https://www.codewars.com/kata/56530b444e831334c0000020/train/javascript)
## Description
<div><p>The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.</p>
<p>The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.</p>
<p>Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.</p>
<p>If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter.";
If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">chromosomeCheck</span>(<span class="cm-def">sperm</span>) {
  <span class="cm-keyword">if</span> (<span class="cm-variable-2">sperm</span>.<span class="cm-property">endsWith</span>(<span class="cm-string">'Y'</span>))
    <span class="cm-keyword">return</span> <span class="cm-string">"Congratulations! You're going to have a son."</span>;
  <span class="cm-keyword">return</span> <span class="cm-string">"Congratulations! You're going to have a daughter."</span>;
}</code></pre></details>