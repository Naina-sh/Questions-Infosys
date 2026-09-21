# 🧩 SECTION 1 — REASONING ABILITY (Infosys SE OA Level)
### 19 questions • Target time: 25 minutes for the real 15-question section

Reasoning is the section Infosys weights most heavily for SE, and it is **not** random: almost every question is one of eight patterns — series, coding-decoding, blood relations, direction sense, syllogism, seating, data sufficiency, and ranking. This set drills all eight. Attempt with a timer, then read the full explanation even where you were right.

---

### Q1. What should come in place of the question mark?
**5, 11, 9, 15, 13, 19, ?**

A) 17  B) 16  C) 21  D) 15

✅ **Answer: A) 17**

**Step by step:**
1. Find the differences: 11−5 = **+6**, 9−11 = **−2**, 15−9 = **+6**, 13−15 = **−2**, 19−13 = **+6**.
2. So the series is alternating: **+6, −2, +6, −2, +6, …**
3. The next difference must be **−2** → 19 − 2 = **17**.

> 🧠 **MEMORY TRICK — "Alternating Sign Test"**
> The moment differences look like *big, small, big, small*, split the series into **two separate series**:
> Odd positions: 5, 9, 13, 17 (+4 each) — Even positions: 11, 15, 19 (+4 each).
> The answer is the next odd-position term. **Two-lane trick: if differences alternate, read every 2nd term and the pattern jumps out instantly.**

---

### Q2. Find the next term: 2, 6, 12, 20, 30, ?

A) 40  B) 42  C) 44  D) 36

✅ **Answer: B) 42**

**Step by step:**
1. Differences: 6−2 = 4, 12−6 = 6, 20−12 = 8, 30−20 = 10.
2. The differences themselves are **4, 6, 8, 10, …** → increasing by 2 each time → next difference = 12.
3. 30 + 12 = **42**.

**Cross-check (the fast way):** 2 = 1×2, 6 = 2×3, 12 = 3×4, 20 = 4×5, 30 = 5×6 → next = 6×7 = **42**. ✔

> 🧠 **MEMORY TRICK — "n(n+1) Product Pattern"**
> 2, 6, 12, 20, 30, 42, 56 → these are **1×2, 2×3, 3×4, 4×5, 5×6, 6×7, 7×8**. If a series grows by 4, 6, 8, 10 you don't even need to add — recognise it as the **product of consecutive numbers** and answer instantly.

---

### Q3. In a certain code language, FRIEND is written as HTKGPF. How is CANDLE written in the same code?

A) ECPFNG  B) ECPGNF  C) DBPFNG  D) ECPFMG

✅ **Answer: A) ECPFNG**

**Step by step:**
1. Compare FRIEND → HTKGPF letter by letter.
   - F → H (+2)  |  R → T (+2)  |  I → K (+2)
   - E → G (+2)  |  N → P (+2)  |  D → F (+2)
2. The rule is: **every letter moves forward by 2 places** in the alphabet.
3. Now apply it to CANDLE:
   - C (+2) → **E**
   - A (+2) → **C**
   - N (+2) → **P**
   - D (+2) → **F**
   - L (+2) → **N**
   - E (+2) → **G**
4. Result = **ECPFNG**.

> 🧠 **MEMORY TRICK — "EJOTY +2 Clock"**
> Remember **E = 5, J = 10, O = 15, T = 20, Y = 25** (jump of 5). To shift any letter forward/backward, locate the nearest EJOTY letter and step from it — much faster and less error-prone than reciting A-B-C. Also remember: shifting **forward wraps around** (Z + 2 = B, Y + 3 = B).

---

### Q4. If the word CAT is coded as 24, then how will DOG be coded using the same rule?

A) 24  B) 25  C) 26  D) 27

✅ **Answer: C) 26**

**Step by step:**
1. Use the alphabet positions: **C = 3, A = 1, T = 20**.
2. Sum = 3 + 1 + 20 = **24** ✔ (matches the given code, so the rule is "sum of letter positions").
3. DOG: **D = 4, O = 15, G = 7** → 4 + 15 + 7 = **26**.

> 🧠 **MEMORY TRICK — "Reverse-pair table"**
> Learn the mirror pairs once: **A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N**.
> Any mirrored pair adds to **27**. So a letter outside the EJOTY anchors can be found fast: *position of F = 27 − position of U(21) = 6*.

---

### Q5. Pointing to a photograph, Ravi said, "She is the daughter of the only son of my grandfather." How is the girl related to Ravi?

A) Cousin  B) Sister  C) Niece  D) Daughter

✅ **Answer: B) Sister**

**Step by step:**
1. "My grandfather's **only son**" → the grandfather has just one son, and that son must be **Ravi's father** (since Ravi exists as a grandson through him).
2. "Daughter of my father" → the girl is the **daughter of Ravi's father**.
3. Ravi is also a child of the same father → the girl is Ravi's **sister**.

> 🧠 **MEMORY TRICK — "Only Son = Me or My Father"**
> Whenever you see **"the only son of my mother"**, it means **me** (if you are male). **"The only son of my grandfather"** means **my father** (or my father's brother, but "only" removes the brother).
> Rule of thumb: **climb up generation by generation, then climb down**. Grandfather → his only son (father) → his daughter = **sister**. Do not jump steps; jumping is what creates the "cousin/niece" trap options.

---

### Q6. Introducing a woman, Shashank said, "She is the mother of the only daughter of my son." How is the woman related to Shashank?

A) Daughter  B) Sister-in-law  C) Daughter-in-law  D) Wife

✅ **Answer: C) Daughter-in-law**

**Step by step:**
1. "My son's only daughter" → Shashank's **granddaughter**.
2. The mother of that granddaughter is Shashank's son's **wife**.
3. Son's wife, from Shashank's point of view = **daughter-in-law**.

> 🧠 **MEMORY TRICK — "Build the chain, then read the last link"**
> Write the chain as arrows: **Shashank → son → (son's wife = mother of his child)**. A "mother of my son's child" is *always* my son's wife → **daughter-in-law**. In blood-relation questions, 90% of the answer lies in the **last two words** of the sentence. Underline them first.

---

### Q7. A man walks 5 km towards the North, then turns right and walks 3 km, then turns right again and walks 5 km. How far is he now from his starting point?

A) 3 km  B) 5 km  C) 8 km  D) 13 km

✅ **Answer: A) 3 km**

**Step by step:**
1. Start at point O. Walk **5 km North** → point A.
2. Turn right. Facing North, right = **East** → walk 3 km East → point B.
3. Turn right. Facing East, right = **South** → walk 5 km South → point C.
4. The 5 km North cancels the 5 km South, so C is exactly **3 km East** of O.
5. Distance from start = **3 km**.

> 🧠 **MEMORY TRICK — "Cancel Opposite Legs"**
> In direction questions, if two movements are **equal and opposite** (5 N and 5 S), they cancel completely — you do not need Pythagoras.
> **Direction compass mantra:** N → right = E → right = S → right = W → right = N (clockwise ring). Just repeat the ring in your head: **N-E-S-W**. For left turns, go **N-W-S-E**.

---

### Q8. One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. Which direction was Suresh facing?

A) North  B) South  C) East  D) West

✅ **Answer: B) South**

**Step by step:**
1. It is morning → the sun is in the **East** → **every shadow falls towards the West**.
2. The pole's shadow fell to Suresh's **right** → Suresh's right-hand side = **West**.
3. Now ask: "If my right hand points West, which way am I facing?"
   - Facing North → right hand = **East** ✗
   - Facing South → right hand = **West** ✔
4. So Suresh was facing **South**.

> 🧠 **MEMORY TRICK — "Shadow is always opposite the sun"**
> Sun East → shadow West (morning). Sun West → shadow East (evening).
> **Then use the "right-hand map":** Facing North → right = East; Facing South → right = West; Facing East → right = South; Facing West → right = North.
> **Memory line: "N-Right-East, S-Right-West"** (rhymes: *Nor-th = East on right; Sou-th = West on right*).
> ⚠️ This question is deliberately the classic trap: candidates answer "North" by reflex. Always **place the shadow direction, then find the facing**.

---

### Q9. Statements: All pens are books. No book is a pencil.
**Conclusions:**
I. No pen is a pencil.
II. Some pencils are pens.

A) Only I follows  B) Only II follows  C) Both follow  D) Neither follows

✅ **Answer: A) Only I follows**

**Step by step (Venn diagram logic):**
1. "All pens are books" → the pen circle sits completely **inside** the book circle.
2. "No book is a pencil" → the book circle and pencil circle are **completely separate** (no overlap at all).
3. Since pens live inside books, and books never touch pencils → **pens can never be pencils**. Conclusion I is **true**.
4. Conclusion II claims some pencils are pens. A pencil is not even a book, so it certainly cannot be a pen → **false**.
5. Only **I** follows.

> 🧠 **MEMORY TRICK — "Draw first, decide later"**
> Never solve syllogism in your head. Draw circles:
> - "All A are B" → A inside B.
> - "No A is B" → two separate circles.
> - "Some A are B" → two circles that overlap a little.
> Then check the conclusion by **looking at the picture**. If the conclusion is *possible but not certain* → it does NOT follow. **"Some" must be visible in the diagram, otherwise it fails.**

---

### Q10. Statements: All roses are flowers. Some flowers fade quickly.
**Conclusions:**
I. Some roses fade quickly.
II. Some flowers that fade quickly are roses.

A) Only I follows  B) Only II follows  C) Both follow  D) Neither follows

✅ **Answer: D) Neither follows**

**Step by step:**
1. "All roses are flowers" → the rose circle is inside the flower circle.
2. "Some flowers fade quickly" → **some part** of the flower circle overlaps the "fade quickly" circle. But that overlapping part may be the part **outside** roses.
3. Conclusion I says some roses (a specific sub-part of flowers) fade quickly. The overlap given does not touch the rose part → **not certain** → does not follow.
4. Conclusion II says the same thing in reverse words → also not certain → does not follow.
5. Neither follows.

> 🧠 **MEMORY TRICK — "The 'Some' Circle Must Touch"**
> For any conclusion containing **some / at least a few**, put your pencil on the circle mentioned in the conclusion. If the **given overlap does not physically touch that circle**, the conclusion fails.
> Quick elimination rule for the OA: **"Some A are B" from "All C are A" + "Some A are B" is ALWAYS invalid** — that pair is the most common Infosys trick. Only if the statement says *"Some flowers ARE roses"* can you conclude anything about roses.

---

### Q11. Five friends A, B, C, D and E sit in a row facing North.
- C sits exactly in the middle.
- A is not adjacent to C.
- B sits at the extreme left end.
- D sits immediately to the right of C.

Who sits at the extreme right end?

A) A  B) E  C) D  D) C

✅ **Answer: A) A**

**Step by step:**
1. Draw five seats facing North: `_ _ _ _ _` (positions 1 to 5, position 1 = extreme left).
2. "C is exactly in the middle" of 5 seats → **C = position 3**.
3. "D sits immediately to the right of C" → **D = position 4**.
4. "B is at the extreme left" → **B = position 1**.
5. "A is not adjacent to C" → A cannot be at 2 or 4. Positions left are 2 and 5, and 2 is now free but adjacent to C → so **A = position 5**, and **E = position 2**.
6. Final row: **B, E, C, D, A** → extreme right end = **A**.

> 🧠 **MEMORY TRICK — "Fix the Middle First"**
> In any row-seating puzzle, if a clue mentions *"middle"*, *"extreme end"* or *"third from left"*, that clue is the **anchor** — draw the row and lock it immediately. Fixed positions eliminate half the options.
> **Face-direction rule for rows:** In a row facing **North**, "right of X" = the seat on the **reader's right** (towards the East). In a row facing **South**, "right of X" = the seat on the **reader's left**. Whenever the row faces South, simply **turn your paper upside-down** in your head — all left/right answers flip.

---

**Directions for Q12–Q13:** Six friends P, Q, R, S, T and U sit around a circular table, all facing the centre.
- U sits exactly between T and P.
- P sits second to the left of T.
- S sits immediately to the left of R.
- Q is an immediate neighbour of R.

### Q12. Who sits opposite P?

A) Q  B) S  C) U  D) T

✅ **Answer: B) S**

### Q13. Who sits second to the left of R?

A) U  B) S  C) T  D) P

✅ **Answer: C) T**

**Step by step (build the circle once, answer both):**
1. Use the rule: **facing the centre → left = clockwise, right = anticlockwise.**
2. Since a circle can be rotated freely, **fix R at position 1** (say the top) and count clockwise.
3. "Q is an immediate neighbour of R" → Q is at position 2 or position 6.
4. "S sits immediately to the left of R" → left = clockwise → **S = position 2**. Since position 2 is now taken by S, **Q = position 6**.
5. Remaining persons T, U, P take positions 3, 4, 5.
6. "P sits second to the left of T": if T = 3 → second to the left = position 5 → P = 5 ✔ (and U = 4). If T = 4 → P would be at 6 (taken by Q) ✗. If T = 5 → P would be at 1 (taken by R) ✗.
7. So clockwise order = **R(1), S(2), T(3), U(4), P(5), Q(6)**.
8. Check "U is between T and P": U at 4 neighbours T at 3 and P at 5 ✔ — all clues satisfied.
9. **Q12:** position opposite P (5) = 5 + 3 = 8 → 8 − 6 = **2 = S**.
10. **Q13:** second to the left of R (1) = clockwise steps 2, 3 → **3 = T**.

> 🧠 **MEMORY TRICK — "Rotate freely, count clockwise"**
> Set one fixed clue-person at the **top (12 o'clock)** and count positions 1→6 clockwise. Then apply:
> - **Facing centre → Left = Clockwise** (remember "**C-L: Centre–Left**")
> - **Facing outside → Left = Anticlockwise**
> **Opposite seat formula:** in a circle of 6, opposite = **±3 positions**; in a circle of 8 → **±4**; general rule → **± (n/2)**.
> Never redraw the whole circle — after fixing one person, every "left/right" clue is just **+1 / +2 / +3 clockwise or anticlockwise**.

---

### Q14. **Data Sufficiency** — What is the value of the two-digit number?
**Statement I:** The sum of the digits is 9.
**Statement II:** The difference between the digits is 3.

A) I alone is sufficient  B) II alone is sufficient  C) Both together are sufficient  D) Both together are still not sufficient

✅ **Answer: D) Both together are still not sufficient**

**Step by step:**
1. From I: the two digits add to 9 → possible numbers: 18, 27, 36, 45, 54, 63, 72, 81, 90 → many values, not unique.
2. From II: the digits differ by 3 → 14, 25, 30, 36, 41, 47, 52, 58, 63, 69, 74, 85, 96 → many values.
3. Combine: digits x and y with x + y = 9 and |x − y| = 3 → digits are **6 and 3**.
4. But nothing tells us **which digit is the tens digit** → the number could be **63 or 36**.
5. Two possible answers → data is **not sufficient even after combining**.

> 🧠 **MEMORY TRICK — "Two values = Not Sufficient"**
> In data-sufficiency questions, "sufficient" means **exactly ONE unique value**. If your working produces even two possibilities, the answer is "not sufficient".
> **Also remember the DS option order — it is always the same:**
> **(1) I alone → (2) II alone → (3) Both together → (4) Neither.**
> Fast policy: read **Statement I first and try to answer using I alone**. If yes → option 1. Then try **Statement II alone**. Only if both fail, combine.

---

### Q15. **Data Sufficiency** — Is the positive integer N divisible by 6?
**Statement I:** N is divisible by 3.
**Statement II:** N is divisible by 4.

A) I alone is sufficient  B) II alone is sufficient  C) Both together are sufficient  D) Both together are still not sufficient

✅ **Answer: C) Both together are sufficient**

**Step by step:**
1. Statement I alone: N = 3, 6, 9, 12 … → 9 is **not** divisible by 6, 12 **is** → cannot decide.
2. Statement II alone: N = 4, 8, 12, 16 … → 8 is **not** divisible by 6, 12 **is** → cannot decide.
3. Combine: N is a multiple of both 3 and 4 → N is a multiple of **LCM(3,4) = 12**.
4. Every multiple of 12 is even and divisible by 3 → **always divisible by 6**.
5. So together they are sufficient.

> 🧠 **MEMORY TRICK — "6 = 2 × 3"**
> To prove divisibility by a composite number, prove divisibility by its **coprime factors**:
> - Divisible by **6** → need ÷2 **and** ÷3
> - Divisible by **12** → need ÷3 **and** ÷4
> - Divisible by **15** → need ÷3 **and** ÷5
> **Memory line: "Split into the coprime pair, prove both, done."**

---

### Q16. 8 : 72 :: 6 : ?

A) 48  B) 54  C) 42  D) 60

✅ **Answer: B) 54**

**Step by step:**
1. Look for the relation between 8 and 72: 8 × 9 = 72.
2. Apply the same multiplier to the third term: 6 × 9 = **54**.

> 🧠 **MEMORY TRICK — "Same Partner, Same Move"**
> In analogy questions the two sides must use the **identical operation**. Test the three cheapest operations in this order: **(i) ×k, (ii) n²/n³ ± c, (iii) n × (n+1)**.
> Here 72 = 8 × 9 → the multiplier is **one more than the base**, so 6 → 6 × 9 = 54. The option 48 (= 6 × 8) is the planted trap for people who use a *similar but wrong* multiplier.

---

### Q17. Complete the series: AZ, BY, CX, ?

A) DV  B) EW  C) DW  D) DX

✅ **Answer: C) DW**

**Step by step:**
1. First letters: **A, B, C, …** → moving forward by 1 → next = **D**.
2. Second letters: **Z, Y, X, …** → moving backward by 1 → next = **W**.
3. Combine → **DW**.

> 🧠 **MEMORY TRICK — "Read the two lanes separately"**
> A two-letter series is **two independent 1-letter series glued together**. Write them as two columns:
> `A B C D` (forward) and `Z Y X W` (backward).
> **Extra insight:** in these pairs the two letters are always **mirror pairs adding to 27** (A+Z = 27, B+Y = 27, C+X = 27, D+W = 27). Spot that and you predict both partners instantly.

---

### Q18. Study the following arrangement carefully:
**F 4 % K 9 @ R 2 W # 6 $ A 3 E 7 ! M**
Which of the following elements is **fifth to the right of the eighth element from the left**?

A) 3  B) A  C) $  D) 6

✅ **Answer: B) A**

**Step by step:**
1. Number every element from the left:
   1=F, 2=4, 3=%, 4=K, 5=9, 6=@, 7=R, **8=2**, 9=W, 10=#, 11=6, 12=$, **13=A**, 14=3, 15=E, 16=7, 17=!, 18=M.
2. Eighth element from the left = **2** (position 8).
3. Fifth to the right of position 8 → 8 + 5 = **position 13** = **A**.

> 🧠 **MEMORY TRICK — "Right = Add, Left = Subtract"**
> Never count element-by-element from the middle. Use one formula:
> **Final position = given position + (right steps)**, or **− (left steps)**.
> Here: 8 + 5 = 13 → read position 13 directly. Counting five elements one at a time costs 40 seconds and is where silly marks are lost.

---

### Q19. In a row of 40 students, A is 12th from the left end and B is 15th from the right end. How many students are there between A and B?

A) 11  B) 12  C) 13  D) 14

✅ **Answer: C) 13**

**Step by step:**
1. Convert **both** positions to the same reference (from the left).
2. B is 15th from the right in a row of 40 → B's position from the left = 40 − 15 + 1 = **26th**.
3. A is 12th from the left.
4. Students between them = 26 − 12 − 1 = **13**.

> 🧠 **MEMORY TRICK — "Convert one, subtract, minus one"**
> **Position from left = Total − Position from right + 1** (the "+1" is the classic forgotten step).
> Then **students between = difference of positions − 1**, because A and B themselves must be excluded.
> **Memory line: "One to convert, one to subtract."** Two "+1/−1" slips are the biggest source of wrong answers in this topic.

---

## 📌 Section 1 — Pattern Recap (write this on your rough sheet in the first 30 seconds)

| Pattern | Instant trigger | Time to solve |
|---|---|---|
| Number / letter series | Differences → two-lane split → squares & cubes | 20 sec |
| Coding–decoding | ±n letter shift, letter-position sums, mirror 27 | 30 sec |
| Blood relations | Build the chain generation by generation | 30 sec |
| Direction sense | N-E-S-W ring + cancel opposite legs | 30 sec |
| Syllogism | Draw circles; "some" must touch | 40 sec |
| Seating | Anchor fixed clues first (middle / end / "immediately") | 90 sec |
| Data sufficiency | Try I alone → II alone → together | 45 sec |
| Ranking | Convert one side, subtract, minus one | 20 sec |

**➡️ Next file: `Infosys_SE_OA_02_Technical_Math_Ability.md`**




