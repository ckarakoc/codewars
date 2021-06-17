# [Extract the domain name from a URL](https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python)
## Description
<div><p>Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:</p>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">domain_name</span>(<span class="cm-string">"http://github.com/carbonfive/raygun"</span>) <span class="cm-operator">==</span> <span class="cm-string">"github"</span> 
<span class="cm-variable">domain_name</span>(<span class="cm-string">"http://www.zombie-bites.com"</span>) <span class="cm-operator">==</span> <span class="cm-string">"zombie-bites"</span>
<span class="cm-variable">domain_name</span>(<span class="cm-string">"https://www.cnet.com"</span>) <span class="cm-operator">==</span> <span class="cm-string">"cnet"</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">domain_name</span>(<span class="cm-string">"http://github.com/carbonfive/raygun"</span>) <span class="cm-operator">==</span> <span class="cm-string">"github"</span> 
<span class="cm-variable">domain_name</span>(<span class="cm-string">"http://www.zombie-bites.com"</span>) <span class="cm-operator">==</span> <span class="cm-string">"zombie-bites"</span>
<span class="cm-variable">domain_name</span>(<span class="cm-string">"https://www.cnet.com"</span>) <span class="cm-operator">==</span> <span class="cm-string">"cnet"</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">domainName</span>(<span class="cm-string">"http://github.com/carbonfive/raygun"</span>) <span class="cm-operator">==</span> <span class="cm-string">"github"</span> 
<span class="cm-variable">domainName</span>(<span class="cm-string">"http://www.zombie-bites.com"</span>) <span class="cm-operator">==</span> <span class="cm-string">"zombie-bites"</span>
<span class="cm-variable">domainName</span>(<span class="cm-string">"https://www.cnet.com"</span>) <span class="cm-operator">==</span> <span class="cm-string">"cnet"</span>
</code></pre>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">import</span> <span class="cm-variable">re</span>
<span class="cm-keyword">def</span> <span class="cm-def">domain_name</span>(<span class="cm-variable">url</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">re</span>.<span class="cm-property">sub</span>(<span class="cm-string">'https?://|www\.'</span>, <span class="cm-string">''</span>, <span class="cm-variable">url</span>).<span class="cm-property">split</span>(<span class="cm-string">'.'</span>, <span class="cm-number">1</span>)[<span class="cm-number">0</span>]</code></pre></details>