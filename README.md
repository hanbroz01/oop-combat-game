# 🛡️ OOP Combat Game (WIP)

A **text-based Python combat game** built to practice and demonstrate **object-oriented programming (OOP)** concepts such as **inheritance, encapsulation, and method reuse**.

This project is an **iterative work-in-progress (WIP)** and primarily serves as a **learning and experimentation project**.

---

## Description

This project focuses on **clean, readable OOP design** rather than full gameplay complexity.

### Current highlights:

- Demonstrates core **Python OOP principles**
- Clear separation of responsibilities using a base class
- Simple but extendable combat mechanics

> ⚠️ **Work in progress:** Core mechanics are implemented, but full gameplay systems are still under development.

---

## Code Structure

- **`Character`**  
  Base class containing shared attributes and combat logic:
  - `health`
  - `power`
  - `attack()`
  - `receive_damage()`

- **`Player (Character)`**  
  Extends `Character` with:
  - Leveling system
  - Stat progression (health & power increase)

- **`Monster (Character)`**  
  Extends `Character` with:
  - Rage mode that temporarily doubles power

This structure allows easy expansion with new character types, enemies, or mechanics.

---

## Installation

### Requirements

- **Python 3.10+** (tested)

### Setup

```bash
git clone https://github.com/hanbroz01/oop-combat-game.git
cd oop-combat-game
python main.py
```

## Usage

Running `main.py` currently demonstrates the **core combat mechanics** using the Player and Monster classes:

- One **Player** and one **Monster** are created
- Hard-coded attacks show damage, health changes, leveling, and rage
- Console output provides clear feedback for each action

> ⚠️ **Note:** This version is purely **mechanics-focused**. There is no actual gameplay loop, randomness, or player input yet. Every run produces the same deterministic output, which is ideal for testing and explaining OOP design.

---

## Features (Current)

- Player leveling system
- Monster rage mechanic (temporary power boost)
- Combat with fixed damage tracking
- Health floor (prevents negative health)
- Clear console feedback for actions
- Easy to extend and test new mechanics

---

## Planned Features

- **Turn-based game loop:** allow players and monsters to take turns until one wins
- **Multiple monsters per session:** introduce several enemies for more strategic combat
- **Inventory and items:** healing potions, buffs, or weapons to add strategy
- **Player choices:** attack, heal, or use items, potentially with randomized outcomes
- **Win / lose conditions and scoring:** track success, experience, or rewards
- **Optional GUI or text-based menu system:** improve user experience beyond console output
- **Randomized damage / critical hits:** add unpredictability for replayability
- **Save/load system:** keep player progress for longer sessions

---

## Example Gameplay

Here is an example of running the current combat mechanics:

```text
Testing:
These are the starting stats for Han:
Level = 1
Health = 3
Power = 1

Han attacks Goblin for 1 damage!

Goblin received 1 damage.

Goblin attacks Han for 1 damage!

Han received 1 damage.


----------------------------------------

Goblin received 100 damage.

Han leveled up! Level: 2, Health: 3, Power: 2

----------------------------------------

Goblin is raging! Power doubled to 2.
Goblin attacks Han for 2 damage!

Han received 2 damage.


Demo complete!
```

> ⚠️ **Note:** This is currently a **deterministic test run** to demonstrate combat mechanics. There is no actual gameplay loop or player input yet. Each run produces the same output, making it ideal for testing and explaining OOP concepts.

---

## Notes

- Built as a **learning and prototype project**
- Focuses on **readability, structure, and extensibility**
- Deterministic output ensures mechanics are clear and easy to explain
- Future iterations will introduce gameplay loops, randomness, and interactivity

---

### ⭐ Why this project?

This repository is part of my learning journey and is designed to clearly demonstrate how **object-oriented design** can be applied to game mechanics in Python.
