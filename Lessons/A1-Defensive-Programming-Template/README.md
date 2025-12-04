---
title: "Defensive Programming, Errors, and Contracts"
layout: layouts/course.njk
courseId: A1-Defensive-Programming-Template
level: Intermediate
duration: 3-4 hours
description: "Write resilient code that fails fast, communicates intent, and recovers gracefully."
tags:
  - course
  - programming
  - intermediate
  - defensive-programming
date: 2025-11-17T20:00:00.000000
---
# A1: Defensive Programming, Errors, and Contracts

## Course Overview
**Duration**: 3–4 hours
**Prerequisites**: Testing foundations
**Goal**: Write resilient code that fails fast, communicates intent, and recovers gracefully.

## Learning Objectives
By the end of this lesson, you will be able to:
- Choose EAFP or LBYL appropriately, with justification
- Implement clear error handling with actionable messages
- Add targeted tests for error paths and contracts
- Build defensive programming patterns into existing code

## Topics Covered
- EAFP vs LBYL and when to use each
- Invariants, assertions, guard clauses
- Python exceptions hierarchy, custom exceptions, error boundaries
- Design by contract (pre-/post-conditions)
- Sentinel values vs exceptions; logging basics

## Folder Structure
```
A1-Defensive-Programming/
├── README.md                          # This overview
├── lesson-content.md                 # Detailed lesson material
├── summary.md                        # Key takeaways and assessment
├── tests/                            # Practice exercises and implementations
│   ├── calculator.py                # Practice module to harden
│   ├── config_loader.py             # Alternative practice module
│   ├── test_calculator.py           # Basic tests + exercise instructions
│   ├── test_config_loader.py        # Basic tests + exercise instructions
│   ├── test_calculator_hardened.py  # ✨ Complete defensive implementation
│   └── test_config_loader_hardened.py # ✨ Complete defensive implementation
├── solutions/                        # Reference solutions
│   └── calculator_solution.md       # Example solution approach
└── reference/                        # Learning resources
    ├── exercise_instructions.md     # Step-by-step exercise guide
    ├── quick_reference.md           # Patterns and templates
    ├── python_exceptions.md         # Exception hierarchy reference
    ├── best_practices.md            # Defensive programming guidelines
    └── common_pitfalls.md           # What to avoid
```## Getting Started

### Prerequisites Check
Before you start, ensure:
- [ ] Repository cloned and tests run locally (`pytest -q`)
- [ ] Python >= 3.10 and virtual environment active
- [ ] CI has pytest + coverage set up

### Learning Path
1. **Read** `lesson-content.md` for theoretical foundation
2. **Study** exercise instructions in `reference/exercise_instructions.md`
3. **Practice** with modules in `tests/` folder (`calculator.py`, `config_loader.py`)
4. **Test** your improvements by running the test files
5. **Compare** your approach with `solutions/calculator_solution.md`
6. **Review** `summary.md` for key takeaways and self-assessment
7. **Reference** additional materials in `reference/` as needed

### Quick Win Goal
Convert a nested conditional into guard clauses; tests become easier to read.

## Assessment Criteria
Your implementation will be considered successful when:
- [ ] Tests pass and include error-path coverage (>= 2 new tests)
- [ ] No bare except statements; custom exceptions used where appropriate
- [ ] Logs include context (inputs or IDs) without leaking secrets
- [ ] Code demonstrates clear understanding of EAFP vs LBYL principles

## Common Pitfalls to Avoid
- Overusing exceptions for control flow
- Leaking sensitive data in error messages or logs

## Reflection Questions
- Which contract assertion prevented a bug you might have missed?
- How did guard clauses improve your code's readability?
- What patterns emerged in your error handling strategy?
