# [Money, Money, Money](https://www.codewars.com/kata/563f037412e5ada593000114/train/javascript)
## Description
<div><p>Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.</p>
<p>The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year the new sum is re-invested.</p>
<p>Note to Tax: not the invested principal is taxed, but only the year's accrued interest</p>
<p>Example:</p>
<pre><code>  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00


After 1st Year --&gt;
  P = 1041.00
After 2nd Year --&gt;
  P = 1083.86
After 3rd Year --&gt;
  P = 1128.30
</code></pre>
<p>Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.</p>
<p>Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.  </p>
<p>Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideration that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.</p>
</div>
<details><summary>Solution</summary><pre><code><span class="cm-keyword">function</span> <span class="cm-def">calculateYears</span>(<span class="cm-def">principal</span>, <span class="cm-def">interest</span>, <span class="cm-def">tax</span>, <span class="cm-def">desired</span>) {
  <span class="cm-keyword">for</span> (<span class="cm-variable">years</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>;<span class="cm-variable-2">principal</span> <span class="cm-operator">&lt;</span> <span class="cm-variable-2">desired</span>; <span class="cm-variable">years</span><span class="cm-operator">++</span>)
    <span class="cm-variable-2">principal</span> <span class="cm-operator">+=</span> <span class="cm-variable-2">principal</span> <span class="cm-operator">*</span> <span class="cm-variable-2">interest</span> <span class="cm-operator">*</span> (<span class="cm-number">1</span><span class="cm-operator">-</span><span class="cm-variable-2">tax</span>);
  <span class="cm-keyword">return</span> <span class="cm-variable">years;</span>
}</code></pre></details>