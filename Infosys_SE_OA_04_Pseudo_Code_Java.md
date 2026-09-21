# 💻 SECTION 4 — PSEUDO CODE / PROGRAMMING LOGIC (Infosys SE OA Level, Java style)
### 23 questions • Target time: 20 minutes for the real 5-question section

The real Infosys pseudo code block gives **5 questions in 10 minutes** and asks **output prediction, error finding, complexity and small OOP logic** — never full coding. Everything below is written in **Java-style** syntax (the style Infosys itself uses in the exam). For every question you get a **line-by-line trace**, because the only reliable method is a dry run.

**The 3 golden rules before you start:**
1. **Integer division truncates in Java**: `7 / 2 = 3`, `-7 / 2 = -3`. Never assume decimals.
2. **A loop's final value matters**: questions often ask the value *after* the loop ends, not inside it.
3. **Trace on paper in 3 columns: variable | value | loop count.**

---

### Q1. What will be the output of the following pseudo code?

```java
Integer n, sum
Set n = 1234
Set sum = 0
While (n > 0)
    sum = sum + (n mod 10)
    n = n / 10
End While
Print sum
```

A) 6  B) 8  C) 10  D) 12

✅ **Answer: C) 10**

**Line-by-line trace:**

| Line | What happens | n | sum |
|---|---|---|---|
| `n = 1234` | initial value | 1234 | 0 |
| `sum = sum + (n mod 10)` | `1234 mod 10 = 4` → sum = 0 + 4 | 1234 | **4** |
| `n = n / 10` | integer division → 1234/10 = 123 | **123** | 4 |
| 2nd pass | `123 mod 10 = 3` → sum = 4 + 3 = 7 | 123 | **7** |
| `n = n / 10` | 123/10 = 12 | **12** | 7 |
| 3rd pass | `12 mod 10 = 2` → sum = 7 + 2 = 9 | 12 | **9** |
| `n = n / 10` | 12/10 = 1 | **1** | 9 |
| 4th pass | `1 mod 10 = 1` → sum = 9 + 1 = **10** | 1 | **10** |
| `n = n / 10` | 1/10 = **0** (integer division!) | **0** | 10 |
| `While (n > 0)` | 0 > 0 is **false** → loop exits | 0 | 10 |

**Output: 10** — the program computes the **sum of the digits** of 1234 (1+2+3+4).

> 🧠 **MEMORY TRICK — "mod 10 gives the last digit, / 10 removes it"**
> This two-line pair is the universal **digit-extraction** engine:
> - **`n mod 10` → the LAST digit**
> - **`n / 10` → the number WITHOUT its last digit**
> Any question with these two lines is doing one of: **digit sum, digit count, reverse, palindrome check, Armstrong check**. Recognise the pattern and you can often answer without tracing. **Memory line: "Mod takes the tail, divide cuts the tail."**

---

### Q2. What will be printed?

```java
Integer num, rev
Set num = 45
Set rev = 0
While (num > 0)
    rev = rev * 10 + num mod 10
    num = num / 10
End While
Print rev
```

A) 45  B) 54  C) 9  D) 450

✅ **Answer: B) 54**

**Line-by-line trace:**

| Pass | `num mod 10` | `rev = rev*10 + digit` | `num = num/10` |
|---|---|---|---|
| 1 | 45 mod 10 = **5** | 0 × 10 + 5 = **5** | 4 |
| 2 | 4 mod 10 = **4** | 5 × 10 + 4 = **54** | 0 → loop ends |

**Output: 54** — the number is **reversed**.

> 🧠 **MEMORY TRICK — "rev = rev × 10 + digit is the REVERSE builder"**
> The moment you see **`rev * 10 + digit`**, the answer is the **reverse of the input**. Nothing else is needed:
> - 45 → **54** | 123 → 321 | 1200 → 21 (the leading zero disappears because 0 contributes nothing).
> **Cousin pattern:** if the code instead builds `sum = sum * 10 + digit` without a `rev`, it is the same thing. And if it builds a **second number and compares** it to the original, the question is a **palindrome check**.

---

### Q3. What will be the value of `count` after execution?

```java
Integer i, j, count
Set count = 0
For (i = 1; i <= 4; i = i + 1)
    For (j = i; j <= 4; j = j + 1)
        count = count + 1
    End For
End For
Print count
```

A) 8  B) 10  C) 12  D) 16

✅ **Answer: B) 10**

**Line-by-line trace (only the inner loop's run count matters):**

| Outer `i` | Inner loop `j` runs | Runs added |
|---|---|---|
| 1 | j = 1, 2, 3, 4 | **4** |
| 2 | j = 2, 3, 4 | **3** |
| 3 | j = 3, 4 | **2** |
| 4 | j = 4 | **1** |
| **Total** | | **4 + 3 + 2 + 1 = 10** |

**Output: 10**

> 🧠 **MEMORY TRICK — "Inner loop starts at i → triangle numbers"**
> When the inner loop is written **`j = i to n`**, the count is **1 + 2 + 3 + … + n = n(n+1)/2** — a **triangle number**.
> Here n = 4 → 4 × 5/2 = **10** ✔ (No tracing needed at all!)
> Compare with the other two shapes:
> - `j = 1 to n` inside `i = 1 to n` → **n × n** (square)
> - `j = i to n` inside `i = 1 to n` → **n(n+1)/2** (triangle)
> **Memory line: "Square if both start at 1, triangle if the inner starts at i."**

---

### Q4. What will be printed?

```java
Integer i, s
Set s = 0
For (i = 1; i <= 20; i = i + 1)
    If (i mod 4 == 0)
        s = s + i
    End If
End For
Print s
```

A) 40  B) 50  C) 60  D) 70

✅ **Answer: C) 60**

**Line-by-line trace (the `If` filters which values enter the sum):**

| `i` | `i mod 4 == 0`? | `s` |
|---|---|---|
| 1, 2, 3 | false | 0 |
| **4** | true | 0 + 4 = **4** |
| 5, 6, 7 | false | 4 |
| **8** | true | 4 + 8 = **12** |
| 9, 10, 11 | false | 12 |
| **12** | true | 12 + 12 = **24** |
| 13–15 | false | 24 |
| **16** | true | 24 + 16 = **40** |
| 17–19 | false | 40 |
| **20** | true | 40 + 20 = **60** |

**Output: 60** → 4 + 8 + 12 + 16 + 20.

**Fast method:** multiples of 4 up to 20 = 4, 8, 12, 16, 20 → sum = 4 × (1 + 2 + 3 + 4 + 5) = 4 × 15 = **60**.

> 🧠 **MEMORY TRICK — "Factor out the multiple"**
> For "sum of multiples of k up to n": **sum = k × (1 + 2 + … + m)** where m = n/k.
> Here k = 4, m = 5 → 4 × 15 = 60 ✔
> **For big n use the formula: sum = k × m(m+1)/2** (e.g. multiples of 3 up to 300 → 3 × 100 × 101/2 = 15150).
> **Memory line: "Take k out, add 1 to m, halve it."**

---

### Q5. What will be printed?

```java
Integer a, b, res
Set a = 3
Set b = 4
Set res = 0
While (b > 0)
    res = res + a
    b = b - 1
End While
Print res
```

A) 7  B) 10  C) 12  D) 16

✅ **Answer: C) 12**

**Line-by-line trace:**

| Pass | Before | `res = res + a` | `b = b - 1` | After |
|---|---|---|---|---|
| 1 | res = 0, b = 4 | res = 0 + 3 = **3** | b = 3 | res = 3 |
| 2 | res = 3, b = 3 | res = 3 + 3 = **6** | b = 2 | res = 6 |
| 3 | res = 6, b = 2 | res = 6 + 3 = **9** | b = 1 | res = 9 |
| 4 | res = 9, b = 1 | res = 9 + 3 = **12** | b = 0 | res = 12 |
| — | b = 0 → `0 > 0` false | loop stops | — | **12** |

**Output: 12** → the program performs **3 × 4 by repeated addition** (`a` added `b` times).

> 🧠 **MEMORY TRICK — "Add the same number b times = a × b"**
> This is the classic **multiplication-by-addition** loop. The answer is simply **a × b** — here 3 × 4 = 12.
> **General pattern table for loop-based arithmetic (memorise, it appears constantly):**
> | Code shape | It computes |
> |---|---|
> | `res = res + a` repeated b times | **a × b** |
> | `res = res * a` repeated b times | **aᵇ** (power) |
> | `res = res + i` from 1 to n | **n(n+1)/2** (sum) |
> | `fact = fact * i` from 1 to n | **n!** (factorial) |
> **Memory line: "+ is times, × is power, i is triangle, fact is factorial."**

---

### Q6. What will be printed?

```java
Integer arr[5] = {2, 4, 6, 8, 10}
Integer i, total
Set total = 0
For (i = 0; i < 5; i = i + 1)
    total = total + arr[i] * i
End For
Print total
```

A) 60  B) 70  C) 80  D) 90

✅ **Answer: C) 80**

**Line-by-line trace (careful: array index starts at 0, and each element is multiplied by its index):**

| `i` | `arr[i]` | `arr[i] * i` | `total` |
|---|---|---|---|
| 0 | 2 | 2 × 0 = **0** | **0** |
| 1 | 4 | 4 × 1 = **4** | **4** |
| 2 | 6 | 6 × 2 = **12** | **16** |
| 3 | 8 | 8 × 3 = **24** | **40** |
| 4 | 10 | 10 × 4 = **40** | **80** |
| 5 | loop condition `5 < 5` false | — | **80** |

**Output: 80**

> 🧠 **MEMORY TRICK — "Index starts at ZERO, so the first element contributes nothing"**
> Two facts that decide almost every array question:
> 1. **`i = 0` is the first element**, and `i < 5` (not `i <= 5`) touches exactly 5 elements.
> 2. If the code multiplies by `i`, the **0th element contributes 0** (that is where candidates over-count).
> **"Sum of first n numbers" check:** if the code were `total + arr[i]` (without × i) the answer would be 2+4+6+8+10 = 30 — an option Infosys often includes as the trap.
> **Memory line: "Zero index = zero contribution."**

---

### Q7. What will be printed?

```java
Integer arr[6] = {14, 7, 22, 9, 22, 3}
Integer i, c
Set c = 0
For (i = 0; i < 6; i = i + 1)
    If (arr[i] mod 2 == 0)
        c = c + 1
    End If
End For
Print c
```

A) 2  B) 3  C) 4  D) 6

✅ **Answer: B) 3**

**Line-by-line trace:**

| `i` | `arr[i]` | `arr[i] mod 2 == 0`? | `c` |
|---|---|---|---|
| 0 | 14 | true (even) | **1** |
| 1 | 7 | false | 1 |
| 2 | 22 | true | **2** |
| 3 | 9 | false | 2 |
| 4 | 22 | true | **3** |
| 5 | 3 | false | 3 |

**Output: 3** (the even numbers are 14, 22 and 22 — the repeat 22 is counted twice).

> 🧠 **MEMORY TRICK — "Duplicate values are counted twice — the loop does not know about duplicates"**
> A counter loop counts **positions, not unique values**. Seeing 22 twice means 22 is counted twice.
> **Even/odd test: `n mod 2 == 0` → even; `n mod 2 != 0` → odd.**
> **Prime test: `n mod i == 0` inside `i = 2 to n/2` → not prime.** Watch for `i = 2 to n/2` (efficient) versus `i = 2 to n-1` (same result, slower) — Infosys asks about both.
> **Memory line: "Unique value ≠ unique position."**

---

### Q8. What will be printed?

```java
String str = "INFOSYS"
Integer i, c
Set c = 0
For (i = 0; i < length(str); i = i + 1)
    If (str[i] == 'S')
        c = c + 1
    End If
End For
Print c
```

A) 1  B) 2  C) 3  D) 0

✅ **Answer: B) 2**

**Line-by-line trace (index the string first):**

Position: `0=I, 1=N, 2=F, 3=O, 4=S, 5=Y, 6=S` → length = **7**

| `i` | `str[i]` | equals `'S'`? | `c` |
|---|---|---|---|
| 0 | I | no | 0 |
| 1 | N | no | 0 |
| 2 | F | no | 0 |
| 3 | O | no | 0 |
| 4 | **S** | **yes** | **1** |
| 5 | Y | no | 1 |
| 6 | **S** | **yes** | **2** |
| 7 | `7 < 7` false → stop | — | **2** |

**Output: 2**

> 🧠 **MEMORY TRICK — "String index runs 0 to length − 1"**
> For a string of length L, valid indices are **0 … L−1**. The final index is **L − 1**, never L (that is the *StringIndexOutOfBounds* trap).
> **Comparison of characters uses single quotes in Java (`'S'`), strings use double quotes (`"S"`).** `str[i] == 'S'` compares characters (fine); `str[i] == "S"` would be a **type error** — Infosys sometimes asks exactly that error question.
> **Memory line: "Length 7 → last index 6."**

---

### Q9. What will be printed?

```java
String s = "PROGRAM"
Integer i, count
Set count = 0
For (i = 0; i < length(s); i = i + 1)
    If (s[i] == 'A' OR s[i] == 'E' OR s[i] == 'I' OR s[i] == 'O' OR s[i] == 'U')
        count = count + 1
    End If
End For
Print count
```

A) 1  B) 2  C) 3  D) 0

✅ **Answer: B) 2**

**Line-by-line trace:**

Position: `0=P, 1=R, 2=O, 3=G, 4=R, 5=A, 6=M` → length = **7**

| `i` | `s[i]` | Is it a vowel? | `count` |
|---|---|---|---|
| 0 | P | no | 0 |
| 1 | R | no | 0 |
| 2 | **O** | **yes** | **1** |
| 3 | G | no | 1 |
| 4 | R | no | 1 |
| 5 | **A** | **yes** | **2** |
| 6 | M | no | 2 |
| 7 | `7 < 7` false → stop | — | **2** |

**Output: 2** (the vowels are O and A).

> 🧠 **MEMORY TRICK — "AEIOU = 5 checks, and U is the only one with a 'u'"**
> Vowel-check code always has 5 `OR` conditions. Two traps Infosys builds into it:
> 1. **Lowercase letters are not vowels in this code** — `'a'` (97) ≠ `'A'` (65). If the string were "program" all lowercase, the answer would be **0**.
> 2. **'Y' is not a vowel here** (some books count it — in Java-style OA questions it never is).
> **Memory line: "Capital A-E-I-O-U only; Y is not invited."**

---

### Q10. What will be printed?

```java
Function fun(Integer n)
    If (n <= 1)
        Return 1
    Else
        Return n * fun(n - 2)
    End If
End Function

Print fun(7)
```

A) 105  B) 120  C) 35  D) 720

✅ **Answer: A) 105**

**Line-by-line trace (recursion expands downwards, then multiplies upwards):**

| Call | Condition `n <= 1`? | Returns |
|---|---|---|
| `fun(7)` | 7 ≤ 1 false | 7 × fun(5) |
| `fun(5)` | false | 5 × fun(3) |
| `fun(3)` | false | 3 × fun(1) |
| `fun(1)` | **1 ≤ 1 true** | **1** ← base case stops the recursion |
| Back up | — | 3 × 1 = **3** |
| Back up | — | 5 × 3 = **15** |
| Back up | — | 7 × 15 = **105** |

**Output: 105** (this is the product of all odd numbers from 7 down to 1 → 7 × 5 × 3 × 1).

> 🧠 **MEMORY TRICK — "Base case first, then unwind upward"**
> For every recursion question:
> 1. **Find the base case** (the `if` that returns a plain number) — that is where you start writing.
> 2. Write the chain **downwards**: fun(7) = 7 × fun(5) = 7 × 5 × fun(3) = …
> 3. **Multiply as you come back up.**
> **Pattern recognition:**
> - `n * fun(n − 1)` → **factorial**
> - `n * fun(n − 2)` → **product of alternating numbers** (7 × 5 × 3 × 1 = 105)
> - `n + fun(n − 1)` → **triangle sum**
> - `fun(n − 1) + fun(n − 2)` → **Fibonacci**
> **Memory line: "−1 = factorial, −2 = alternate, two calls = Fibonacci."**

---

### Q11. What will be printed?

```java
Function add(Integer n)
    If (n == 0)
        Return 0
    Else
        Return n + add(n - 1)
    End If
End Function

Print add(10)
```

A) 45  B) 50  C) 55  D) 100

✅ **Answer: C) 55**

**Line-by-line expansion:**
1. `add(10)` = 10 + `add(9)`
2. = 10 + 9 + `add(8)`
3. = 10 + 9 + 8 + … + 1 + `add(0)`
4. `add(0)` → the base case returns **0**, so the recursion stops.
5. Total = 1 + 2 + 3 + … + 10 = **n(n+1)/2 = 10 × 11/2 = 55**.

**Output: 55**

> 🧠 **MEMORY TRICK — "Sum 1 to n: n(n+1)/2 — multiply the pair, halve it"**
> **1 to 10 → 10 × 11 = 110 → 110/2 = 55.**
> Once you spot `n + add(n−1)` you do **not** expand anything — it is always the triangle sum.
> **Fast reference: 1–10 = 55 | 1–20 = 210 | 1–50 = 1275 | 1–100 = 5050.**
> **Memory line: "First and last, add them; times the count; divide by two."** (1 + 100 = 101, count 100 → 101 × 100/2 = 5050 ✔)

---

### Q12. What will be printed?

```java
Integer a, b
Set a = 6
Set b = 3
Print (a AND b) + (a OR b)
```

A) 7  B) 8  C) 9  D) 10

✅ **Answer: C) 9**

**Line-by-line trace (convert to binary first — always):**

| | Decimal | Binary (3-bit) |
|---|---|---|
| a | 6 | 1 1 0 |
| b | 3 | 0 1 1 |

**AND (bit-by-bit; 1 only when BOTH bits are 1):**

```
  1 1 0
& 0 1 1
-------
  0 1 0   → 2
```

**OR (bit-by-bit; 1 when AT LEAST ONE bit is 1):**

```
  1 1 0
| 0 1 1
-------
  1 1 1   → 7
```

**Final step:** (a AND b) + (a OR b) = 2 + 7 = **9**.

> 🧠 **MEMORY TRICK — "AND is the strict one, OR is the generous one, XOR is the different one"**
> | Operator | Rule | Example (6, 3) |
> |---|---|---|
> | **AND (&)** | 1 only if **both** are 1 | 2 |
> | **OR (\|)** | 1 if **at least one** is 1 | 7 |
> | **XOR (^)** | 1 if bits are **different** | 5 |
> **Memory line: "AND = Both, OR = Anyone, XOR = Different."**
> **Bonus identity that makes this whole question 5 seconds long:**
> **(a AND b) + (a OR b) = a + b** — always true! So here, the answer is simply 6 + 3 = **9** ✔
> Check with another pair: a = 5, b = 3 → (1) + (7) = 8 = 5 + 3 ✔
> Another identity Infosys loves: **a XOR b XOR a = b** (XOR-ing twice cancels the value).
> **Binary bench marks to memorise: 6 = 110, 5 = 101, 3 = 011, 10 = 1010, 12 = 1100, 15 = 1111.**

---

### Q13. What will be printed?

```java
Integer x, y
Set x = 7
Set y = 2
x = x XOR y
y = x XOR y
x = x XOR y
Print x
```

A) 2  B) 7  C) 5  D) 9

✅ **Answer: A) 2**

**Line-by-line trace (XOR is written as `^`):**

| Line | Calculation | x | y |
|---|---|---|---|
| Start | — | **7** | **2** |
| `x = x ^ y` | 7 ^ 2 → 111 ^ 010 = 101 = **5** | **5** | 2 |
| `y = x ^ y` | 5 ^ 2 → 101 ^ 010 = 111 = **7** | 5 | **7** |
| `x = x ^ y` | 5 ^ 7 → 101 ^ 111 = 010 = **2** | **2** | 7 |
| `Print x` | — | **2** | 7 |

**Output: 2** — the two values have been **swapped** (x became 2 and y became 7) using only XOR, with no third variable.

> 🧠 **MEMORY TRICK — "Three XORs = a swap"**
> ```
> x = x ^ y
> y = x ^ y
> x = x ^ y      → x and y are swapped
> ```
> Two facts let you answer without tracing:
> 1. **The 3-line XOR block ALWAYS swaps the two variables** → after it, `Print x` gives the **original value of y** (here 2).
> 2. **XOR is self-cancelling: a ^ a = 0 and a ^ 0 = a.** So `a ^ b ^ a = b`.
> **Memory line: "Three XORs and they trade places."** This is the fastest question in the whole pseudo code section once you know it.

---

### Q14. What will be printed?

```java
Integer a
Set a = 5
Print (a << 1) + (a >> 1)
```

A) 10  B) 12  C) 15  D) 7

✅ **Answer: B) 12**

**Line-by-line trace:**

| Expression | Meaning | Calculation | Result |
|---|---|---|---|
| `a << 1` | shift left by 1 bit | 5 = 0101 → 1010 = **10** (same as 5 × 2) | 10 |
| `a >> 1` | shift right by 1 bit | 5 = 0101 → 0010 = **2** (same as 5 ÷ 2, integer) | 2 |
| Sum | — | 10 + 2 | **12** |

**Output: 12**

> 🧠 **MEMORY TRICK — "Left shift = ×2ⁿ, Right shift = ÷2ⁿ"**
> - `a << n` = **a × 2ⁿ** (shift left multiplies)
> - `a >> n` = **a ÷ 2ⁿ** rounded down (shift right divides)
> Check: 5 << 1 = 10 ✔ (5 × 2), 5 >> 1 = 2 ✔ (5 ÷ 2 = 2.5 → 2)
> **Memory line: "Left grows, right shrinks — move the point, not the digits."**
> Exam favourites to have ready: **1 << 4 = 16 | 3 << 2 = 12 | 16 >> 2 = 4 | 8 >> 3 = 1.**

---

### Q15. What will be printed?

```java
Integer i, s
Set s = 0
For (i = 1; i <= 10; i = i + 1)
    If (i == 6)
        break
    End If
    s = s + i
End For
Print s
```

A) 15  B) 21  C) 45  D) 55

✅ **Answer: A) 15**

**Line-by-line trace:**

| `i` | Check `i == 6`? | Action | `s` |
|---|---|---|---|
| 1 | no | s = 0 + 1 | **1** |
| 2 | no | s = 1 + 2 | **3** |
| 3 | no | s = 3 + 3 | **6** |
| 4 | no | s = 6 + 4 | **10** |
| 5 | no | s = 10 + 5 | **15** |
| **6** | **yes** | **`break` → the loop STOPS immediately** (6 is not added) | **15** |
| 7–10 | never executed | — | 15 |

**Output: 15** (1 + 2 + 3 + 4 + 5).

> 🧠 **MEMORY TRICK — "break EXITS, continue SKIPS"**
> - **`break`** → leaves the loop **entirely**; nothing after it in the loop runs again.
> - **`continue`** → skips only the **rest of the current round**; the loop continues with the next value.
> **Where Infosys hides the trap:** the value that triggers `break` is **not processed**. So `break` at `i == 6` means 6 is **never added** → 1+2+3+4+5 = **15**, not 21.
> **Memory line: "Break = out of the building. Continue = skip one room."**

---

### Q16. What will be printed?

```java
Integer i, s
Set s = 0
For (i = 1; i <= 6; i = i + 1)
    If (i mod 3 == 0)
        continue
    End If
    s = s + i
End For
Print s
```

A) 9  B) 12  C) 15  D) 18

✅ **Answer: B) 12**

**Line-by-line trace:**

| `i` | `i mod 3 == 0`? | Action | `s` |
|---|---|---|---|
| 1 | no | s = 0 + 1 | **1** |
| 2 | no | s = 1 + 2 | **3** |
| **3** | **yes** | **`continue` → skips the addition** | 3 |
| 4 | no | s = 3 + 4 | **7** |
| 5 | no | s = 7 + 5 | **12** |
| **6** | **yes** | **`continue` → skips the addition** | **12** |
| 7 | `7 <= 6` false → loop ends | — | **12** |

**Output: 12** (1 + 2 + 4 + 5, skipping both multiples of 3).

> 🧠 **MEMORY TRICK — "continue = the values that disappear"**
> With `continue`, the loop still runs its full range — only the **matching values are removed from the calculation**.
> Count backwards for speed: sum of 1–6 = 21; the skipped values are 3 and 6 → 21 − 9 = **12** ✔
> **This "total minus skipped" method is faster and safer than tracing line by line whenever several values are skipped.**
> **Memory line: "Continue = subtract the skipped ones."**

---

### Q17. What will be printed?

```java
Integer i, s
Set i = 10
Set s = 0
Do
    s = s + i
    i = i + 1
While (i < 10)
Print s
```

A) 0  B) 10  C) 11  D) Infinite loop

✅ **Answer: B) 10**

**Line-by-line trace (read the loop type carefully — it is a `Do … While`):**

| Step | Action | i | s |
|---|---|---|---|
| Before the loop | i = 10, s = 0 | 10 | 0 |
| **Do body runs FIRST (no condition checked yet!)** | s = 0 + 10 = **10** | 10 | **10** |
| | i = 10 + 1 = **11** | **11** | 10 |
| `While (i < 10)` | 11 < 10 → **false** → loop ends | 11 | **10** |

**Output: 10**

> 🧠 **MEMORY TRICK — "Do-While runs at least ONCE"**
> The three loop types behave differently when the condition is already false:
> | Loop | Runs when the condition is false from the start? |
> |---|---|
> | `while (cond)` | **0 times** (checks first) |
> | `do … while (cond)` | **exactly 1 time** (runs first, checks last) |
> | `for (…)` with a false condition | **0 times** |
> **Memory line: "Do-While is the stubborn one — it refuses to run zero times."**
> This single fact is the whole trick of this question: a `while` loop here would print **0**; the `do-while` prints **10**.

---

### Q18. What will be printed?

```java
Class Base
    Public void show()
        Print "Base"
    End void
End Class

Class Derived Inherits Base
    Public void show()
        Print "Derived"
    End void
End Class

Main:
    Base obj = new Derived()
    obj.show()
```

A) Base  B) Derived  C) BaseDerived  D) Compilation error

✅ **Answer: B) Derived**

**Line-by-line explanation:**
1. `Class Derived Inherits Base` → class **Derived is a subclass** of Base.
2. Both classes define a method `show()` with **the same signature** `show()` → this is **method overriding**.
3. `Base obj = new Derived()` → the **reference type is Base** but the **object created is of type Derived**. This is called **upcasting**, and it is legal in Java because a Derived *is a* Base.
4. `obj.show()` → Java looks at the **actual object type at run time** (Derived), not the reference type → the **Derived version** of `show()` runs.
5. Output: **Derived**.

> 🧠 **MEMORY TRICK — "Reference decides what you CAN call; object decides what RUNS"**
> Remember this one sentence and all polymorphism questions are solved:
> - **Compile time** → the compiler checks the **reference type** (Base) → is `show()` available in Base? Yes ✔
> - **Run time** → the JVM uses the **object type** (Derived) → Derived's `show()` executes.
> **Memory line: "Left side = permission, right side = performance."**
> **Related distinction to keep clear:**
> - **Overriding** = same name, same parameters, **different class (inheritance)** → run-time (dynamic) polymorphism → object decides.
> - **Overloading** = same name, **different parameters, same class** → compile-time polymorphism → reference decides.

---

### Q19. What will be printed?

```java
Class Test
    void display(Integer a)
        Print "int"
    End void

    void display(Double a)
        Print "double"
    End void
End Class

Main:
    Test t = new Test()
    t.display(5)
```

A) int  B) double  C) intdouble  D) Compilation error

✅ **Answer: A) int**

**Line-by-line explanation:**
1. `Class Test` has **two methods with the same name but different parameter types** → this is **method overloading**.
2. `t.display(5)` → the argument 5 is an **Integer literal** (no decimal point).
3. Java's rule for overload resolution: **pick the most specific matching type** → `display(Integer)` is an **exact match**, while `display(Double)` would need a widening conversion.
4. Exact match wins → **"int"** is printed.

> 🧠 **MEMORY TRICK — "5 is int, 5.0 is double — exact match wins"**
> Overload resolution order in Java: **exact match → widening → boxing → varargs**. Infosys tests the first two.
> - `display(5)` → **int** version (5 is an integer literal)
> - `display(5.0)` → **double** version (a decimal literal is a double, never a float/int)
> - `display(5.0f)` → float version if it exists
> **Memory line: "Decimal point = double. No point = int."** Also, overloaded methods are resolved **at compile time**, unlike overridden methods.

---

### Q20. What is the time complexity of the following pseudo code?

```java
For (i = 0; i < n; i = i + 1)
    For (j = 0; j < i; j = j + 1)
        Print j
    End For
End For
```

A) O(n)  B) O(n log n)  C) O(n²)  D) O(1)

✅ **Answer: C) O(n²)**

**Step by step:**
1. The outer loop runs **n times** (i = 0 to n−1).
2. The inner loop runs **i times** for each value of i: 0 + 1 + 2 + … + (n−1) = **n(n−1)/2** print operations.
3. Big-O keeps only the **highest power** and drops constants: n²/2 − n/2 → **O(n²)**.
4. So the answer is **O(n²)**.

> 🧠 **MEMORY TRICK — "Count the loops, look for halving"**
> Complexity recognition in one table:
> | Code pattern | Complexity |
> |---|---|
> | One loop running n times | **O(n)** |
> | Two nested loops (each n times) | **O(n²)** |
> | Two nested loops where the inner runs to i | **O(n²)** (triangle, still n²) |
> | Loop where i **doubles** (`i = i*2`) or **halves** (`n = n/2`) | **O(log n)** |
> | Halving loop inside an n-loop | **O(n log n)** |
> | No loop, straight-line code | **O(1)** |
> **Memory line: "Nested = multiply, halving = log, both = n log n."**
> **Guaranteed-answer list to memorise:** linear search **O(n)**, binary search **O(log n)**, bubble/insertion/selection sort **O(n²)**, merge/quick sort **O(n log n)**.

---

### Q21. What will be printed?

```java
String s = "Java"
Print s.charAt(1) + length(s)
```

A) a4  B) 101  C) 4a  D) 97

✅ **Answer: B) 101**

**Line-by-line trace:**
1. `s = "Java"` → indices: `0=J, 1=a, 2=v, 3=a` → `length(s) = 4`.
2. `s.charAt(1)` = the character **`'a'`**.
3. In Java, a **`char` has a numeric value** (its ASCII/Unicode code): `'a' = 97`, `'A' = 65`, `'0' = 48`.
4. `'a' + 4` → Java promotes the char to int → 97 + 4 = **101**.
5. So the output is the **number 101**, not the text "a4".

**If you wanted text**, you would need `s.charAt(1) + "" + length(s)` → that would print `a4`.

> 🧠 **MEMORY TRICK — "char + int = number (the ASCII code wins)"**
> Java's promotion rule: **`char` is treated as a number as soon as it meets any arithmetic operator.**
> - `'a' + 4` → **101** (number) | `'a' + "" + 4` → **a4** (text)
> - Key ASCII anchors to remember: **'A' = 65, 'a' = 97 (difference 32), '0' = 48**
> So **uppercase ↔ lowercase conversion = ±32**.
> **Memory line: "Add a quote and it stays a letter; add a number and it becomes a digit."**

---

### Q22. Class A contains methods `me()` and `see()`. Class B inherits A and overrides `see()`. Class C also inherits A and overrides `see()`. Class D inherits from **both B and C**. What problem arises because of `see()`?

A) Cohesion problem  B) Diamond problem  C) Coupling problem  D) Encapsulation problem

✅ **Answer: B) Diamond problem**

**Step by step:**
1. The inheritance structure is: **A at the top**, B and C below it, and **D at the bottom inheriting from both B and C** — the shape of a **diamond**.
2. Both B and C provide their own version of `see()`. If D inherits both, **the compiler cannot decide which `see()` D should use**.
3. This **ambiguity from multiple inheritance** is called the **Diamond Problem**.
4. In Java this is avoided because **Java does not allow multiple inheritance of classes** (only single inheritance). Multiple inheritance *is* allowed through **interfaces**, and if two interfaces declare a default method with the same name, Java forces the class to override it explicitly.

> 🧠 **MEMORY TRICK — "Diamond = A at top, two in the middle, one at the bottom"**
> Sketch it: **A → (B, C) → D**. The picture itself is a diamond, and the problem is that D gets **two different versions of the same method**.
> - **Java solution:** no multiple class inheritance; use **interfaces**.
> - **C++ solution:** explicit scope resolution (`D::B::see()`).
> **Memory line: "Two parents, one method name = a fight you must settle."**

---

### Q23. Consider these two classes:

```java
class Animal {
    protected Food seekFood() {
        return new Food();
    }
}

class Dog extends Animal {
    protected DogFood seekFood() {
        return new DogFood();
    }
}
```

(where `DogFood` is a subclass of `Food`.) Which statement is correct about the return type of `Dog.seekFood()`?

A) It is an example of a covariant return type
B) It is an example of an abstract return type
C) It is an example of a contravariant return type
D) This code will not compile

✅ **Answer: A) It is an example of a covariant return type**

**Step by step:**
1. The signature is the same — `seekFood()` with **no parameters** → this is **method overriding**, not overloading.
2. The parent returns **`Food`**; the child returns **`DogFood`**.
3. `DogFood` **extends `Food`** → the child's return type is a **subtype** (a narrower, more specific type).
4. When an overriding method returns a **more specific subtype**, that is called a **covariant return type**. Java allows it (from Java 5 onwards) and it compiles fine.
5. So the correct statement is **A**.

> 🧠 **MEMORY TRICK — "Co = narrow (same direction as the class); Contra = wider (not allowed)"**
> - **Covariant** = the child's return type is **smaller / more specific** (DogFood ⊂ Food) → **allowed**.
> - **Contravariant** = the child tries to return a **bigger / more general** type (Food where the parent returned DogFood) → **not allowed** → compile error.
> - **Parameters behave the opposite way**: the child may **widen** the parameter type (contravariant parameters) — the reverse of return types.
> **Memory line: "Return can go narrow, parameters can go wide."**

---

## 📌 Section 4 — Pseudo Code Cheat Sheet + Java Traps

### Loop idioms → what they compute instantly
| Idiom | Meaning |
|---|---|
| `n mod 10`, `n = n/10` | digit extraction (digit sum / count / reverse / palindrome / Armstrong) |
| `rev = rev*10 + digit` | reverse a number |
| `sum = sum + i` for i = 1..n | **n(n+1)/2** |
| `fact = fact * i` for i = 1..n | **n!** |
| `count = count + 1` inside `for j = i to n` | **n(n+1)/2** (triangle) |
| 3 × `XOR` lines | swap two variables |
| `a << 1` / `a >> 1` | ×2 / ÷2 |
| `i = i * 2` or `n = n / 2` | **O(log n)** loop |

### The 6 Java traps Infosys plants most often
1. **Integer division truncates** → `7/2 = 3` (not 3.5).
2. **Array/string index starts at 0** and ends at **length − 1**.
3. **`break` exits, `continue` skips** — the triggering value is not processed.
4. **`do-while` runs at least once** even if the condition is false.
5. **Overriding (object decides) vs Overloading (reference decides).**
6. **`char` + number = ASCII number** → `'a' + 4 = 101`.

### The 4 complexity answers you must know cold
| Operation | Complexity |
|---|---|
| Linear search | O(n) |
| Binary search | O(log n) |
| Bubble / insertion / selection sort | O(n²) |
| Merge sort / Quick sort (average) | O(n log n) |

**➡️ Next file: `Infosys_SE_OA_05_Numerical_Puzzles.md`**





