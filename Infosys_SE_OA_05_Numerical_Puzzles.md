# 🔢 SECTION 5 — NUMERICAL PUZZLES (Infosys SE OA Level)
### 18 questions • Target time: 25 minutes

The reported Infosys "Numerical Puzzle" block uses **figures, grids, wheels, stars and number matrices** with **one hidden arithmetic rule**. In the real OA you get **4 questions in 10 minutes** — so the skill being tested is **pattern recognition speed**, not calculation. The recurring rules are: opposite-sector logic, row/column operations, sum-of-corners, and square/cube patterns.

---

### Q1. Find the missing number in the matrix.

| 5 | 7 | 24 |
|---|---|---|
| 4 | 9 | 26 |
| 6 | 3 | **?** |

A) 16  B) 18  C) 20  D) 22

✅ **Answer: B) 18**

**Step by step:**
1. Test the **row-wise** operations on row 1: 5 and 7 → 24.
   - 5 + 7 = 12 (not 24) → but 12 × 2 = 24 ✔
2. Check the rule on row 2: (4 + 9) × 2 = 13 × 2 = **26** ✔ Rule confirmed: **(1st + 2nd) × 2 = 3rd**.
3. Apply to row 3: (6 + 3) × 2 = 9 × 2 = **18**.

> 🧠 **MEMORY TRICK — "Test your rule on TWO rows before using it"**
> Never trust a rule that fits only one row (here 5 + 7 + 12 also "works" if you invent a wrong rule). **Confirm on row 2, then apply to row 3.**
> **Rule-hunting order for any matrix:**
> 1. Third column from first two (**+  then ×**)
> 2. Row sums equal
> 3. Column operations
> 4. Diagonal operations
> **Memory line: "Two rows confirm, the third one answers."**

---

### Q2. Find the missing number.

| 2 | 3 | 8 |
|---|---|---|
| 4 | 5 | 24 |
| 6 | 7 | **?** |

A) 40  B) 42  C) 48  D) 56

✅ **Answer: C) 48**

**Step by step:**
1. Row 1: 2 × 3 = 6, and the third number is 8 = 6 + 2 → the "extra 2" equals the **first** number.
2. So the rule is: **3rd = (1st × 2nd) + 1st = 1st × (2nd + 1)**.
3. Check row 2: 4 × (5 + 1) = 4 × 6 = **24** ✔
4. Apply to row 3: 6 × (7 + 1) = 6 × 8 = **48**.

> 🧠 **MEMORY TRICK — "a × b + a = a(b + 1)"**
> When you see a small extra amount added to a product, check whether that extra is the **first number**, the **second number**, or their **sum/difference**.
> **Fast factorised form:** `a × b + a` = **a × (b + 1)**. Computing 6 × 8 is far quicker than 6 × 7 + 6.
> **Memory line: "Always factorise before you multiply."**

---

### Q3. In each triangle, the centre number follows the same rule. Find the missing centre.

```
 Triangle 1        Triangle 2        Triangle 3
     3                 6                 8
    / \               / \               / \
   4---5             7---9             5---5
  centre = 6        centre = 11       centre = ?
```

A) 8  B) 9  C) 10  D) 12

✅ **Answer: B) 9**

**Step by step:**
1. Triangle 1 corners: 3, 4, 5 → sum = 12; centre = 6 = 12 ÷ **2**.
2. Triangle 2 corners: 6, 7, 9 → sum = 22; centre = 11 = 22 ÷ **2** ✔ Rule confirmed: **centre = (sum of the three corners) ÷ 2**.
3. Triangle 3 corners: 8, 5, 5 → sum = 18 → centre = 18 ÷ 2 = **9**.

> 🧠 **MEMORY TRICK — "Figures: add the outside, then look at the ratio to the inside"**
> For **any** figure puzzle (triangle, square, star, cross, wheel):
> **Step 1: add all the outer numbers. Step 2: compare the sum with the centre → is it ×1, ÷2, ×2, −10?**
> Step 2 is instant: if the centre is about **half** the sum, the rule is ÷2; if it is exactly the sum minus a small number, the rule is a subtraction.
> **Memory line: "Outside first, then find the bridge."**

---

### Q4. In the 8-sector circular wheel below, the numbers in sectors that are **directly opposite** each other follow the same rule. Find the missing value.

```
            3
         ?      4
      24          5
         15    6
            8
```

(Reading clockwise from the top: 3, 4, 5, 6, 8, 15, 24, ?)

A) 30  B) 32  C) 35  D) 36

✅ **Answer: C) 35**

**Step by step:**
1. In an 8-sector wheel, the sector **directly opposite** a given sector is **4 positions away**.
2. Pair up the numbers that face each other:
   - 3 (top) ↔ 8 (bottom) → 3² − 1 = 8 ✔
   - 4 ↔ 15 → 4² − 1 = 15 ✔
   - 5 ↔ 24 → 5² − 1 = 24 ✔
3. So the rule is **opposite = n² − 1**.
4. The number opposite 6 = 6² − 1 = 36 − 1 = **35**.

> 🧠 **MEMORY TRICK — "In a wheel, opposite = half-a-turn away"**
> - **8 sectors** → opposite is **4 steps** away
> - **6 sectors** → opposite is **3 steps** away
> - **12 sectors** → opposite is **6 steps** away
> **General rule: opposite = (total sectors ÷ 2) steps apart.**
> Then test the three "cheap" relationships on the pairs you already have: **+constant, ×constant, or a power (n² ± 1, n³ ± 1)**. Here the jump 3 → 8 is very close to 3² = 9, which gives away the square rule in 3 seconds.
> **Memory line: "Half-turn pair, then power test."**

---

### Q5. The digits of the number **627045138** are written into a 3 × 3 grid in **snake form**: fill the first row from left to right, then the second row from right to left, then the third row from left to right again. Which digit lands in the **centre cell** of the grid?

A) 0  B) 4  C) 5  D) 2

✅ **Answer: B) 4**

**Step by step:**
1. Digits in order: **6, 2, 7, 0, 4, 5, 1, 3, 8**.
2. Row 1 (left → right): cells (1,1) = 6, (1,2) = 2, (1,3) = 7.
3. Row 2 (right → left): cells (2,3) = 0, (2,2) = 4, (2,1) = 5.
4. Row 3 (left → right): cells (3,1) = 1, (3,2) = 3, (3,3) = 8.
5. The grid becomes:
   ```
   6  2  7
   5  4  0
   1  3  8
   ```
6. Centre cell (2,2) = **4**.

> 🧠 **MEMORY TRICK — "Snake = alternate the direction, count straight through"**
> The trick is to remember that **the digit order never changes — only the direction in which you place them changes**. So number the cells in the snake path (1 → 9) and match them with the digits in the original order.
> **Fast position rule for a 3 × 3 snake:** cell 5 (the centre) always receives the **5th digit** of the number. In this question, the 5th digit of 627045138 is **4** ✔ — you can answer in 5 seconds without drawing the grid.
> **Memory line: "Centre gets the middle digit."**

---

### Q6. In the addition pyramid below, every number is the sum of the two numbers directly below it. Find the missing number.

```
          23
       11    12
     7    ?    8
```

A) 3  B) 4  C) 5  D) 6

✅ **Answer: B) 4**

**Step by step:**
1. Rule: **a number = the sum of the two numbers immediately below it**.
2. From the left: 7 + ? = 11 → ? = **4**.
3. Verify from the right: ? + 8 = 12 → 4 + 8 = 12 ✔
4. Verify the top: 11 + 12 = **23** ✔ All three rows agree.

> 🧠 **MEMORY TRICK — "Pyramid: solve the lowest row first, and verify from both sides"**
> In an addition pyramid, **every missing number can be found from its row directly by subtraction**:
> **missing = above − known neighbour.**
> Here 11 − 7 = 4 (and 12 − 8 = 4 confirms it).
> **Memory line: "Subtract downwards, add upwards."** Always verify with the second neighbour — if the two answers differ, you have misread the figure.

---

### Q7. If A = 1, B = 2, C = 3 … Z = 26 and the value of a word is the sum of the values of its letters, what is the value of the word **JAVA**?

A) 30  B) 32  C) 34  D) 36

✅ **Answer: C) 34**

**Step by step:**
1. Letter values: **J = 10, A = 1, V = 22, A = 1**.
2. Sum = 10 + 1 + 22 + 1 = **34**.

> 🧠 **MEMORY TRICK — "EJOTY is your ladder"**
> Memorise **E = 5, J = 10, O = 15, T = 20, Y = 25**. Any other letter is only 1–4 steps from the nearest anchor:
> - V → Y = 25, so count back 3 → V = **22** ✔
> - P → O = 15, so count forward 1 → P = **16** ✔
> **Reverse coding (letters numbered backwards): Z = 1, Y = 2, …** → **reverse value = 27 − normal value** (V = 27 − 22 = 5).
> Read the question carefully: if it says **A = 26, B = 25**, it is asking for the reverse table.
> **Memory line: "EJOTY forward, 27 minus for reverse."**

---

### Q8. If 2 = 9, 3 = 28, 4 = 65 and 5 = 126, what is the value of 6?

A) 196  B) 216  C) 217  D) 226

✅ **Answer: C) 217**

**Step by step:**
1. Write the pattern with cubes in mind:
   - 2³ = 8 → +1 = **9** ✔
   - 3³ = 27 → +1 = **28** ✔
   - 4³ = 64 → +1 = **65** ✔
   - 5³ = 125 → +1 = **126** ✔
2. Rule confirmed: **n → n³ + 1**.
3. So 6 → 6³ + 1 = 216 + 1 = **217**.

> 🧠 **MEMORY TRICK — "If the numbers sit just above n³, the rule is n³ + 1"**
> Recognition table for "single number → single number" puzzles:
> | Pattern | Rule |
> |---|---|
> | 2→9, 3→28, 4→65, 5→126 | **n³ + 1** (always 1 above the cube) |
> | 2→8, 3→27, 4→64 | **n³** |
> | 2→5, 3→10, 4→17, 5→26 | **n² + 1** |
> | 2→6, 3→12, 4→20, 5→30 | **n(n+1)** (consecutive product) |
> **Memory line: "Cube-plus-one is the most common Infosys rule — check cubes FIRST."**
> Mental cubes to have ready: **2³=8, 3³=27, 4³=64, 5³=125, 6³=216, 7³=343.**

---

### Q9. 5 : 30 :: 7 : ?

A) 42  B) 48  C) 56  D) 63

✅ **Answer: C) 56**

**Step by step:**
1. Relationship on the left: 5 × 6 = **30** → the multiplier is **one more than the number** → n × (n + 1).
2. Apply to 7: 7 × 8 = **56**.

> 🧠 **MEMORY TRICK — "Product of neighbours"**
> Whenever the second value is roughly **6 × the first**, test **n(n+1)** before anything else.
> - 5 → 30 (5 × 6) | 6 → 42 (6 × 7) | 7 → 56 (7 × 8) | 8 → 72 (8 × 9)
> **Trap check:** the option 63 = 7 × 9 (using the *previous* multiplier 8+1 wrongly) and 42 = 6 × 7 (using the *wrong base*). Both are planted. **Always recompute with the NEW number, not by adding a fixed difference.**
> **Memory line: "Two neighbours multiplied."**

---

### Q10. In the figure below, the four numbers outside the centre follow the same rule in every figure. Find the missing number.

```
             2
             |
    6 ----- 13 ----- 8
             |
             ?
```

A) 8  B) 9  C) 10  D) 11

✅ **Answer: C) 10**

**Step by step:**
1. Add the three known outer numbers: 2 + 6 + 8 = **16**.
2. Compare with the centre: 13 × 2 = **26**, and 26 − 16 = 10 → so the missing outer number is 10.
3. **Rule:** centre = (sum of all four outer numbers) ÷ 2 → 13 = (2 + 6 + 8 + 10)/2 = 26/2 = 13 ✔

> 🧠 **MEMORY TRICK — "Add the outside, then halve — the most common centre rule"**
> The single most repeated rule in all centre-figure puzzles is **centre = (sum of the outer numbers) ÷ 2**. Its cousins:
> - **centre = sum − 10 / sum of digits**
> - **centre = product of two outer numbers ÷ the third**
> **Fast method:** multiply the centre by 2 → you get the **total of all outer numbers**. Here 13 × 2 = 26 → 26 − 16 = **10** in one line.
> **Memory line: "Double the middle, subtract the known."**

---

### Q11. Which of the following pairs does **not** belong to the group?

A) 2 : 8  B) 3 : 27  C) 4 : 64  D) 5 : 100

✅ **Answer: D) 5 : 100**

**Step by step:**
1. Test the pattern in the first three pairs: 2 → 2³ = **8** ✔, 3 → 3³ = **27** ✔, 4 → 4³ = **64** ✔.
2. So the group rule is **n : n³**.
3. Check the last pair: 5³ = **125**, not 100 → **5 : 100 breaks the rule** (100 = 10², a square, not a cube).

> 🧠 **MEMORY TRICK — "Majority rules, then verify the odd one"**
> In odd-one-out questions do **not** check every option against every possible rule. Instead:
> 1. **Find the rule that fits 3 of the 4 options** (here three pairs are perfect cubes).
> 2. **Verify only the remaining option.**
> **Memory line: "Three agree, one is the odd one."**
> **Squares to 20:** 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400.
> **Cubes to 7:** 8, 27, 64, 125, 216, 343. **100 is a square, 125 is a cube — Infosys swaps these two deliberately.**

---

### Q12. How many squares of all sizes are there in the 3 × 3 grid shown below?

```
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
```

A) 9  B) 10  C) 13  D) 14

✅ **Answer: D) 14**

**Step by step:**
1. **1 × 1 squares** = 3 rows × 3 columns = **9**.
2. **2 × 2 squares** = they can start at 2 horizontal positions × 2 vertical positions = **4**.
3. **3 × 3 squares** = the whole grid itself = **1**.
4. Total = 9 + 4 + 1 = **14**.

> 🧠 **MEMORY TRICK — "Count by size, not by eye"**
> For an **n × n grid**, the number of squares is
> **n² + (n−1)² + (n−2)² + … + 1²**
> - 2 × 2 grid → 4 + 1 = **5**
> - 3 × 3 grid → 9 + 4 + 1 = **14**
> - 4 × 4 grid → 16 + 9 + 4 + 1 = **30**
> **Memory line: "Squares inside squares: 1, 5, 14, 30."**
> (For **rectangles** in an n × m grid the formula is different: **[n(n+1)/2] × [m(m+1)/2]** — for 3 × 3 that gives 36 rectangles.)

---

### Q13. If 3 × 4 = 19 and 5 × 6 = 41, then 7 × 8 = ?

A) 56  B) 65  C) 71  D) 87

✅ **Answer: C) 71**

**Step by step:**
1. Try the natural extension of multiplication:
   - 3 × 4 = 12 → given answer 19 → extra = 19 − 12 = **7** = (3 + 4) ✔
   - 5 × 6 = 30 → given answer 41 → extra = 41 − 30 = **11** = (5 + 6) ✔
2. So the rule is: **a × b → (a × b) + (a + b)**.
3. Apply: 7 × 8 = 56 → 56 + (7 + 8) = 56 + 15 = **71**.

**Factorised shortcut:** a × b + a + b = **(a + 1)(b + 1) − 1**. Check: (7 + 1)(8 + 1) − 1 = 72 − 1 = **71** ✔

> 🧠 **MEMORY TRICK — "Custom operator: do the real operation, then measure the gap"**
> For every "fake arithmetic" puzzle (`3 × 4 = 19`), the method is fixed:
> **1) Compute the REAL operation → 2) subtract it from the given answer → 3) the gap reveals the hidden extra.**
> Here the gaps were 7 and 11, which are exactly the **sums** of the two numbers — pattern found in 10 seconds.
> **Cousin rules that also appear:** `a × b + a` (gap = a) and `a × b + b` (gap = b). Read the gap carefully.
> **Memory line: "Real result first, then measure the gap."**

---

### Q14. If 5 + 3 = 28, 9 + 1 = 810 and 8 + 6 = 214, then 7 + 3 = ?

A) 410  B) 104  C) 47  D) 40

✅ **Answer: A) 410**

**Step by step:**
1. Look at 5 + 3 = **28** → the digits "2" and "8". Note: 5 − 3 = **2** and 5 + 3 = **8**. So the answer is **the difference followed by the sum**, written side by side.
2. Verify on the second: 9 + 1 → 9 − 1 = **8**, 9 + 1 = **10** → "8" + "10" = **810** ✔
3. Verify on the third: 8 + 6 → 8 − 6 = **2**, 8 + 6 = **14** → "2" + "14" = **214** ✔ Rule confirmed.
4. Apply to 7 + 3: 7 − 3 = **4**, 7 + 3 = **10** → **"4" + "10" = 410**.

> 🧠 **MEMORY TRICK — "Two parts = difference and sum, joined as text"**
> Any answer that is **longer than a normal sum** (28, 810, 214) is a **concatenation of two results**, not one number. Split it:
> - 28 → 2 | 8 → these are (a − b) and (a + b)
> - 810 → 8 | 10 → 9 − 1 and 9 + 1
> **The "joined" rule is the most common fake-operator format in Infosys puzzles.**
> ⚠️ **Careful:** "4" + "10" is **410**, not 4 + 10 = 14 — the answer is a *string*, not a sum. Candidates who answer 14 or 40 lose the mark.
> **Memory line: "Difference then sum, side by side — never add them."**

---

### Q15. At what time between 4 o'clock and 5 o'clock will the hour hand and the minute hand of a clock **coincide**?

A) 4 : 20 minutes  B) 4 : 21 9/11 minutes  C) 4 : 22 minutes  D) 4 : 24 6/11 minutes

✅ **Answer: B) 4 : 21 9/11 minutes**

**Step by step:**
1. At exactly 4 o'clock the **hour hand is at 4 × 30 = 120°** and the minute hand is at 0° → the gap is **120°**.
2. The minute hand moves at **6°/minute** and the hour hand at **0.5°/minute** → the gap closes at a **relative speed of 5.5° per minute**.
3. Time to close 120° = 120 ÷ 5.5 = **240/11 minutes** = **21 9/11 minutes** (≈ 21 min 49 s).
4. So the hands coincide at **4 : 21 9/11** (approximately 4:21:49).

**Formula check:** the hands coincide at **60H/11** minutes past H o'clock → 60 × 4/11 = 240/11 ✔

> 🧠 **MEMORY TRICK — "Divide the hour angle by 5.5"**
> Three clock facts to keep forever:
> | Question | Formula |
> |---|---|
> | Hands **coincide** at H o'clock | **60H/11** minutes past H |
> | Hands at **right angles** at H o'clock | **(30H ± 90)/5.5** minutes (two answers) |
> | Hands **opposite** at H o'clock | **(30H ± 180)/5.5** minutes |
> **Where does 5.5 come from?** 6 − 0.5 = the relative speed. **Memory line: "The minute hand gains 5½ degrees every minute."**
> **Quick sanity check:** the answer must be a little **more than H × 5** minutes (here > 20) and **less than 60** — that alone eliminates two options.

---

### Q16. A bottle and its cork together cost ₹110. The bottle costs ₹100 more than the cork. What is the cost of the cork?

A) ₹5  B) ₹10  C) ₹15  D) ₹20

✅ **Answer: A) ₹5**

**Step by step:**
1. Let the cork cost **c**. Then the bottle costs **c + 100**.
2. Total: c + (c + 100) = 110 → 2c = 10 → c = **₹5**.
3. **Verify:** cork ₹5, bottle ₹105 → total = ₹110 ✔ and the bottle is exactly ₹100 more than the cork ✔

> 🧠 **MEMORY TRICK — "'More than' must be re-checked after solving"**
> The reflex answer is ₹10 (110 − 100), but that gives bottle ₹10 + ₹100 = ₹110 **plus** cork ₹10 = ₹120 ≠ ₹110 → wrong.
> **The one-line check that never fails: after finding both values, ADD them and see if they match the total.** If they don't, you used the difference instead of the sum.
> **Memory line: "Two unknowns → two tests: the total AND the difference."**

---

### Q17. The sum of two numbers is 30 and their product is 216. What is the difference between the two numbers?

A) 4  B) 6  C) 8  D) 9

✅ **Answer: B) 6**

**Step by step:**
1. Let the numbers be x and y: x + y = 30 and xy = 216.
2. Use the identity: **(x − y)² = (x + y)² − 4xy**.
3. (x − y)² = 30² − 4 × 216 = 900 − 864 = **36**.
4. x − y = √36 = **6**.

**Verification:** the numbers are 18 and 12 → 18 + 12 = 30 ✔ and 18 × 12 = 216 ✔ → difference = 6 ✔

> 🧠 **MEMORY TRICK — "The Sum-Difference-Product triangle"**
> Three identities that appear in both puzzles and quant:
> - **(x + y)² = x² + y² + 2xy**
> - **(x − y)² = x² + y² − 2xy**
> - **(x − y)² = (x + y)² − 4xy** ← the star of this question
> **Memory line: "Sum squared minus four times the product = difference squared."**
> **Bonus speed trick:** if the numbers are close in value, guess the pair from the product first — 216 = 18 × 12 and 18 + 12 = 30 → answer instantly.

---

### Q18. In a group of 100 students, 60 play cricket, 45 play football and 25 play both games. How many students play neither of the two games?

A) 10  B) 15  C) 20  D) 25

✅ **Answer: C) 20**

**Step by step:**
1. Use the overlapping-sets formula: **n(C ∪ F) = n(C) + n(F) − n(C ∩ F)**.
2. n(C ∪ F) = 60 + 45 − 25 = **80** → 80 students play at least one game.
3. Neither = 100 − 80 = **20**.

**Venn-diagram check:** Cricket only = 60 − 25 = 35; Football only = 45 − 25 = 20; both = 25 → total = 35 + 20 + 25 = 80 → neither = **20** ✔

> 🧠 **MEMORY TRICK — "Add both, subtract the common, then subtract from the total"**
> The 3-step template for every two-set question:
> **1) Add the two group sizes → 2) subtract the overlap (it was counted twice) → 3) subtract from the total to get the "neither" group.**
> **Memory line: "Double-counted once, so subtract it once."**
> With **three** sets the same idea becomes: **|A∪B∪C| = ΣA − Σ(pairwise overlaps) + (all three)**.

---

## 📌 Section 5 — Numerical Puzzle Pattern Bank (recognise in 10 seconds)

| Figure / data shape | The rule Infosys almost always uses |
|---|---|
| 3 × 3 number matrix | (col1 + col2) × k = col3, or col1 × (col2 + 1) = col3 |
| Circular wheel (8 sectors) | Opposite = n² ± 1, n³ ± 1, or 2n + k |
| Triangle (3 corners + centre) | centre = sum of corners ÷ 2 (or × k) |
| Cross / plus figure | centre = sum of the 4 arms ÷ 2 |
| Addition pyramid | each term = sum of the two below; solve the lowest row by subtraction |
| Snake grid | the *digit order* never changes, only the direction — the centre gets the middle digit |
| n = 9, 28, 65, 126 | n³ + 1 |
| 5 : 30 :: 7 : ? | n × (n + 1) |
| 5 + 3 = 28, 9 + 1 = 810 | difference and sum, joined as text |
| Box of squares | n² + (n−1)² + … + 1² → 14 for a 3 × 3 grid |
| Clock angle / coincidence | relative speed 5.5°/min; coincide at 60H/11 minutes |
| Bottle & cork style | solve with two unknowns, then verify the total AND the difference |

**⚠️ Time discipline for this section:** give each puzzle a hard **60 seconds**. If the rule has not clicked, mark your best guess (no negative marking has been reported for SE) and move on. Losing 4 minutes on one wheel puzzle costs you three easier marks elsewhere.

**➡️ Next file: `Infosys_SE_OA_06_English_Grammar.md`**




