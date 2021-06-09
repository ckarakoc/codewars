# Remove First and Last Character
## Description
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.  You don't have to worry with strings with less than two characters.

<details><summary>Solution</summary>
<pre class="p-2 my-2 border overflow-x-auto" lang="python"><code><span class="cm-keyword">def</span> <span class="cm-def">remove_char</span>(<span class="cm-variable">s</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">s</span>[<span class="cm-number">1</span>:<span class="cm-operator">-</span><span class="cm-number">1</span>]</code></pre>
</details>