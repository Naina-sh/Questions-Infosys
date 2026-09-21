# 🧩 SECTION 3 — PUZZLE SOLVING / LOGICAL DEDUCTION (Infosys SE OA Level)
### 18 questions • Target time: 25 minutes

The reported Infosys puzzle questions are **multi-clue deduction puzzles**: floor puzzles, box stacking, scheduling, seating, ranking comparisons, clock puzzles, weighing puzzles and cube-cutting puzzles. They are not "brain teasers with a trick" — they are **solvable by writing the clues as fixed positions**. This set teaches you the exact order in which to apply clues.

---

**Directions for Q1–Q2:** Six friends A, B, C, D, E and F live on six different floors of a building. Floor 1 is the lowest and floor 6 is the highest.
- A lives on floor 1.
- C lives on an odd-numbered floor above floor 3.
- D lives immediately below C.
- E lives immediately below F.
- B does not live on floor 2.

### Q1. Who lives on the topmost floor?

A) C  B) B  C) F  D) E

✅ **Answer: B) B**

### Q2. How many people live below D?

A) 2  B) 3  C) 4  D) 1

✅ **Answer: B) 3**

**Step by step (solve the puzzle once, answer both):**
1. "C lives on an **odd-numbered floor above floor 3**" → floors above 3 are 4, 5, 6; the odd ones are **5** only → **C = floor 5**.
2. "D lives immediately below C" → **D = floor 4**.
3. "A lives on floor 1" → **A = floor 1**.
4. Floors left for B, E and F = **2, 3, 6**.
5. "E immediately below F" → E and F must be consecutive floors. Among 2, 3, 6 the only consecutive pair is (2, 3) → **E = 2, F = 3**.
6. The remaining floor 6 goes to B, and this satisfies "B is not on floor 2" ✔
7. Final arrangement (floor → person): **1 = A, 2 = E, 3 = F, 4 = D, 5 = C, 6 = B**.
8. **Q1:** topmost floor (6) = **B**.
9. **Q2:** people below D (floor 4) = floors 1, 2, 3 → **3 people**.

> 🧠 **MEMORY TRICK — "Odd/Even clues are eliminators, not answers"**
> Any clue of the type *"odd floor above 3"*, *"even-numbered house"*, *"not on floor 2"* **narrows the field to one or two places**. Apply these **first** — they kill options fastest. Then apply the *"immediately below / immediately above"* clues.
> **Also learn the standard position words:** *immediately above/below* = the very next place; *two floors between* = a gap of 3; *just above* = immediately above.
> **Memory line: "Eliminate first, place second."**

---

**Directions for Q3–Q4:** Five boxes P, Q, R, S and T are kept one above another in a stack (the topmost position is 1).
- Q is at the bottom.
- R is immediately above T.
- P is above R.
- S is not at the top.
- S is immediately below P.

### Q3. Which box is at the top?

A) P  B) S  C) R  D) T

✅ **Answer: A) P**

### Q4. Which box is immediately below S?

A) T  B) R  C) Q  D) P

✅ **Answer: B) R**

**Step by step:**
1. "Q is at the bottom" → position 5 = **Q**.
2. "R is immediately above T" → R and T form a consecutive pair. With Q at 5, the pair can be (1,2), (2,3) or (3,4).
3. Try the pair at (3,4) → R = 3, T = 4. Remaining positions 1 and 2 hold P and S. "P is above R" ✔ both work, so use the last clue: "S is immediately below P" → **P = 1, S = 2** ✔ and "S is not at the top" ✔
4. The pair at (2,3) → R = 2, T = 3, leaving positions 1 and 4 for P and S; for "S immediately below P", S = 4 and P = 1 are **not adjacent** ✗ → rejected.
5. So the only valid stack from top to bottom is **P, S, R, T, Q**.
6. **Q3:** top = **P**.
7. **Q4:** immediately below S = **R**.

> 🧠 **MEMORY TRICK — "When two answers survive, use the leftover clue as the tie-breaker"**
> Stack/floor puzzles give you **two possible patterns** if you stop early. That is intentional. Take the clue you have not used yet (here *"S is immediately below P"*) and **test it against both patterns** — one will die instantly.
> **Written format that saves time:** draw a vertical strip from top to bottom with the numbers 1–5 on the left, and write a name only when a clue *forces* it. Never guess a position; a wrong guess costs you that question and the next one too.

---

**Directions for Q5–Q6:** Eight friends A, B, C, D, E, F, G and H sit in a straight row facing North.
- A sits third from the left end.
- Only two persons sit between A and E.
- B sits second to the right of A.
- C sits at the extreme left end.
- G sits second to the left of D.
- H sits at the extreme right end.

### Q5. Who sits fourth from the right end?

A) E  B) B  C) F  D) H

✅ **Answer: B) B**

### Q6. Who sits exactly between A and B?

A) C  B) G  C) D  D) E

✅ **Answer: C) D**

**Step by step:**
1. Draw 8 seats facing North, numbered 1 (extreme left) to 8 (extreme right): `1 2 3 4 5 6 7 8`.
2. **A is third from the left** → A = position **3**.
3. **B is second to the right of A** → facing North, right = higher number → 3 + 2 = **5**. So B = position 5.
4. **Two persons between A and E** → E is 3 positions away from A → E = 3 + 3 = **6**.
5. **C is at the extreme left** → C = position **1**; **H is at the extreme right** → H = position **8**.
6. Positions left for D, F, G = **2, 4, 7**.
7. **G is second to the left of D** → D − 2 = G. Among 2, 4, 7 the only working pair is G = 2, D = 4 ✔ (if D = 7, G would be 5, already taken by B).
8. So F = position **7**, and the final row is: **C, G, A, D, B, E, F, H**.
9. **Q5:** fourth from the right → 8 − 4 + 1 = position 5 = **B**.
10. **Q6:** the seat between A (3) and B (5) = position 4 = **D**.

> 🧠 **MEMORY TRICK — "Convert 'from the right' with one formula"**
> **Position from the right = Total + 1 − Position from the left.**
> Here: 8 + 1 − 5 = 4th from the right → confirms position 5 is 4th from the right.
> **"Between two persons" is a COUNT, not a distance:** "two persons between X and Y" → the gap in positions is **3**. **Memory line: "Between + 1 = the jump."**

---

**Directions for Q7–Q8:** A, B, C, D, E and F each give a presentation on six different days of the same week, from Monday to Saturday.
- C presents on Wednesday.
- The number of persons presenting before D is the same as the number of persons presenting after F.
- B presents immediately after A.
- F does not present on Monday.

### Q7. Who presents on Tuesday?

A) D  B) E  C) F  D) A

✅ **Answer: B) E**

### Q8. On which day does F present?

A) Monday  B) Wednesday  C) Friday  D) Saturday

✅ **Answer: D) Saturday**

**Step by step:**
1. Number the working days 1 to 6: Mon = 1, Tue = 2, Wed = 3, Thu = 4, Fri = 5, Sat = 6.
2. **C = Wednesday = day 3.**
3. The clue "persons before D = persons after F" means **D + F = 7** (because D − 1 = 6 − F).
4. Possible pairs: (D, F) = (4, 3), (5, 2), (2, 5), (6, 1), (1, 6). Day 3 is taken by C, so **(4, 3) is out**. Day 1 with F on Monday is also out (given "F does not present on Monday"), so **(6, 1) is out**.
5. Remaining possibilities: (5, 2), (2, 5), (1, 6).
6. Test each with "B immediately after A":
   - (D, F) = (1, 6): D = Mon, F = Sat → free days for A, B, E are 2, 4, 5 → A = Thu (4), B = Fri (5) works, E = Tue (2) ✔ **valid**.
   - (D, F) = (2, 5): D = Tue, F = Fri → free days are 1, 4, 6 → no two consecutive days available for A and B ✗ **rejected**.
   - (D, F) = (5, 2): D = Fri, F = Tue → free days are 1, 4, 6 → again no consecutive pair ✗ **rejected**.
7. So the final schedule is: **Mon – D, Tue – E, Wed – C, Thu – A, Fri – B, Sat – F**.
8. **Q7:** Tuesday = **E**. **Q8:** F presents on **Saturday**.

> 🧠 **MEMORY TRICK — "The 'equal on both sides' clue is an equation, not a guess"**
> When a puzzle says *"the same number of people are before X as after Y"*, immediately write **X + Y = Total + 1** (here D + F = 7). It converts a wordy clue into **one arithmetic line that produces a short list of pairs** — usually 3 or 4 — and the remaining clues kill all but one.
> **Memory line: "Equal sides → add to Total + 1."**

---

**Directions for Q9–Q10:** Five friends A, B, C, D and E scored different marks in a test.
- A scored more than B but less than C.
- E scored less than C but more than A.
- D scored more than only one friend.

### Q9. Who scored the highest?

A) A  B) C  C) D  D) E

✅ **Answer: B) C**

### Q10. Who scored the lowest?

A) B  B) D  C) E  D) A

✅ **Answer: A) B**

**Step by step:**
1. "A > B but A < C" → **C > A > B**.
2. "E < C but E > A" → **C > E > A**.
3. Combine: **C > E > A > B** (B is still the lowest so far).
4. "D scored more than only one friend" → exactly one person is below D → **D is 4th and the person below him is 5th**.
5. The only person below D can be B (since C > E > A is already fixed) → **C > E > A > D > B**.
6. Check: D is above only B ✔ → order is valid.
7. **Q9:** highest = **C**. **Q10:** lowest = **B**.

> 🧠 **MEMORY TRICK — "Turn every clue into an inequality arrow"**
> Rewrite each comparison as a single arrow chain (C > A > B) and then **merge the chains** at the common person. Words like *"more than only one"* mean **"there is exactly 1 person below me"** → that person is 4th in a group of 5.
> **Position dictionary to memorise for comparison puzzles:**
> - "more than only one" → **4th**
> - "less than only two" → **3rd**
> - "more than all" → **1st**
> **Memory line: "Only-one = second from the end."**

---

### Q11. If 6 cats can catch 6 mice in 6 minutes, then how many cats are needed to catch 24 mice in 12 minutes?

A) 8  B) 12  C) 16  D) 24

✅ **Answer: B) 12**

**Step by step:**
1. Start from the given fact: **6 cats catch 6 mice in 6 minutes**.
2. Divide by 6 → **1 cat catches 1 mouse in 6 minutes** (ratio thinking: cats and mice reduce together, time stays).
3. In **12 minutes**, 1 cat can catch 12/6 = **2 mice**.
4. For 24 mice: 24 ÷ 2 = **12 cats**.

> 🧠 **MEMORY TRICK — "Work = Rate × Time; the unit rate is the key"**
> Always reduce the statement to **"1 worker → how much in how long"**, then scale up.
> **The equal-ratio sentence to remember: "Same cats → more time = more mice; more mice → more cats."**
> BEWARE the trap answer 24 cats — that is what you get if you wrongly assume "6 cats catch 6 mice in 6 minutes" means "1 cat = 1 mouse per minute". Infosys plants exactly that option.

---

### Q12. What is the angle between the hour hand and the minute hand of a clock at 3:15?

A) 0°  B) 7.5°  C) 15°  D) 30°

✅ **Answer: B) 7.5°**

**Step by step:**
1. **Minute hand** at 15 minutes = 15 × 6 = **90°** (the minute hand moves 6° per minute).
2. **Hour hand** at 3:15 → it has moved 3 hours plus 15 minutes:
   = 3 × 30 + 15 × 0.5 = 90 + **7.5** = **97.5°** (the hour hand moves 0.5° per minute).
3. Difference = 97.5 − 90 = **7.5°**.

> 🧠 **MEMORY TRICK — "6 and half"**
> - **Minute hand: ×6 degrees per minute**
> - **Hour hand: ×30 per hour + ×0.5 per extra minute**
> **Angle formula to memorise: |30H − 5.5M|** (H = hour, M = minutes).
> Check: |30 × 3 − 5.5 × 15| = |90 − 82.5| = **7.5°** ✔
> **Memory line: "Thirty H minus five-point-five M."** If the result is more than 180°, subtract it from 360°.

---

### Q13. How many times do the hands of a clock overlap (coincide) in a period of 24 hours?

A) 20  B) 22  C) 24  D) 26

✅ **Answer: B) 22**

**Step by step:**
1. The hands overlap **once every 65 5/11 minutes**, which is a little more than once per hour.
2. In 12 hours they coincide **11 times** (not 12 — the 12 o'clock overlap is shared between two cycles).
3. In 24 hours → 11 × 2 = **22 times**.

**Same family of facts:**
- Hands **opposite (in a straight line)** → **22 times** in 24 hours.
- Hands at **right angles** → **44 times** in 24 hours.

> 🧠 **MEMORY TRICK — "22 for coincide, 22 for straight, 44 for right angle"**
> Remember the pair **"11 per 12 hours"** — because the hands need 65 5/11 minutes to meet, one meeting per hour is impossible.
> **Song-style memory: "Eleven in twelve, so twenty-two in twenty-four."**

---

### Q14. A watch gains 5 seconds every 3 minutes. If it is set correctly at 8:00 AM, what time will it show at 10:00 PM on the same day?

A) 10:20:00 PM  B) 10:23:20 PM  C) 10:25:00 PM  D) 10:15:40 PM

✅ **Answer: B) 10:23:20 PM**

**Step by step:**
1. Time elapsed from 8:00 AM to 10:00 PM = **14 hours** = 14 × 60 = **840 minutes**.
2. Number of 3-minute blocks in 840 minutes = 840 ÷ 3 = **280 blocks**.
3. Total gain = 280 × 5 = **1400 seconds**.
4. Convert: 1400 ÷ 60 = 23 minutes and 20 seconds.
5. So the watch shows 10:00 PM + 23 min 20 s = **10:23:20 PM**.

> 🧠 **MEMORY TRICK — "Count the blocks, then multiply the error"**
> Three-step template for every "faulty clock" question:
> **1) Total minutes elapsed → 2) how many blocks of the given interval → 3) multiply by the error and add/subtract.**
> - "Gains" → **add** the error to the shown time.
> - "Loses" → **subtract**.
> **Memory line: "Gain means fast, lose means slow."** Also, if the question asks the **correct** time when a faulty clock shows a value, invert the operation (divide by the error factor) — do not just subtract the error, because the block count is based on the *watch's* minutes.

---

### Q15. In a certain code language:
- "nee tik" means "good boy"
- "tik toe" means "boy runs"
- "toe pa" means "runs fast"

What does "nee" mean?

A) boy  B) runs  C) good  D) fast

✅ **Answer: C) good**

**Step by step:**
1. Compare statement 1 and statement 2, which share the common word **"tik"** → the common meaning is **"boy"** → so **tik = boy**.
2. From statement 1, "nee tik" = "good boy" and tik = boy → **nee = good**.
3. Cross-check with statement 3: "toe pa" = "runs fast". From statement 2, "tik toe" = "boy runs" and tik = boy → **toe = runs** → therefore **pa = fast**.
4. Answer: **nee = good**.

> 🧠 **MEMORY TRICK — "Find the common word = find the common meaning"**
> In every substitution/language-code puzzle:
> **Two sentences sharing one word → that word means whatever the two meanings share.**
> Then **delete the known word** and the rest of the sentence decodes itself.
> **Memory line: "Common word, common meaning; then strike it out."**
> This 2-line method solves what looks like a 5-line puzzle, and it works for 3–4 sentence puzzles of the same family.

---

### Q16. Two friends, Ravi and Meena, are standing together. It is known that **exactly one** of them always lies and the other always tells the truth. Ravi says: "Both of us are liars." Which of the following is correct?

A) Ravi is truthful and Meena is the liar
B) Ravi is the liar and Meena is truthful
C) Both are liars
D) Both are truthful

✅ **Answer: B) Ravi is the liar and Meena is truthful**

**Step by step:**
1. Assume Ravi's statement is **true** → then both are liars → but if Ravi is a liar he cannot state a true sentence → **contradiction**.
2. So Ravi's statement must be **false** → Ravi is the **liar**.
3. That matches the given condition "exactly one liar".
4. Therefore **Meena tells the truth**.

> 🧠 **MEMORY TRICK — "Assume true, and see if it kills itself"**
> For every liar / truth-teller puzzle, **assume the statement is true first**. If the assumption contradicts itself (a liar telling the truth), the statement is false — done in one step.
> **Standard self-referential results to remember:**
> - "I am a liar" → **impossible** (nobody can say it and be consistent).
> - "Both of us are liars" → the speaker **must be the liar** (this question).
> - "At least one of us is a liar" → the speaker is **truthful**.
> **Memory line: "True assumption that hurts itself is a false statement."**

---

### Q17. A cube is painted red on all its faces, and then it is cut into 27 equal smaller cubes. How many of the smaller cubes have **exactly two** faces painted?

A) 6  B) 8  C) 12  D) 16

✅ **Answer: C) 12**

**Step by step:**
1. Cutting into 27 equal cubes means a **3 × 3 × 3** arrangement.
2. Small cubes with **exactly two faces painted** are those sitting at the **middle of each edge** (not corners, not centres).
3. A cube has **12 edges**, and each edge of a 3×3×3 cube has exactly **1 middle cube**.
4. So the count = 12 × 1 = **12**.

### Q18. In the same 3 × 3 × 3 cut cube, how many smaller cubes have **exactly one** face painted?

A) 4  B) 6  C) 8  D) 9

✅ **Answer: B) 6**

**Step by step:**
1. Cubes with exactly one painted face sit at the **centre of each face** (not touching any edge).
2. A cube has **6 faces**; a 3×3×3 cube has exactly **1 centre cube per face**.
3. Count = 6 × 1 = **6**.

**Full table for a 3 × 3 × 3 = 27 cube (memorise this — it is the most-asked version):**
| Type | Count | Where they sit |
|---|---|---|
| 3 faces painted | **8** | corners |
| 2 faces painted | **12** | middle of each edge |
| 1 face painted | **6** | centre of each face |
| 0 faces painted | **1** | the hidden centre |
| **Total** | **27** | ✔ |

> 🧠 **MEMORY TRICK — "8 corners, 12 edges, 6 faces, 1 heart"**
> For **n × n × n** painted cubes:
> - **3 faces** = 8 (always 8 corners, whatever n)
> - **2 faces** = **12(n − 2)**
> - **1 face** = **6(n − 2)²**
> - **0 faces** = **(n − 2)³**
> For n = 3: 8, 12, 6, 1 ✔
> **Memory line: "Corners fixed at 8; edges 12; faces 6; centre 1 — and remember to subtract 2 from n first."**

---

## 📌 Section 3 — Puzzle Attack Plan (the order in which you apply clues)

| Step | What to do |
|---|---|
| 1 | **Draw the frame first** — a floor strip (1 to 6), a row (`1 2 3 4 5 6`), a table, or a day strip. Never solve puzzles mentally. |
| 2 | **Lock the "extreme" and "middle" clues** (topmost, bottom, extreme left, exactly in the middle). |
| 3 | **Apply "immediately above/below/left/right" clues** — these create pairs with no gap. |
| 4 | **Convert count clues into equations** ("two people between", "equal number on both sides", "more than only one"). |
| 5 | **Test leftovers:** if two arrangements survive, use the unused clue to eliminate one. |
| 6 | **Answer both questions from the SAME diagram** — never rebuild for the second question. |

**Time rule:** if a puzzle is not solved in **90 seconds**, mark the two questions and move on. Puzzle sections are where SE aspirants lose the Reasoning section.

**➡️ Next file: `Infosys_SE_OA_04_Pseudo_Code_Java.md`**



