# [Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e/train/javascript)
## Description
<div><p>Trolls are attacking your comment section!</p>
<p>A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.</p>
<p>Your task is to write a function that takes a string and return a new string with all vowels removed.</p>
<p>For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".</p>
<p>Note: for this kata <code>y</code> isn't considered a vowel.</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">disemvowel</span>(<span class="cm-def">str</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">str</span>.<span class="cm-property">replace</span>(<span class="cm-string-2">/[aeiou]/gi</span>, <span class="cm-string">''</span>);
}</code></pre></details>