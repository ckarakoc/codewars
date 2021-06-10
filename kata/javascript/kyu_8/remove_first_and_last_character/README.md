# [Remove First and Last Character](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/javascript)
## Description
<div><p>It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.  You don't have to worry with strings with less than two characters.</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">removeChar</span>(<span class="cm-def">str</span>){
  <span class="cm-keyword">return</span> <span class="cm-variable-2">str</span>.<span class="cm-property">slice</span>(<span class="cm-number">1</span>, <span class="cm-variable-2">str</span>.<span class="cm-property">length</span><span class="cm-operator">-</span><span class="cm-number">1</span>)
};</code></pre></details>