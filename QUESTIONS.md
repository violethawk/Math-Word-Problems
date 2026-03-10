# Complete Question & Answer Set

110 problems across 3 phases and 8 difficulty tiers. Every problem, its expected answer, and the operation plan (where applicable).

For each tier, one full worked example is shown first, followed by the remaining problems.

---

## Phase 1 — Calculator Only (50 problems)

The agent has one tool: a basic calculator (add, subtract, multiply, divide). Problems have unambiguous answers.

### Tier 1 — Single Operation (10 problems)

#### Worked Example

```
Problem:  "What is 47 plus 83?"
Answer:   130

Step 1 -- THINK:   I need to add 47 and 83.
Step 2 -- ACT:     calculator({operation: "add", a: 47, b: 83})
Step 3 -- OBSERVE: 130.0
Step 4 -- THINK:   FINAL ANSWER: 130
```

Operation plan: `add(47, 83) → 130`

#### All Tier 1 Problems

| # | Problem | Answer |
|---|---------|--------|
| 1 | What is 47 plus 83? | 130 |
| 2 | A book costs $15. You buy 3. How much total? | 45 |
| 3 | You have 100 stickers and give away 37. How many left? | 63 |
| 4 | A pizza is cut into 8 slices. 3 people split it equally. How many slices does each person get? | 2.667 |
| 5 | I have 20 marbles and my friend gives me 15 more. How many marbles do I have? | 35 |
| 6 | A car travels 60 miles in one hour. How far does it travel in 4 hours? | 240 |
| 7 | You buy 5 bags of candy with 7 candies each. How many candies do you have? | 35 |
| 8 | There are 45 students and 3 classes. If the students are split equally, how many students per class? | 15 |
| 9 | A farmer has 24 eggs and sells 10. How many eggs remain? | 14 |
| 10 | Each pack has 6 batteries. How many batteries are in 5 packs? | 30 |

---

### Tier 2 — Two Operations (10 problems)

#### Worked Example

```
Problem:  "I have 3 baskets with 12 apples each. I eat 7. How many are left?"
Answer:   29

Step 1 -- THINK:   I need to find the total number of apples. Multiply 3 baskets by 12 apples.
Step 2 -- ACT:     calculator({operation: "multiply", a: 3, b: 12})
Step 3 -- OBSERVE: 36.0
Step 4 -- THINK:   Now subtract the 7 apples eaten.
Step 5 -- ACT:     calculator({operation: "subtract", a: 36, b: 7})
Step 6 -- OBSERVE: 29.0
Step 7 -- THINK:   FINAL ANSWER: 29
```

Operation plan: `multiply(3, 12) → 36`, then `subtract(36, 7) → 29`

#### All Tier 2 Problems

| # | Problem | Answer |
|---|---------|--------|
| 1 | I have 3 baskets with 12 apples each. I eat 7. How many are left? | 29 |
| 2 | A pizza has 8 slices. 3 people each eat 2 slices. How many are left? | 2 |
| 3 | You earn $15/hour and work 8 hours. You spend $40 on groceries. How much do you have? | 80 |
| 4 | A class has 28 students. 4 are absent. The rest split into groups of 6. How many groups? | 4 |
| 5 | A container holds 5 liters. You have 3 containers and pour out 2 liters. How much liquid is left? | 13 |
| 6 | You read 30 pages of a book each day for 5 days. Then you read 20 pages. How many pages have you read? | 170 |
| 7 | There are 10 packs of pencils with 12 pencils each. You give away 15 pencils. How many pencils remain? | 105 |
| 8 | A farmer has 7 cows and buys 5 more. Each cow produces 8 liters of milk. How much milk do the cows produce? | 96 |
| 9 | You save $50 each week for 6 weeks. Then you spend $120. How much do you have left? | 180 |
| 10 | A theatre has 200 seats. In a show, 75 tickets are sold online and 50 at the door. How many seats are empty? | 75 |

---

### Tier 3 — Three Operations (10 problems)

#### Worked Example

```
Problem:  "A store has 4 shelves with 15 books each. They sell 12 and receive a shipment of 20. How many now?"
Answer:   68

Step 1 -- THINK:   First, find total books on shelves: 4 shelves x 15 books.
Step 2 -- ACT:     calculator({operation: "multiply", a: 4, b: 15})
Step 3 -- OBSERVE: 60.0
Step 4 -- THINK:   They sold 12, so subtract.
Step 5 -- ACT:     calculator({operation: "subtract", a: 60, b: 12})
Step 6 -- OBSERVE: 48.0
Step 7 -- THINK:   They received 20 more books.
Step 8 -- ACT:     calculator({operation: "add", a: 48, b: 20})
Step 9 -- OBSERVE: 68.0
Step 10 -- THINK:  FINAL ANSWER: 68
```

Operation plan: `multiply(4, 15) → 60`, then `subtract(60, 12) → 48`, then `add(48, 20) → 68`

#### All Tier 3 Problems

| # | Problem | Answer |
|---|---------|--------|
| 1 | A store has 4 shelves with 15 books each. They sell 12 and receive a shipment of 20. How many now? | 68 |
| 2 | You earn $12/hour for 8 hours, then $18/hour for 3 hours overtime. What's your total pay? | 150 |
| 3 | A farmer plants 5 rows of 10 trees each. 8 trees die. He plants 12 more. How many trees? | 54 |
| 4 | A factory produces 20 gadgets per hour for 5 hours and then 15 gadgets per hour for 4 hours. How many gadgets produced? | 160 |
| 5 | You have $200. You buy a jacket for $60, shoes for $45, and then earn $80 mowing lawns. How much money do you have now? | 175 |
| 6 | A cafe sells 150 coffees per day. On Monday they sell 30 more than usual, on Tuesday 20 less than usual. How many coffees in two days? | 310 |
| 7 | There are 120 guests at a party. 30 leave early and 15 more arrive. Then 20 leave. How many guests now? | 85 |
| 8 | You run 5 km each day for 3 days. Then you run 8 km and 2 km more. What's the total distance run? | 25 |
| 9 | A factory has 100 widgets. They ship 30, produce 50 more, then discard 10 defective. How many widgets remain? | 110 |
| 10 | An account had $500. Withdraw $120, deposit $200, and pay a bill of $150. How much remains? | 430 |

---

### Tier 4 — Four Operations (10 problems)

#### Worked Example

```
Problem:  "A farmer has 3 fields. Each produces 250 bushels. He sells half at $4/bushel
           and stores the rest. What did he earn?"
Answer:   1500

Step 1  -- THINK:   Total production: 3 fields x 250 bushels.
Step 2  -- ACT:     calculator({operation: "multiply", a: 3, b: 250})
Step 3  -- OBSERVE: 750.0
Step 4  -- THINK:   He sells half, so divide by 2.
Step 5  -- ACT:     calculator({operation: "divide", a: 750, b: 2})
Step 6  -- OBSERVE: 375.0
Step 7  -- THINK:   He sells those at $4 per bushel.
Step 8  -- ACT:     calculator({operation: "multiply", a: 375, b: 4})
Step 9  -- OBSERVE: 1500.0
Step 10 -- THINK:   FINAL ANSWER: 1500
```

Operation plan: `multiply(3, 250) → 750`, then `divide(750, 2) → 375`, then `multiply(375, 4) → 1500`

#### All Tier 4 Problems

| # | Problem | Answer |
|---|---------|--------|
| 1 | A farmer has 3 fields. Each produces 250 bushels. He sells half at $4/bushel and stores the rest. What did he earn? | 1500 |
| 2 | A school has 6 classes of 25 students. Each student needs 3 notebooks at $2 each. What's the total cost? | 900 |
| 3 | A company has 5 departments with 12 employees each. Each employee receives 3 certificates. Each certificate costs $10. There's a 5% discount on the total. What is the discounted cost? | 1710 |
| 4 | A factory produces 100 widgets per day for 7 days. It sells each widget for $15 and pays $3 in costs per widget. What is the total profit? | 8400 |
| 5 | A rectangular garden is 20m long and 15m wide. Fencing costs $12 per meter. There is a walkway costing $50. What is the total cost? | 890 |
| 6 | A school sells 120 tickets to a play at $10 each. They spend $300 on costumes and $200 on props. They donate half the profits to charity. How much do they donate? | 350 |
| 7 | You start with $1000. You buy a phone for $600, then sell an old laptop for $200, then pay a bill of $150, and finally receive a gift of $50. How much money do you have? | 500 |
| 8 | A tank contains 1000 liters of water. It leaks 150 liters, then 200 liters are added, then 50 liters are used, and finally 100 liters are added. How much water is in the tank? | 1100 |
| 9 | A large order of 500 pens is to be shipped. Each box holds 50 pens. You ship 6 boxes, then receive 100 additional pens. How many pens are left to ship? | 300 |
| 10 | A fruit vendor has 30 kg of apples, 20 kg of oranges, and 25 kg of bananas. She sells 10 kg of apples, 5 kg of oranges, and 15 kg of bananas. Then she buys 5 kg of apples. How many kilograms of apples does she have now? | 25 |

---

### Tier 5 — Five Operations (10 problems)

#### Worked Example

```
Problem:  "A bakery makes 12 dozen cookies. They sell 40% on Monday and 25% of the
           remainder on Tuesday. How many are left after Tuesday?"
Answer:   64.8

Step 1  -- THINK:   12 dozen = 12 x 12 cookies.
Step 2  -- ACT:     calculator({operation: "multiply", a: 12, b: 12})
Step 3  -- OBSERVE: 144.0
Step 4  -- THINK:   They sell 40% on Monday. Find 40% of 144.
Step 5  -- ACT:     calculator({operation: "multiply", a: 144, b: 0.40})
Step 6  -- OBSERVE: 57.6
Step 7  -- THINK:   Subtract Monday's sales from total.
Step 8  -- ACT:     calculator({operation: "subtract", a: 144, b: 57.6})
Step 9  -- OBSERVE: 86.4
Step 10 -- THINK:   Now 25% of the remainder (86.4) is sold on Tuesday.
Step 11 -- ACT:     calculator({operation: "multiply", a: 86.4, b: 0.25})
Step 12 -- OBSERVE: 21.6
Step 13 -- THINK:   Subtract Tuesday's sales.
Step 14 -- ACT:     calculator({operation: "subtract", a: 86.4, b: 21.6})
Step 15 -- OBSERVE: 64.8
Step 16 -- THINK:   FINAL ANSWER: 64.8
```

Operation plan: `multiply(12, 12) → 144`, then `multiply(144, 0.40) → 57.6`, then `subtract(144, 57.6) → 86.4`, then `multiply(86.4, 0.25) → 21.6`, then `subtract(86.4, 21.6) → 64.8`

#### All Tier 5 Problems

| # | Problem | Answer |
|---|---------|--------|
| 1 | A bakery makes 12 dozen cookies. They sell 40% on Monday and 25% of the remainder on Tuesday. How many are left after Tuesday? | 64.8 |
| 2 | A computer is discounted by 15%, then a coupon takes off $50, then a 8% sales tax is applied. The original price is $1000. What is the final price? | 864 |
| 3 | A runner completes 10 km on Monday, 12 km on Tuesday, 8 km on Wednesday, and 3 km on Thursday. She then doubles the total distance and subtracts 5 km for rest days. What is her final training distance? | 61 |
| 4 | A factory produces 100 widgets per day for 5 days, then 120 widgets per day for 3 days. They ship 400 widgets and then 100 widgets are returned. How many widgets remain? | 560 |
| 5 | A bank account starts with $2000. You deposit $500, withdraw $300, earn 5% interest on the current balance, then pay a $50 fee. What is the final balance? | 2260 |
| 6 | A car travels 50 mph for 2 hours, then 60 mph for 1 hour, takes a 0.5-hour break, then travels 55 mph for 1.5 hours. What is the total distance traveled? | 242.5 |
| 7 | A 1000-liter tank is empty. Water flows in at 50 liters/min for 10 minutes, out at 30 liters/min for 5 minutes, then in at 40 liters/min for 5 minutes. Afterwards, half is pumped out. How much water remains? | 275 |
| 8 | A construction project requires 1000 bricks. Workers lay 200 bricks/day for 3 days, then 150 bricks/day for 2 days, and then remove 50 damaged bricks. How many bricks remain to be laid? | 150 |
| 9 | A travel itinerary: flight 3.5 hours, train 2.75 hours, layover 1.25 hours, car 4.5 hours, boat 1 hour. There is a 30-minute break during the car drive. What is the total travel time? | 12.5 |
| 10 | A class buys 20 boxes of pencils (12 each). They distribute 180, lose 15, then buy 5 more boxes. How many pencils do they have now? | 105 |

---

## Phase 2 — Multiple Tools (30 problems)

The agent chooses between four tools: calculator, unit_converter, percentage_calculator, and date_calculator. Problems don't specify which tool to use.

### Tier 6 — Tool Selection Required

#### Worked Example

```
Problem:  "A recipe calls for 2.5 cups of flour for 4 servings. You're making 8 servings.
           How many grams of flour do you need?"
Answer:   600

Step 1  -- THINK:   I need to scale the recipe from 4 to 8 servings first. That's a ratio of 8/4 = 2.
Step 2  -- ACT:     calculator({operation: "divide", a: 8, b: 4})
Step 3  -- OBSERVE: 2.0
Step 4  -- THINK:   Multiply 2.5 cups by the scaling factor of 2.
Step 5  -- ACT:     calculator({operation: "multiply", a: 2.5, b: 2.0})
Step 6  -- OBSERVE: 5.0
Step 7  -- THINK:   Now convert 5 cups of flour to grams. I need the unit converter.
Step 8  -- ACT:     unit_converter({value: 5.0, from_unit: "cups_flour", to_unit: "grams"})
Step 9  -- OBSERVE: 600.0
Step 10 -- THINK:   FINAL ANSWER: 600
```

Tools used: calculator (scaling) + unit_converter (cups to grams)

#### All Tier 6 Problems

| # | Problem | Answer | Tools Needed |
|---|---------|--------|--------------|
| 1 | A shirt costs $80 and is 25% off. What is the sale price? | 60 | percentage |
| 2 | A laptop costs $1200. There's a 10% discount, then you pay 8% sales tax on the discounted price. What do you pay? | 1166.4 | percentage + calculator |
| 3 | You earn $3000 per month. You save 15% of your salary. After 4 months, how much have you saved? | 1800 | percentage + calculator |
| 4 | A restaurant bill is $85. You want to leave a 20% tip. What is the total amount you pay? | 102 | percentage |
| 5 | A store marks up products by 40%. If a product costs $50 to make, what is the selling price? | 70 | percentage |
| 6 | A recipe calls for 2.5 cups of flour for 4 servings. You're making 8 servings. How many grams of flour do you need? | 600 | calculator + unit_converter |
| 7 | You drive 120 miles. Your friend drives 150 km. Who drove farther, and by how many miles? | 26.82 | unit_converter + calculator |
| 8 | A package weighs 5 lbs. You need to ship 3 of them. What is the total weight in kilograms? | 6.8 | calculator + unit_converter |
| 9 | A room is 15 feet long and 12 feet wide. What is the area in square feet? | 180 | calculator |
| 10 | You run a 10 km race in 50 minutes. What was your pace in minutes per mile? | 8.05 | unit_converter + calculator |
| 11 | A town has 25000 people. The population grew by 12% last year. Then 500 people moved away. What is the current population? | 27500 | percentage + calculator |
| 12 | You invest $5000 and earn 7% return. You then withdraw $200. How much remains? | 5150 | percentage + calculator |
| 13 | A class of 40 students took a test. 85% passed. Of those who passed, 6 got an A. How many who passed did not get an A? | 28 | percentage + calculator |
| 14 | A factory produces 2000 units. 3% are defective. Each defective unit costs $25 to fix. What is the total repair cost? | 1500 | percentage + calculator |
| 15 | A house was bought for $250000 and appreciated by 8%. What is it worth now in thousands of dollars? | 270 | percentage + calculator |
| 16 | A European car gets 15 km per liter. Fuel costs $1.20 per liter. You drive 100 miles. How much do you spend on fuel? | 12.87 | unit_converter + calculator |
| 17 | You weigh 180 lbs and want to lose 10% of your body weight. How many kilograms do you need to lose? | 8.16 | percentage + unit_converter |
| 18 | A recipe for 6 people uses 500 grams of sugar. You're cooking for 9 people. How many cups of sugar do you need? | 3.75 | calculator + unit_converter |
| 19 | You start a project on 2025-03-01 and it takes 45 days. Then you have a 10-day review. How many total days from start to review end? | 55 | calculator + date_calculator |
| 20 | An event is 120 days away. You need 90 days to prepare. How many days do you have before you must start preparing? | 30 | calculator |
| 21 | You buy 3 items at $40 each with a 15% discount. Convert the total to euros at 0.92 euros per dollar. How many euros do you pay? | 93.84 | calculator + percentage + converter |
| 22 | A 50 kg bag of rice costs $80. You need 110 lbs of rice. How much will it cost? | 79.88 | unit_converter + calculator |
| 23 | A car travels 300 miles on 10 gallons of gas. Gas costs $3.50 per gallon. How many km can you drive per dollar spent? | 13.79 | unit_converter + calculator |
| 24 | Your salary is $4500. You pay 22% in taxes and then convert the remainder to British pounds at 0.79 per dollar. How many pounds do you take home? | 2772.9 | percentage + calculator |
| 25 | A pool holds 10000 gallons. You fill it at 5 gallons per minute. After 80% is full, you switch to 3 gallons per minute. How many total minutes to fill it? | 2266.67 | percentage + calculator |
| 26 | A 5 km race charges $30 entry. If 200 runners sign up and 15% drop out, how much revenue is collected from those who actually run? | 5100 | percentage + calculator |
| 27 | A farmer has 200 acres. He plants 60% with corn and 25% with wheat. How many acres are unplanted? | 30 | percentage + calculator |
| 28 | You mix 2 lbs of coffee at $12/lb with 3 lbs at $8/lb. What is the average price per kilogram of the blend? | 21.16 | calculator + unit_converter |
| 29 | A marathon is 26.2 miles. You ran 30 km. What percentage of a marathon have you completed? | 71.17 | unit_converter + calculator |
| 30 | A tank holds 500 liters. It's 40% full. You add 50 gallons of water (1 gallon = 3.785 liters). How many liters are in the tank now? | 389.25 | percentage + unit_converter + calculator |

---

## Phase 3 — Incomplete Information (30 problems)

The agent must recognize unsolvable problems and reject them rather than hallucinate. 20 solvable problems are mixed with 10 unsolvable ones.

### Tier 7 — Solvable (with distractors and tricks)

#### Worked Example

```
Problem:  "John is 35 years old and weighs 180 lbs. He buys 6 apples at $0.75 each.
           How much does he spend?"
Answer:   4.5

Step 1 -- THINK:   The age (35) and weight (180 lbs) are irrelevant distractors.
                    I just need to multiply 6 apples by $0.75.
Step 2 -- ACT:     calculator({operation: "multiply", a: 6, b: 0.75})
Step 3 -- OBSERVE: 4.5
Step 4 -- THINK:   FINAL ANSWER: 4.5
```

Key skill: filtering irrelevant information.

#### All Tier 7 Problems

| # | Problem | Answer | Notes |
|---|---------|--------|-------|
| 1 | A train travels at 80 mph for 3 hours. How far does it go? | 240 | Straightforward |
| 2 | You buy 4 notebooks at $3 each and 2 pens at $1.50 each. The store gives you a $2 discount. How much do you pay? | 13 | Multi-step |
| 3 | A garden is 10m by 8m. You plant flowers in a 3m by 3m section. How much area is left unplanted? | 71 | Area subtraction |
| 4 | There are 5 red balls, 3 blue balls, and 7 green balls. You remove all the blue balls. How many remain? | 12 | Ignore blue count |
| 5 | A movie is 2 hours and 15 minutes long. You've watched 45 minutes. How many minutes are left? | 90 | Unit conversion |
| 6 | A baker makes 5 dozen muffins and sells them for $2 each. She gives 10 away for free. How much revenue? | 100 | Subtract before multiply |
| 7 | You have $500. You buy a jacket for $120 and shoes for $80. Your friend pays you back $50. How much do you have? | 350 | Chain of operations |
| 8 | A parking lot has 200 spaces. 60% are occupied in the morning. By noon, 30 more cars arrive. How many spaces are still empty? | 50 | Percentage + arithmetic |
| 9 | A pool is 50 meters long. A swimmer does 12 laps (one lap = one length). How many meters did she swim? | 600 | Interpret "lap" |
| 10 | A teacher has 120 worksheets. She gives 4 worksheets to each of her 28 students. How many are left over? | 8 | Multiply then subtract |
| 11 | John is 35 years old and weighs 180 lbs. He buys 6 apples at $0.75 each. How much does he spend? | 4.5 | Distractor info |
| 12 | A blue car has 4 doors. A red car has 2 doors. There are also 3 motorcycles. How many doors on the cars? | 6 | Ignore motorcycles |
| 13 | Sarah has 3 cats, 2 dogs, and a goldfish. Each cat eats 200g/day, each dog 400g. How much food per day? | 1400 | Ignore goldfish |
| 14 | A room is 15ft long, 12ft wide, 9ft tall. Paint costs $25/gallon covering 350 sq ft. You only paint the floor. How many square feet? | 180 | Ignore height and paint |
| 15 | 52 cards in a deck. Remove the 4 aces and 4 kings. Remaining cards weigh 1.5g each. How many cards remain? | 44 | Ignore weight |
| 16 | You have 3 quarters, 2 dimes, and 5 nickels. How much money in cents? | 120 | Coin values |
| 17 | A snail climbs 3 feet by day, slips back 1 foot at night. After 5 full day-night cycles, how many feet gained? | 10 | Pattern reasoning |
| 18 | Two ropes: 8m and 5m. Cut 2m off the longer one and discard it, then tie them together. Total length? | 11 | Read carefully |
| 19 | A clock strikes every hour. How many times does it strike between 1:00 PM and 5:00 PM inclusive? | 15 | Sum 1+2+3+4+5 |
| 20 | Three friends split a $90 dinner bill equally, then each leaves a $5 tip. How much does each person pay? | 35 | Per-person calculation |

---

### Tier 8 — Unsolvable (10 problems)

#### Worked Example

```
Problem:  "Two trains leave cities 400 miles apart, heading toward each other. Train A
           goes 60 mph. When do they meet?"
Answer:   UNSOLVABLE

Step 1 -- THINK:   To find when the trains meet, I need both speeds so I can compute
                    the combined closing rate. Train A's speed is 60 mph, but Train B's
                    speed is not given. Without it, I cannot solve this problem.

UNSOLVABLE: Train B's speed is missing. I cannot determine when the trains meet
without knowing how fast Train B is traveling.
```

Key skill: recognizing missing information instead of hallucinating an answer.

#### All Tier 8 Problems

| # | Problem | What's Missing |
|---|---------|----------------|
| 1 | Two trains leave cities 400 miles apart, heading toward each other. Train A goes 60 mph. When do they meet? | Train B's speed |
| 2 | A store sells apples and oranges. Apples cost $2 each. You buy some fruit and pay $14. How many apples did you buy? | Orange price and quantity breakdown |
| 3 | A rectangle has a perimeter of 30 meters. What is its area? | Individual side lengths |
| 4 | A car drives from City A to City B. The trip takes 3 hours. How fast was the car going? | Distance |
| 5 | You mix red and blue paint to make purple. You used 3 cups of red paint. How much purple paint do you have? | Amount of blue paint |
| 6 | A factory produces widgets. Each widget sells for $15. What is the factory's monthly profit? | Production count and costs |
| 7 | Three siblings share some candy. The oldest gets twice as many as the youngest. How many pieces does each child get? | Total candy and middle child's share |
| 8 | A tank is filling with water at some rate. After 2 hours it's half full. When will it be completely full? | Fill rate (can't assume constant) |
| 9 | A plane flies east at 500 mph. Another plane flies west. When will they be 2000 miles apart? | Second plane's speed |
| 10 | You earn a certain salary. After a 10% raise, you can afford a new car. How much does the car cost? | Salary amount |
