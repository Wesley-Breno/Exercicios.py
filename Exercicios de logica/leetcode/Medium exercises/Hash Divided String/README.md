<h1>Hash Divided String</h1>
<div class="elfjS" data-track-load="description_content"><p>You are given a string <code>s</code> of length <code>n</code> and an integer <code>k</code>, where <code>n</code> is a <strong>multiple</strong> of <code>k</code>. Your task is to hash the string <code>s</code> into a new string called <code>result</code>, which has a length of <code>n / k</code>.</p>

<p>First, divide <code>s</code> into <code>n / k</code> <strong><span data-keyword="substring-nonempty" class=" cursor-pointer relative text-dark-blue-s text-sm"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r44:"><div>substrings</div></div><div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(224px, 240px);"></div></div></div></span></strong>, each with a length of <code>k</code>. Then, initialize <code>result</code> as an <strong>empty</strong> string.</p>

<p>For each <strong>substring</strong> in order from the beginning:</p>

<ul>
	<li>The <strong>hash value</strong> of a character is the index of that character in the <strong>English alphabet</strong> (e.g., <code>'a' → 0</code>, <code>'b' → 1</code>, ..., <code>'z' → 25</code>).</li>
	<li>Calculate the <em>sum</em> of all the <strong>hash values</strong> of the characters in the substring.</li>
	<li>Find the remainder of this sum when divided by 26, which is called <code>hashedChar</code>.</li>
	<li>Identify the character in the English lowercase alphabet that corresponds to <code>hashedChar</code>.</li>
	<li>Append that character to the end of <code>result</code>.</li>
</ul>

<p>Return <code>result</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abcd", k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">"bf"</span></p>

<p><strong>Explanation:</strong></p>

<p>First substring: <code>"ab"</code>, <code>0 + 1 = 1</code>, <code>1 % 26 = 1</code>, <code>result[0] = 'b'</code>.</p>

<p>Second substring: <code>"cd"</code>, <code>2 + 3 = 5</code>, <code>5 % 26 = 5</code>, <code>result[1] = 'f'</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "mxz", k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">"i"</span></p>

<p><strong>Explanation:</strong></p>

<p>The only substring: <code>"mxz"</code>, <code>12 + 23 + 25 = 60</code>, <code>60 % 26 = 8</code>, <code>result[0] = 'i'</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>k &lt;= s.length &lt;= 1000</code></li>
	<li><code>s.length</code> is divisible by <code>k</code>.</li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
</div>