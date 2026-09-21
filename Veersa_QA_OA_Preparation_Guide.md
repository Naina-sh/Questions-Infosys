# 📘 VEERSA (A Neurealm Company) — Fresher QA OA: Complete Preparation Guide
### Built from actual candidate experiences (GeeksforGeeks 2023–2024) + official drive notice
### Written for absolute beginners — every concept explained from zero

## 📋 Test Pattern (based on real Veersa OA experiences)

| Item | Details (reported by actual candidates) |
|---|---|
| Name | CBT / "VAT" (Veersa Aptitude Test) via **Prometric** |
| Questions | ~75 MCQs (2024 report) |
| Sections | Quantitative Aptitude, OOPs/Programming, SQL (+ some JS output Qs in 2024) |
| Marking | **+4 correct / −4 wrong** (2023 report) — NEGATIVE MARKING |
| Difficulty | "Medium — not too tough" (repeated by multiple candidates) |
| Next rounds | Top scorers → direct interview; others → GD → Interview |

> ⚠️ **Golden rule because of −4 marking:** attempt a question only if you can eliminate at least 2 options. Never blind-guess.

---

# SECTION 1: QUANTITATIVE APTITUDE

## 1.1 Percentages

### From zero
"Percent" = per hundred. 25% = 25/100 = 0.25. To find 25% of 80: (25/100)×80 = 20.
Useful identity: x% of y = y% of x (25% of 80 = 80% of 25 = 20).

### Memorize these conversions
1/2=50%, 1/3=33.33%, 1/4=25%, 1/5=20%, 1/6=16.66%, 1/8=12.5%, 1/9=11.11%, 1/11=9.09%

### Shortcut: Successive change (asked CONSTANTLY at Veersa-style tests)
Increase a% then decrease b% (or reverse): **Net % = a + b + (a×b)/100** (minus sign for decrease).

**Example:** +20% then −20%: 20 + (−20) + (20×−20)/100 = **−4%** (4% DECREASE — not zero!).

**Q1.** A number is increased by 40% then decreased by 40%. Net change?
- A) 0%  B) 16% decrease  C) 16% increase  D) 8% decrease

✅ **Answer: B.** Net = 40 − 40 + (40×−40)/100 = −16%.

**Q2.** 45% of a number is 81. What is 60% of it?
- A) 96  B) 108  C) 112  D) 120

✅ **Answer: B.** Number = 81/0.45 = 180 → 60% = 108.

## 1.2 Profit & Loss

### From zero
CP = cost price, SP = selling price. Profit = SP − CP. **Profit% is ALWAYS on CP** (the #1 beginner mistake).
Profit% = (SP − CP)/CP × 100. SP = CP × (100 + profit%)/100.

### Key shortcuts
- Same % profit on one item and same % loss on another → **overall loss of r²/100 %**
- "Marked 40% up, then 40% discount" → successive change: 40 − 40 + (40×−40)/100 = **−16% loss**

**Q.** Marked 50% above cost, sold at 20% discount. Profit%?
- A) 30%  B) 25%  C) 20%  D) 15%

✅ **Answer: C.** CP=100, MP=150, SP = 150×0.8 = 120 → profit 20%.

## 1.3 Ratio & Proportion

### From zero
a:b compares quantities. Each "share" = Total ÷ (sum of ratio parts). 2:3 out of 10 → shares of 4 and 6.

**Q1.** ₹420 divided in 2:3:2. B gets?
- A) 140  B) 160  C) 180  D) 210

✅ **Answer: C.** 7 parts → 60 each → B = 3×60 = 180.

**Q2.** Incomes 3:4, expenses 2:3, each saves ₹600. Income of A?
- A) 1800  B) 2400  C) 3600  D) 3000

✅ **Answer: A.** 3x−2y=600, 4x−3y=600 → subtract: x=y → 3x−2x=600 → x=600 → A = 1800.

## 1.4 Averages

### From zero
Average = Sum ÷ Count. Think of it as the "balance point."

**Shortcut:** replacing one number x by y among n numbers changes average by (y−x)/n.

**Q1.** Average of 5 numbers is 27; removing one makes it 25. Which was removed?
- A) 30  B) 35  C) 37  D) 40

✅ **Answer: B.** Old sum 135, new sum 100 → removed 35.

**Q2.** Average age of 30 students is 14; with teacher it's 15. Teacher's age?
- A) 31  B) 45  C) 44  D) 40

✅ **Answer: B.** 31×15 − 30×14 = 465 − 420 = 45.

**Q3.** Average of first 20 natural numbers?
- A) 10  B) 10.5  C) 11  D) 9.5

✅ **Answer: B.** (n+1)/2 = 10.5.

## 1.5 Time, Speed & Distance (TSD)

### From zero
**Speed = Distance / Time.** Everything else is unit conversion + relative speed.

### Unit conversion (MEMORIZE)
- km/h → m/s: **× 5/18**
- m/s → km/h: **× 18/5**

### Relative speed
- Same direction: SUBTRACT speeds
- Opposite direction: ADD speeds
- Train crossing a **pole/man** → distance = train length only
- Train crossing a **platform/bridge/train** → distance = SUM of lengths

**Q1.** A 240 m train crosses a pole in 12 s. Speed in km/h?
- A) 60  B) 72  C) 80  D) 64

✅ **Answer: B.** 240/12 = 20 m/s → ×18/5 = **72 km/h**.

**Q2.** Same train crosses a 360 m platform in?
- A) 24  B) 30  C) 36  D) 40 (seconds)

✅ **Answer: B.** Distance = 240+360 = 600 m → 600/20 = **30 s**.

**Q3.** Trains at 60 and 90 km/h approach from 300 km apart. Meet in?
- A) 2 h  B) 2.5 h  C) 3 h  D) 3.5 h

✅ **Answer: A.** Opposite → 150 km/h → 300/150 = 2 h.

**Boats:** Downstream = boat + stream, Upstream = boat − stream.
Boat = (down+up)/2, Stream = (down−up)/2.

## 1.6 Time & Work

### From zero
If A finishes a job in n days, A does 1/n per day. Rates ADD.
Two workers formula: **Time together = a×b/(a+b)**.

**Q1.** A in 10 days, B in 15. Together?
- A) 5  B) 6  C) 7  D) 8

✅ **Answer: B.** (10×15)/(10+15) = 150/25 = 6 days.

**Q2.** A+B take 6 days; A alone 10. B alone?
- A) 12  B) 15  C) 16  D) 18

✅ **Answer: B.** 1/6 − 1/10 = 1/15 → 15 days.

**Q3.** 12 men in 20 days. 30 men take?
- A) 6  B) 8  C) 10  D) 12

✅ **Answer: B.** Work = 240 man-days → 240/30 = 8 days.

## 1.7 Number Series

### From zero — test patterns in this order:
1. Constant differences (AP)
2. Growing differences (+2,+4,+6…)
3. Multiplying (×2, ×3, ×1.5)
4. Squares/cubes ± small number
5. Fibonacci (sum of previous two)
6. Alternate-position patterns

**Q1.** 2, 6, 12, 20, 30, ?
- A) 40  B) 42  C) 44  D) 36

✅ **Answer: B.** Diffs 4,6,8,10 → next 12 → 42. (n²+n pattern.)

**Q2.** 3, 7, 16, 35, ?
- A) 74  B) 70  C) 76  D) 72

✅ **Answer: A.** ×2 then +1,+2,+3… → 35×2+4 = 74.

**Q3.** 1, 4, 27, 256, ?
- A) 3125  B) 625  C) 2401  D) 512

✅ **Answer: A.** nⁿ pattern → 5⁵ = 3125.

## 1.8 Probability (basics — enough for Veersa)

### From zero
P = favorable/total, always between 0 and 1.

**Dice (2 dice = 36 outcomes):** P(sum=7)=6/36=1/6 (most likely), P(sum=9)=4/36=1/9, P(sum≥10)=1/6.
**Cards:** 52 total, 13/suit, 4 aces, 26 red → P(ace)=1/13, P(red queen)=2/52=1/26.
**Coins — complement trick:** P(at least one head in n tosses) = 1 − (1/2)ⁿ.

**Q1.** Two dice. P(sum is 9)?
- A) 1/9  B) 1/6  C) 2/9  D) 1/12

✅ **Answer: A.** (3,6),(4,5),(5,4),(6,3) → 4/36 = 1/9.

**Q2.** 3 coins. P(at least one head)?
- A) 1/2  B) 3/8  C) 7/8  D) 1/8

✅ **Answer: C.** 1 − 1/8 = 7/8.

## 1.9 Simple & Compound Interest

- SI = P×R×T/100 (same every year)
- CI = P(1+R/100)ᵀ − P
- **2-yr CI − SI = P(R/100)²**

**Q1.** SI on ₹5000 at 8% for 3 years?
- A) 1200  B) 1000  C) 1400  D) 1250

✅ **Answer: A.** 5000×8×3/100 = ₹1200.

**Q2.** CI − SI on ₹10,000 at 10% for 2 years?
- A) 100  B) 90  C) 110  D) 200

✅ **Answer: A.** 10000×(10/100)² = ₹100.

## 1.10 Logical Reasoning quick hits

- **Blood relations:** draw a family tree, never solve in your head.
  *"She is the daughter of my grandfather's only son"* → grandfather's only son = my father → she = my **sister**.
- **Directions:** sketch always. Facing North, right 90° → East; again → South.
- **Coding-decoding:** compare letters; try ±1 shift first. MONDAY→NPOEBZ (+1 shift) ⇒ FRIDAY→**GSJEBZ**.

**Q.** "His mother is the only daughter of my mother." Sita said of a man. Sita is his?
- A) Sister  B) Mother  C) Aunt  D) Grandmother

✅ **Answer: B.** Only daughter of her mother = Sita herself → she is his **mother**.

---
---

# SECTION 2: PROGRAMMING FUNDAMENTALS & OUTPUT PREDICTION

## 2.1 Increment/Decrement operators (the #1 asked pattern)

### From zero
- `x++` (post-increment): USE the current value of x, THEN add 1
- `++x` (pre-increment): add 1 FIRST, THEN use the new value
- `x--` / `--x`: same, but subtract 1

**Rule of thumb:** the position of `++` tells you WHEN the change takes effect relative to using the value.

**Q1.**
```java
int x = 5;
int y = x++ + ++x;
System.out.println(y);
```
- A) 10  B) 11  C) 12  D) 13

✅ **Answer: C) 12.** Step-by-step: `x++` gives 5 (x becomes 6). Then `++x` makes x 7 and gives 7. y = 5 + 7 = **12**. Track x's value after every token — never skip.

**Q2.**
```java
int a = 10;
System.out.println(a++ + a++);
```
- A) 20  B) 21  C) 22  D) 23

✅ **Answer: B) 21.** First `a++` gives 10 (a→11); second gives 11 (a→12). 10 + 11 = **21**.

**Q3.**
```java
int p = 3;
int q = --p * p++;
System.out.println(q + " " + p);
```
- A) 6 3  B) 9 4  C) 6 4  D) 9 3

✅ **Answer: A) 6 3.** `--p` → p=2, gives 2. `p++` gives 2 (p→3). q = 2×2 = 6, p is 3.

## 2.2 Loops & traces

### From zero
- `for (int i=0; i<5; i++)` runs i = 0,1,2,3,4 (five times — starts at 0, stops BEFORE 5)
- `while(condition)` repeats as long as condition is true
- `break` exits the loop entirely; `continue` skips to next iteration

**Q4.**
```java
int s = 0;
for (int i = 1; i <= 4; i++) {
    if (i == 3) continue;
    s += i;
}
System.out.println(s);
```
- A) 6  B) 10  C) 7  D) 4

✅ **Answer: C) 7.** Adds 1+2, skips 3 (continue), adds 4 → 7.

**Q5.**
```java
int i = 0;
while (i < 10) {
    i += 3;
}
System.out.println(i);
```
- A) 9  B) 12  C) 10  D) infinite loop

✅ **Answer: B) 12.** i goes 3, 6, 9, 12 — 12 ≥ 10 stops. First value ≥ 10 reachable by +3 steps from 0 is 12.

**Q6.**
```java
int n = 5, f = 1;
for (int i = 1; i <= n; i++) f = f * i;
System.out.println(f);
```
- A) 15  B) 120  C) 25  D) 60

✅ **Answer: B) 120.** This is factorial: 1×2×3×4×5 = 120. Recognize classic snippets — they repeat in OAs.

## 2.3 Data types, operators, strings in Java

- Integer division truncates: `7/2 = 3` (not 3.5). `7.0/2 = 3.5`.
- `%` is remainder (modulus): `7%3 = 1`, `10%4 = 2`.
- `char` in arithmetic uses ASCII: `'A' = 65`, `'a' = 97`, `'0' = 48`.
- String comparison: `==` compares references; `.equals()` compares content.
- String is immutable — methods return NEW strings.

**Q7.** What is `System.out.println(10/3 + " " + 10%3);`?
- A) 3.33 1  B) 3 1  C) 3.33 3.33  D) 3 3

✅ **Answer: B) 3 1.** Integer division 10/3=3; remainder 10%3=1.

**Q8.**
```java
String s1 = "hello";
String s2 = new String("hello");
System.out.println(s1 == s2);
System.out.println(s1.equals(s2));
```
- A) true true  B) false true  C) true false  D) false false

✅ **Answer: B) false true.** `==` compares memory references (different objects → false); `.equals()` compares the characters → true. **Extremely common interview + MCQ question.**

**Q9.** `System.out.println('A' + 1);` prints?
- A) B  B) 66  C) A1  D) 65

✅ **Answer: B) 66.** char + int → int arithmetic on ASCII (65+1). (If it were `('A'+1)` cast to char, it would print 'B'.)

## 2.4 JavaScript output questions (reported in 2024 OA)

### From zero
- JS `+` with a string does CONCATENATION (joins text)
- JS `+` with numbers does addition — left to right!
- `typeof` returns the type as a string: `"string"`, `"number"`, `"boolean"`, `"undefined"`

**Q10.** `console.log(typeof "5" + 1 + 2);`
- A) 8  B) string3  C) string12  D) NaN

✅ **Answer: C) string12.** `typeof "5"` = "string". Then left-to-right: "string"+1 = "string1", +2 = "string12".

**Q11.** `console.log(1 + "2" + 3);`
- A) 6  B) 123  C) 15  D) NaN

✅ **Answer: B) 123.** 1+"2" → "12" (string!), "12"+3 → "123".

**Q12.** `console.log("5" - 2);`
- A) 3  B) "3"  C) "52"  D) NaN

✅ **Answer: A) 3.** There's no `-` for strings, so JS converts "5" to a number → 3. (+ concatenates, but − forces numeric.)

## 2.5 Arrays & logic snippets

**Q13.**
```java
int[] arr = {4, 8, 15, 16, 23};
int max = arr[0];
for (int i = 1; i < arr.length; i++)
    if (arr[i] > max) max = arr[i];
System.out.println(max);
```
- A) 4  B) 23  C) 16  D) error

✅ **Answer: B) 23.** Classic find-max pattern: start with first element, keep the bigger one. This exact pattern appears in Veersa interviews too.

**Q14.** What does this print for input 5?
```java
int n = 5, a = 0, b = 1;
for (int i = 0; i < n; i++) {
    System.out.print(a + " ");
    int t = a + b; a = b; b = t;
}
```
- A) 1 1 2 3 5  B) 0 1 1 2 3  C) 0 1 2 3 4  D) 1 2 3 5 8

✅ **Answer: B) 0 1 1 2 3.** Fibonacci starting from 0: each term = sum of previous two. Recognize the a,b,temp pattern — it's everywhere.

---
---

# SECTION 3: OOPs CONCEPTS (Guaranteed section in every reported Veersa CBT)

*Object-Oriented Programming from zero, in Java terminology — that's what Veersa tests.*

## 3.1 The 4 Pillars (learn verbatim)

1. **Encapsulation** — wrapping data (variables) and methods together, hiding data via `private` + getters/setters. *Ex: BankAccount with private balance changed only via deposit()/withdraw().*
2. **Abstraction** — showing only essential features, hiding implementation. *Ex: you call `car.brake()` without knowing HOW it works.*
3. **Inheritance** — a child class acquires the parent's members via `extends`. *Ex: class Dog extends Animal → Dog gets Animal's eat(). Code reuse.*
4. **Polymorphism** — "many forms": same method name behaves differently. Two types: compile-time (overloading) and runtime (overriding).

> ⚠️ "Wrapping data+methods into one unit" = **Encapsulation**. "Hiding implementation details" = **Abstraction**. Don't confuse them!

## 3.2 Overloading vs Overriding (THE most asked Veersa OOPs topic)

| | Overloading | Overriding |
|---|---|---|
| Where | Same class | Parent → child class |
| Signature | Same name, DIFFERENT parameters | Same name, SAME parameters |
| Resolved | **Compile time** | **Runtime** |
| Also called | Compile-time/static polymorphism | Runtime/dynamic polymorphism |

**Q1.** Method overloading is an example of:
- A) Runtime polymorphism  B) Compile-time polymorphism  C) Data hiding  D) Dynamic binding

✅ **Answer: B.** The compiler decides which version to call, based on arguments, at compile time.

**Q2.** Method overriding is:
- A) Compile-time polymorphism  B) Runtime polymorphism  C) Encapsulation  D) Abstraction

✅ **Answer: B.** The actual object's method runs — decided at runtime (dynamic binding).

**Q3.** `add(int a, int b)` and `add(int a, int b, int c)` in one class are:
- A) Overridden  B) Overloaded  C) Duplicated  D) Invalid

✅ **Answer: B.** Same name + different parameter lists = overloading.

## 3.3 Abstract class vs Interface

| | Abstract class | Interface |
|---|---|---|
| Methods | Abstract AND normal | Abstract (default/static allowed since Java 8) |
| Variables | Any | Only `public static final` constants |
| Constructor | Yes | **No** |
| Keyword | `extends` | `implements` |
| Multiple inheritance | No | Yes (implement many interfaces) |
| Instantiate? | No | No |

**Q4.** Which cannot be instantiated directly but can contain abstract methods?
- A) Interface only  B) Abstract class only  C) Both  D) Final class

✅ **Answer: C.**

**Q5.** Which is NOT true about interfaces?
- A) Methods are public abstract by default  B) Variables are public static final  C) Interfaces have a constructor  D) A class can implement multiple interfaces

✅ **Answer: C.** Interfaces have NO constructors. Any "interface has a constructor" option is always the false statement.

**Q6.** A class with at least one abstract method must be declared:
- A) final  B) static  C) abstract  D) private

✅ **Answer: C.** (An abstract class may also have zero abstract methods, though.)

## 3.4 Keywords you must know

- **final**:
  - final variable → constant
  - final method → **cannot be overridden** (but CAN be inherited/overloaded)
  - final class → cannot be extended (e.g., String is final)
- **static**: belongs to the CLASS, not objects. Static methods can't use `this` or access non-static members directly. Called without an object (e.g., `Math.max(2,3)`).
- **this** = current object; **super** = parent-class part.
- **Access modifiers**: private (same class only) < default (same package) < protected (+ subclasses) < public (everywhere).

**Q7.** A final method:
- A) Cannot be overloaded  B) Cannot be overridden  C) Cannot be inherited  D) Must be static

✅ **Answer: B.** final methods can be inherited and overloaded, just never overridden.

**Q8.** Which cannot be inherited?
- A) public class  B) abstract class  C) final class  D) static class member only

✅ **Answer: C.** `final class` cannot be extended at all.

**Q9.** Static methods:
- A) Access instance variables directly  B) Belong to the class, not objects  C) Can be overridden  D) Need an object to call

✅ **Answer: B.**

## 3.5 Constructors, Strings, Exceptions

- Constructor: same name as class, **no return type**, runs automatically on `new`.
- No constructor written → Java provides a default no-arg one. Write ANY constructor → the default disappears.
- Constructors can be **overloaded** but never overridden (they aren't inherited).
- **Virtual functions**: C++ keyword `virtual` enables runtime polymorphism. In Java, **all non-static, non-final, non-private methods are virtual by default**. (A Veersa interviewer asked exactly this concept — know the one-liner!)
- **String is immutable** — every "change" creates a new object (StringBuilder = mutable version).
- **finally** block always executes after try/catch — used to close files/connections.

**Q10.** Which is TRUE about constructors?
- A) Must have a return type  B) Can be overridden  C) Same name as class, no return type  D) Must be static

✅ **Answer: C.**

**Q11.** In Java, `String` is:
- A) Mutable  B) Immutable  C) A primitive type  D) An interface

✅ **Answer: B.**

**Q12.** Which block always executes in exception handling?
- A) try  B) catch  C) finally  D) throw

✅ **Answer: C.**

**Q13.** What does this print?
```java
class A { void show() { System.out.println("A"); } }
class B extends A { void show() { System.out.println("B"); } }
public class Main {
    public static void main(String[] args) {
        A obj = new B();
        obj.show();
    }
}
```
- A) A  B) B  C) Error  D) A B

✅ **Answer: B) B.** Parent reference → child object. Overriding resolves at RUNTIME using the ACTUAL object (B). This is the classic runtime-polymorphism question — memorize the reasoning, it appears in both MCQs and interviews.

---
---

# SECTION 4: SQL / DBMS (in every reported Veersa CBT + interview)

*SQL from absolute zero. In the interview you'll be asked to WRITE queries (especially joins) — practice typing them, don't just read.*

## 4.1 Basics from zero

A database stores tables. A table has rows (records) and columns (fields).
Example table `Emp`:

| id | name | dept | salary |
|----|------|------|--------|
| 1  | Asha | IT   | 50000  |
| 2  | Ravi | HR   | 40000  |
| 3  | Neha | IT   | 60000  |

Core commands:
- `SELECT name, salary FROM Emp;` — read columns
- `SELECT * FROM Emp WHERE salary > 45000;` — filter rows
- `INSERT INTO Emp VALUES (4,'Amit','IT',55000);` — add a row
- `UPDATE Emp SET salary=65000 WHERE id=3;` — modify
- `DELETE FROM Emp WHERE id=2;` — remove rows
- `SELECT DISTINCT dept FROM Emp;` — unique values only
- `ORDER BY salary DESC` — sort (DESC = highest first, ASC = lowest first)

**Q1.** Which clause filters ROWS before grouping?
- A) HAVING  B) WHERE  C) GROUP BY  D) ORDER BY

✅ **Answer: B.** WHERE filters individual rows; HAVING filters GROUPS (after GROUP BY).

## 4.2 Aggregate functions + GROUP BY

Aggregates: `COUNT, SUM, AVG, MAX, MIN` — they collapse many rows into one value.

```sql
SELECT dept, AVG(salary)
FROM Emp
GROUP BY dept
HAVING AVG(salary) > 45000;
```
Meaning: for each department, show average salary — but only departments averaging above 45000.

Flow of a query: **WHERE → GROUP BY → HAVING → SELECT → ORDER BY** (this order matters for MCQs!)

**Q2.** `SELECT COUNT(*), dept FROM Emp GROUP BY dept HAVING COUNT(*) > 5;` returns:
- A) Employees with salary > 5  B) Departments with more than 5 employees  C) Error  D) First 5 departments

✅ **Answer: B.**

**Q3.** Which aggregate ignores NULL values?
- A) COUNT(*)  B) COUNT(col)  C) Both equally  D) Neither

✅ **Answer: B.** COUNT(col) skips NULLs; COUNT(*) counts all rows.

## 4.3 JOINs (THE most requested Veersa interview topic)

### From zero
JOIN = combine rows of two tables using a common column.
Example: `Emp(dept_id)` + `Dept(id, dept_name)`.

- **INNER JOIN** — only rows matching in BOTH tables.
- **LEFT JOIN** — ALL left-table rows + matches; NULLs where no match.
- **RIGHT JOIN** — ALL right-table rows + matches.
- **FULL OUTER JOIN** — everything from both sides.
- **CROSS JOIN** — every row × every row (Cartesian product).

```sql
SELECT e.name, d.dept_name
FROM Emp e
INNER JOIN Dept d ON e.dept_id = d.id;
```

**Q4.** Which JOIN returns all rows from the left table and matching rows from the right (NULLs otherwise)?
- A) INNER  B) LEFT  C) RIGHT  D) CROSS

✅ **Answer: B.**

**Q5.** Two tables, 3 rows and 4 rows, CROSS JOINed → how many rows?
- A) 7  B) 12  C) 34  D) 3

✅ **Answer: B.** 3 × 4 = 12 (Cartesian product).

## 4.4 The classic "second highest salary" (memorize!)

```sql
SELECT MAX(salary) FROM Emp
WHERE salary < (SELECT MAX(salary) FROM Emp);
```
Logic: find the overall max; then find the max of everything BELOW it = second highest.
Alternative: `SELECT DISTINCT salary FROM Emp ORDER BY salary DESC LIMIT 1 OFFSET 1;`

**Q6.** Query for the second-highest salary?
- A) `SELECT MAX(salary) FROM Emp WHERE salary = MAX(salary)`
- B) `SELECT MAX(salary) FROM Emp WHERE salary < (SELECT MAX(salary) FROM Emp)`
- C) `SELECT salary FROM Emp LIMIT 2`
- D) `SELECT TOP 2 salary FROM Emp GROUP BY salary`

✅ **Answer: B.** (A is invalid — aggregates can't be compared like that; C returns two rows, not second-highest.)

## 4.5 Normalization (directly asked — 1NF/2NF/3NF)

Goal: organize data to remove redundancy and anomalies.

- **1NF** — every cell holds ONE atomic value (no lists like "98765, 98123" in one cell).
- **2NF** — 1NF + no partial dependency (a non-key column must not depend on only PART of a composite primary key).
- **3NF** — 2NF + no transitive dependency (non-key column must not depend on another non-key column, e.g., zip → city stored separately).
- **BCNF** — stricter 3NF; every determinant must be a candidate key.

**Q7.** A table with repeating groups / non-atomic values violates:
- A) 1NF  B) 2NF  C) 3NF  D) BCNF

✅ **Answer: A.**

**Q8.** If a non-key attribute depends on another non-key attribute, which form is violated?
- A) 1NF  B) 2NF  C) 3NF  D) BCNF

✅ **Answer: C.** That's a transitive dependency.

## 4.6 DELETE vs TRUNCATE vs DROP + keys (rapid-fire MCQs)

- **DELETE** — removes rows one-by-one, can have WHERE, can be rolled back.
- **TRUNCATE** — removes ALL rows fast, keeps table structure, cannot have WHERE (auto-commit).
- **DROP** — deletes the entire table (structure gone).

Keys:
- **Primary key** — unique + NOT NULL identifier of a row.
- **Foreign key** — column referencing the primary key of another table (enforces referential integrity).
- **Candidate key** — any column(s) that could be primary; the chosen one is primary.
- **Unique key** — unique but allows one NULL (unlike primary key).

**Q9.** Removes all rows but keeps the table structure; can't be rolled back in most DBMS:
- A) DELETE  B) DROP  C) TRUNCATE  D) ALTER

✅ **Answer: C.**

**Q10.** Which key can accept NULL (once) but must be unique?
- A) Primary  B) Foreign  C) Unique  D) Composite

✅ **Answer: C.**

**Q11.** A column that references the primary key of another table is a:
- A) Candidate key  B) Foreign key  C) Super key  D) Alternate key

✅ **Answer: B.**

---
---

# SECTION 5: CODING (interview round — easy/medium arrays & strings)

*Reported pattern at Veersa: one live coding problem on ARRAYS or STRINGS. Practice writing these on paper — you may be asked to.*

## 5.1 The core 8 patterns (learn cold)

**1. Reverse a string**
```java
String rev = "";
for (int i = s.length() - 1; i >= 0; i--) rev += s.charAt(i);
```

**2. Palindrome check** (reads same both ways)
```java
boolean isPal = true;
for (int i = 0; i < s.length()/2; i++)
    if (s.charAt(i) != s.charAt(s.length()-1-i)) { isPal = false; break; }
```
"madam" → palindrome: compare i-th char from front with i-th from back.

**3. Find max/min in array**
```java
int max = arr[0];
for (int i = 1; i < arr.length; i++) if (arr[i] > max) max = arr[i];
```
(For min: flip `>` to `<`.)

**4. Sum & average**
```java
int sum = 0;
for (int x : arr) sum += x;
double avg = (double) sum / arr.length;
```

**5. Count vowels**
```java
int c = 0;
for (char ch : s.toLowerCase().toCharArray())
    if ("aeiou".indexOf(ch) != -1) c++;
```
`indexOf` returns -1 if the char is not in "aeiou".

**6. Prime check** (n > 1, divisible only by 1 and itself)
```java
boolean prime = n > 1;
for (int i = 2; i * i <= n; i++)
    if (n % i == 0) { prime = false; break; }
```
Only test divisors up to √n — the efficiency trick interviewers like.

**7. Factorial & Fibonacci** — see Section 2 Q6/Q14, revise!

**8. Frequency count**
```java
HashMap<Character,Integer> map = new HashMap<>();
for (char ch : s.toCharArray())
    map.put(ch, map.getOrDefault(ch, 0) + 1);
```

**Q1 (practice).** Second largest of {12, 35, 1, 10, 34, 1}?
✅ **Answer: 34.** Track `first` and `second`: if x > first → second=first, first=x; else if x > second && x != first → second=x.

**Q2 (practice).** Count each character in "veersa".
✅ v:1, e:2, r:1, s:1, a:1 — HashMap pattern above. ("Count repeated characters" is loved by them.)

## 5.2 Java reminders
- Input: `Scanner sc = new Scanner(System.in); int n = sc.nextInt(); String s = sc.next();`
- Array length: `arr.length` (no parentheses); String: `s.length()`.

---

# SECTION 6: PUZZLES (reported at Veersa interviews)

**P1. Candle timer (ACTUALLY ASKED — "melting candles puzzle").**
A candle burns fully in 60 min. Two candles, only a lighter. Measure exactly 45 minutes.
✅ **Solution:** Light candle A at BOTH ends and candle B at ONE end simultaneously. A finishes in 60/2 = 30 min. Then light B's other end too — B has 30 min of burn left, now burning at double rate → 15 more min. Total = 30 + 15 = **45 min**.

**P2. 25 horses, 5 tracks, no stopwatch. Top 3 — minimum races?**
✅ **Answer: 7.** Five group races (1–5). Race the 5 group winners (race 6) → that winner is #1. For #2/#3 only candidates are: 2nd/3rd from winner's group, 1st/2nd from runner-up's group, 1st from third group → one final race (race 7).

**P3. 8 identical balls, one heavier. Balance scale — minimum weighings?**
✅ **Answer: 2.** Split 3-3-2. Weigh 3 vs 3: if balanced, heavy is in the last 2 (1 weighing); else heavier 3 → weigh 1 vs 1 (skip one). Total 2.

**P4. Two non-uniform ropes, each burns in 60 min. Measure 30 min?**
✅ Light one rope at BOTH ends → exactly 30 min regardless of non-uniformity.

---

# SECTION 7: QA-ROLE BASICS (10-minute insurance — may not be in OA, but you're interviewing for QA)

- **QA vs QC:** QA = process-oriented, prevents defects; QC = product-oriented, finds defects (testing).
- **SDLC:** Requirement → Design → Coding → Testing → Deployment → Maintenance.
- **STLC:** Requirement analysis → Test planning → Test case design → Environment setup → Execution → Closure.
- **Verification** = "building the product RIGHT" (reviews, no execution). **Validation** = "building the RIGHT product" (actual testing).
- **Levels:** Unit → Integration → System → Acceptance (UAT).
- **Black-box** = no code knowledge; **White-box** = with code; **Grey-box** = partial.
- **Functional** = what the system does; **Non-functional** = how (performance, security, usability).
- **Regression** = re-test after changes; **Smoke** = basic stability check; **Sanity** = narrow check after minor changes.
- **Severity** = impact (business); **Priority** = urgency (fix schedule). High severity + low priority: crash in a rarely used legacy feature.
- **Bug life cycle:** New → Assigned → Open → Fixed → Retest → Verified → Closed (or Reopened).

---

# SECTION 8: GD + INTERVIEW (round 2 — critical!)

One real candidate was REJECTED mainly for weak English/soft skills. Don't let that be you.

**GD (groups of ~5, general topics):**
- Structure: 1 opening line → 2–3 points → 1 closing line. Quality > quantity.
- Practice 1-minute speeches on: "AI — boon or bane", "Social media's impact on students", "Remote work vs office", "Is technology making us lazy?"
- Do: listen, acknowledge ("I'd like to add to that…"), be calm and clear. Don't: shout, stay silent, interrupt rudely.

**Technical interview — confirmed question bank from real Veersa interviews:**
1. Resume projects — tech stack, YOUR role, challenges, results (3-min story each).
2. WRITE SQL: joins between two tables + aggregates (practice Section 4.3 on paper).
3. Live coding: array/string problem (Section 5).
4. One logic puzzle (Section 6).
5. If you say Java: why Java? Multithreading basics (Thread, Runnable, synchronization).
6. MERN/React/Node on resume → syntax-level questions on them.
7. HR: why Veersa, relocation to Noida, strengths/weaknesses, stress handling.

---

# SECTION 9: FINAL RANKED CHECKLIST

| Priority | Topic | Why |
|---|---|---|
| 🔴 1 | Quant aptitude (Sec 1) | Biggest section, reported every year |
| 🔴 2 | SQL (Sec 4): joins, GROUP BY, 2nd-highest, normalization | Every report mentions it |
| 🔴 3 | OOPs (Sec 3): overloading/overriding, abstract vs interface, final/static | Every report mentions it |
| 🔴 4 | Negative-marking strategy: attempt only when you can eliminate 2 options | −4 per wrong answer! |
| 🟠 5 | Output prediction (Sec 2): Java increments, loops, JS coercion | Confirmed in 2024 OA |
| 🟠 6 | GD prep (Sec 8): 1-min intro + 3 topics | GD is in your official process |
| 🟠 7 | Resume projects — 3-min story each | Guaranteed interview question |
| 🟡 8 | Easy array/string coding (Sec 5) | Interview round |
| 🟡 9 | Puzzles (Sec 6) | Interview round |
| 🟡 10 | QA/SDLC/STLC definitions (Sec 7) | Insurance; may not be asked |
| ⬜ Skip | Advanced DSA (DP/graphs/trees), Selenium, system design, ML | Never reported in Veersa fresher OA |

## Night-before quick revision card
- m/s ↔ km/h: ×18/5 / ×5/18
- Successive change: a + b + ab/100
- Together work: ab/(a+b)
- P(at least one head) = 1 − (1/2)ⁿ
- Overloading = compile-time; Overriding = runtime
- final method: no override; final class: no inherit; interface: no constructor
- WHERE before grouping; HAVING after
- Second-highest salary: MAX where < MAX
- TRUNCATE: all rows, no WHERE, no rollback; DROP: table gone
- Parent ref + child object → child's overridden method runs
- Candles: both ends = half time

*Sources: GeeksforGeeks Veersa Technologies interview experiences (2023–2024, four candidate posts); official MSIT placement notice for the 8 Sept 2026 drive (Prometric test → GD (optional) → interview). Reported details may vary slightly for your drive.*

**Good luck! 🎯**
