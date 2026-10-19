---
title: C coding standard
---

# C coding standard

This document outlines the coding standards for C projects, focusing on readability, maintainability, and consistency. Adhering to these guidelines will help ensure high-quality code and facilitate collaborative development.

This standard assumes a C99 or later compiler.

## File Organisation 

A file should consist of logically separated sections, each identified by a blank line and an optional comment.

### File Names

- New file names should be all lowercase.
- Use `.h` for header files and `.c` for C source files.
- File names should clearly reflect the functionality defined or implemented within them.
- Files with a logical connection (e.g., header and source pairs) should reflect this in their names.
- Files belonging to the same module should use a short, unique prefix followed by an underscore (e.g., `module_filename.c`).

Existing files may retain historical naming conventions to avoid unnecessary renaming.

**Examples:**

- `io_base.h`, `io_base.c`
- `server.c`, `server_ioplug.h`, `server_ioplug.c`

### Source Files (`.c`)

C source files should follow this ordering:

1. Beginning comments (file header).
1. Version information.
1. `#include` statements.
1. `#define`s.
1. Local data type definitions.
1. Local (static) function prototypes.
1. Local (static) data.
1. Externally visible functions.
1. Local (static) functions.

**Example File Header for `.c`:**

``` c
/**
 * @file template.c
 * @brief Brief description of contents of file.
 * @details Long description of the file's purpose and functionality.
 * @date date of last edit @todo to be auto added
 * @version CVS $Header$ field
 * @copyright
 * COPYRIGHT NOTICE: ® 20?? <Company Name> All rights reserved. <br>
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * @addtogroup name-of-library-or-application-or-module
 * @{
 */
```

### Header Files (`.h`)

All header files must begin with a comment.

**Example File Header for `.h`:**

```c
/**
 * @file template.h
 * @brief Brief description of contents of file.
 * @details Long description of the header file's purpose and contents.
 * @date date of last edit @todo to be auto added
 * @version CVS $Header$ field
 * @copyright
 * COPYRIGHT NOTICE: ® 20?? <Company Name> All rights reserved. <br>
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * @addtogroup name-of-library-or-application-or-module
 * @{
 */
```

To prevent multiple inclusions, header file contents must be protected by an `#ifndef ... #endif` pair:

```c
#ifndef NAMEOFHEADERFILEINCAPITALS_H
#define NAMEOFHEADERFILEINCAPITALS_H 1

// ...body of header file...

#endif /* NAMEOFHEADERFILEINCAPITALS_H */
```

**General Rule:** Header files should generally *not* include system header files directly. Instead, document which system header files they require.

## Indentation & Line Length

### Indentation

- Use **four spaces** as the unit of indentation.
- Do not use tabs as they can lead to inconsistent formatting.

### Line Length

- Avoid lines longer than **80 characters** for better readability across various terminals and tools.
- Note: Examples in documentation should be shorter, generally no more than 70 characters.

### Wrapping Lines

When an expression exceeds a single line, break it according to these principles:

- Break after a comma.
- Break before an operator.
- Prefer higher-level breaks to lower-level breaks.
- Align the new line with the beginning of the expression at the same level on the previous line.
- If the above rules lead to confusing or squished code, indent by **8 spaces** instead.

**Examples of Function Call Breaking:**

```c
Function(longExpression1, longExpression2, longExpression3,
         longExpression4,
         longExpression5);

var = Function(longExpression1,
               Function2(longExpression2,
                         longExpression3));
```

**Examples of Arithmetic Expression Breaking:**

```c
LongName1 = LongName2 * (LongName3 + LongName4 - LongName5)
            + 4 * longname6; /* PREFERRED */

LongName1 = LongName2 * (LongName3 + LongName4
LongName5) + 4 * Longname6; /* AVOID! */
```

**Examples of Function Declaration Indentation:**

```c
/* CONVENTIONAL INDENTATION */
Function(int AnArg, double AnotherArg, char *YetAnotherArg,
         int *AndStillAnother)
{
    // ...
}

/* INDENT 8 SPACES TO AVOID VERY DEEP INDENTS */
static ReallyLongFunctionName(int AnArg,
                               double anotherArg, char *YetAnotherArg,
                               int *AndStillAnother)
{
    // ...
}

/* OR, PUT EACH ARG ON OWN LINE */
static ReallyLongFunctionName(int AnArg,
                               double anotherArg,
                               char *YetAnotherArg,
                               int *AndStillAnother)
{
    // ...
}
```

**Ternary Expressions:** Here are three acceptable ways to format ternary expressions:

```c
alpha = (aLongBooleanExpression) ? beta : gamma;

alpha = (aLongBooleanExpression) ? beta
                                 : gamma;

alpha = (aLongBooleanExpression)
        ? beta
        : gamma;
```

## Comments 

Programs can have two kinds of comments: **implementation comments** and **documentation comments**.

- Implementation comments are delimited by `/* ... */` and are for commenting out code or providing details about the implementation.
- Documentation comments are delimited by `/** ... */` and are meant to describe the specification of the code, from an implementation-free perspective (e.g., for Doxygen).

Comments should provide overviews and additional, non-obvious information. Avoid duplicating information already clear from the code. Generally, avoid comments that are likely to become outdated as the code evolves.

**Note:** Frequent implementation comments can sometimes indicate unclear code. Consider refactoring the code to make it self-explanatory before adding comments.

### Implementation Comment Formats

Programs can use four styles of implementation comments: block, single-line, trailing, and end-of-line.

#### Block Comments

Used for descriptions of files, methods, data structures, and algorithms. They can appear at the beginning of files, before methods, or within functions. Block comments inside a function should be indented to the same level as the code they describe.

A block comment should be preceded by a blank line.

```c
/*
 * Here is a block comment.
 */
```

#### Single-Line Comments

Short comments that appear on a single line, indented to the level of the code that follows. If a comment requires more than one line, use the block comment format. A single-line comment should be preceded by a blank line.

```c
if (condition)
{
    /* Handle the condition. */
    // ...
}
```

#### Trailing Comments

Very short comments that appear on the same line as the code they describe. They should be shifted far enough to separate them from the statements. If multiple trailing comments appear in a code block, align them to the same tab setting.

```c
if (a == 2)
{
    a = TRUE;  /* special case */
}
else
{
    a = isPrime(a); /* works only for odd a */
}
```

### Documentation Comments

We use **Doxygen style headers** for documenting C functions, structures, enums, unions, etc. Each doc comment is placed immediately before the declaration it describes, enclosed within `/** ... */` delimiters. For detailed information on Doxygen comment tags (`@return`, `@param`, `@see`), refer to [The Doxygen Manual](http://www.doxygen.org "null").

```c
/**
 * @brief The function bar.
 * @details This function performs a placeholder operation. This text is
 * senseless and not intended for serious reading.
 * @note This optional text demonstrates a "note" section. There is nothing
 * critical here, so you don't need to read this section.
 * @param[in] a Description of parameter a.
 * @param[out] b Description of the parameter b.
 * @param[in,out] c Description of the parameter c.
 * @return The error return code of the function.
 * @retval ERR_SUCCESS The function is successfully executed.
 * @retval ERR_FAILURE An error occurred.
 */
errcode_t bar(int a, int b, int c)
{
    // ...
}
```

Some implementation detail does not belong in the documentation. Put it in a block or single-line comment immediately *after* the Doxygen comment and before the declaration.

### Issue Tracker Integration for Comments

When using Doxygen tags such as `@bug`, `@todo` or`@warning` within code comments, these **MUST** include a link to a corresponding item in the project's issue tracker (e.g., Jira, GitHub Issues). This ensures traceability and facilitates management of identified issues or future tasks.

**Example:**

```c
/**
 * @brief The function bar.
 * ...
 */
errcode_t bar(int a, int b, int c)
{
    /** More detailed description inside the code */
    /**
     * @todo Add contents to this function - See <a href="https://your-tracker.com/issues/TASK-123">TASK-123</a>
     */

    /// @warning Do not modify this!! - Refer to <a href="https://your-tracker.com/issues/WARN-789">WARN-789</a>
    /**
     * @bug This is a bug, has been raised as
     * <a href="https://your-tracker.com/issues/BUG-440">BUG-440</a>
     */
    return ERR_SUCCESS;
}
```

## Declarations

### Number Per Line

One declaration per line is recommended to encourage commenting.

```c
int level; /* indentation level */
int size;  /* size of table */
```

**Avoid:**

```c
int level, size; /* AVOID! */
```

Do not put different types on the same line:

```c
int foo, fooarray[SIZE]; /* WRONG! */
```

An alternative is to align a group of declarations with spaces:

```c
int          level;      /* indentation level */
int          size;       /* size of table */
Object       currentEntry; /* currently selected table entry */
```

### Initialisation

Initialise variables in a separate statement immediately after their declaration, unless the initial value depends on a prior computation.

### Placement

Place declarations at the beginning of blocks or immediately before first use.

Mixing declarations and executable statements mid-block should be avoided, except where doing so improves clarity or limits variable scope.

```c
void MyFunction(...)
{
    int int1;
    int1 = 0; /* beginning of block */

    if (condition)
    {
        int int2;
        int2 = 0; /* beginning of "if" block */
        // ...
    }
}
```

The only exception is for loop indices in C++, which can be declared within the `for` statement:

```c
for (int i = 0; i < MaxLoops; i++)
{
    // ...
}
```

Avoid local declarations that hide declarations at higher levels (e.g., declaring the same variable name in an inner block).

```c
int count;
// ...
int MyFunction(...)
{
    if (condition)
    {
        int count; /* AVOID! This hides the outer 'count' */
        // ...
    }
    // ...
}
```

### Function Declarations

When coding C functions, use the following formatting rules:

- All functions must be preceded by a documentation comment describing the function, its arguments, and return code(s).
- The opening brace `{` should appear at the beginning of the line following the declaration statement.
- The closing brace `}` should start a line by itself, aligned with the function's starting line.

```c
/**
 * @brief The function bar.
 * @details This function does something which is doing nothing. So this
 * text is totally senseless and you really do not need to read this,
 * because this text is basically saying nothing.
 * @note This optional text shall only show you, how such a "note"
 * section is looking. There is nothing which really needs your notice,
 * so you do not really need to read this section.
 * @param[in] a Description of parameter a.
 * @param[out] b Description of the parameter b.
 * @param[in,out] c Description of the parameter c.
 * @return The error return code of the function.
 * @retval ERR_SUCCESS The function is successfully executed
 * @retval ERR_FAILURE An error occurred
 */
errcode_t bar(int a, int b, int c)
{
    /** More detailed description inside the code */
    return ERR_SUCCESS;
}
```

## Statements ⚙️

### Simple Statements

Each line should contain at most one statement.

```c
argv++; /* Correct */
argc--; /* Correct */

argv++; argc--; /* AVOID! */
```

### Compound Statements

Compound statements are lists of statements enclosed in braces `{ statements }`.

- The enclosed statements should be indented one more level than the compound statement.
- The opening brace `{` should be on a line by itself, following the line that begins the compound statement, indented to the same level as that line.
- The closing brace `}` should begin a line by itself and be indented to the beginning of the compound statement.
- Always use braces around all statements, even single statements, when they are part of a control structure (e.g., `if-else`, `for`). This prevents accidental bugs when adding statements later.

### `return` Statements

A `return` statement with a value should not use parentheses unless they significantly improve clarity.

```c
return;
return MyDisk_size();
return (size ? size : defaultSize);
```

### `if`, `if-else`, `if else-if else` Statements

The `if-else` class of statements should have the following form:

```c
if (condition)
{
    statements;
}
else
{
    /* Do Nothing */
}

if (condition)
{
    statements;
}
else
{
    statements;
}

if (condition)
{
    statements;
}
else if (condition)
{
    statements;
}
else
{
    statements;
}
```

**Always use braces `{}` with `if` statements.** Avoid the error-prone form that omits braces:

```c
if (condition) /* AVOID! THIS OMITS THE BRACES {}! */
    statement;
```

### `for` Statements

A `for` statement should have the following form:

```c
for (initialization; condition; update)
{
    statements;
}
```

An empty `for` statement (where all work is done in the initialisation, condition, and update clauses) should have the following form:

```c
for (initialization; condition; update);
```

When using the comma operator in the initialisation or update clause of a `for` statement, avoid the complexity of using more than three variables. If necessary, use separate statements before the `for` loop (for initialisation) or at the end of the loop (for updates).

### `while` Statements

A `while` statement should have the following form:

```c
while (condition)
{
    statements;
}
```

An empty `while` statement should have the following form:

```c
while (condition);
```

### `do-while` Statements

A `do-while` statement should have the following form:

```c
do
{
    statements;
}
while (condition);
```

### `switch` Statements

A `switch` statement should have the following form:

```c
switch (condition)
{
    case ABC:
        statements;
        /* falls through */
    case DEF:
        statements;
        break;
    case XYZ:
        statements;
        break;
    default:
        statements;
        break;
}
```

- Every time a `case` falls through (does not include a `break` statement), add a comment where the `break` statement would normally be (e.g., `/* falls through */`).
- Every `switch` statement should include a `default` case. The `break` in the `default` case is redundant but prevents fall-through errors if the `default` is later changed to a specific case and a new `default` is introduced.

## White Space 

### Blank Lines

Blank lines improve readability by logically separating sections of code.

**Two blank lines should always be used:**

- Between sections of a source file.

**One blank line should always be used:**

- Between functions.
- Between local variable declarations in a block and its first statement.
- Before a block or single-line comment.
- Between logical sections inside a function to improve readability.

### Blank Spaces

Blank spaces should be used in the following circumstances:

- After commas in argument lists.
- All binary operators should be separated from their operands by spaces.
- Blank spaces should never separate unary operators (e.g., unary minus, increment `++`, decrement `--`) from their operands.

**Examples:**

```c
a += c + d;
a = (a + b) / (c * d);
while (d++ == s++) // Note: original had assignment, changed to equality for likely intent
{
    n++;
}
```

- Expressions in a `for` statement should be separated by blank spaces.

**Example:**

```c
for (expr1; expr2; expr3)
```

- Casts should be followed by a blank space.

**Examples:**

```c
MyFunction1((char) aNum, (double) x);
MyFunction2((int) (cp + 5), ((int) (i + 3) + 1));
```

## Keywords to Frequently Use

- The **`static`** keyword should be used to declare all functions and variables that do not need to be visible outside of the module in which they are declared.
  - All non-API functions and file-local data shall be declared `static` by default.
- The **`const`** keyword should be used whenever appropriate, including:
  - To declare variables that should not be changed after initialisation.
  - To define call-by-reference function parameters that should not be modified (e.g., `char const * param`).
  - To define fields in a `struct` or `union` that should not be modified (e.g., in a `struct` overlay for memory-mapped I/O peripheral registers).
  - As a strongly typed alternative to `#define` for numerical constants.
- The **`volatile`** keyword should be used whenever appropriate, including:
  - To declare a global variable accessible by any interrupt service routine.
  - To declare a global variable accessible by two or more threads.
  - To declare a pointer to a memory-mapped I/O peripheral register set (e.g., `timer_t volatile * const p_timer`).
  - To declare a delay loop counter.

## Naming Conventions

Naming conventions enhance programme readability.

### Externally Visible Functions

Should have a short prefix uniquely identifying the module, followed by an underscore, followed by the rest of the identifier. The rest of the identifier should consist of words, each beginning with a capital letter, with no underscores.

**Example:** `GAT_FindResource`

### Static Functions

Should follow the same convention as externally visible functions but do not require the module prefix.

### Variable Names

Should be short yet meaningful and mnemonic. Avoid one-character variable names except for temporary "throw-away" variables (e.g., `i, j, k, m, n` for integers; `c, d, e` for characters).

### `#defines`

Should be all uppercase.

### `typedef`s and Structures

Should have a short prefix, followed by an underscore, followed by the rest of the identifier. The rest of the identifier should consist of words, each beginning with a capital letter, with no underscores.

**Example:** `GAT_PropList`

### General Naming Practices

- Variables: All variables should be declared in a consistent case (`lowerCamelCase`)
  - Variables representing truth values (e.g., `TRUE`/`FALSE`) should be of `bool` type.
  - If a variable stores a unit, append the unit type using SI notation (e.g., `FooMs` for milliseconds, `CountS` for seconds).
  - Macros: all uppercase with underscores
  - Types: `Prefix_TypeName` with `_t` suffix  
- Functions: All functions should be declared in a consistent case (`PascalCase` for public APIs, `camelCase` for static functions).
  - Example: `ThisIsAFunctionName()`
  - All functions should return an appropriate success/error value where applicable.

    ```c
    int ThisFunction(); /* Returns a signed 8-bit value */
    err_t ThisFunction(); /* Returns an enumerated error code or positive value */
    ```

  - In the unlikely event that it's impossible to know if a function call succeeded, it may be `void`.

    ```c
    void ThisFunction();
    ```

## Programming Practices 🧑‍💻

### Adherence to Standards

- All code should adhere to the ISO C standards, aiming for the latest stable version (currently C17/C18). Where appropriate, consider adopting features from C23.
- We should aim for **MISRA C compliant code**, specifically **MISRA C:2012**, to ensure safety, security, and reliability, especially in embedded and real-time systems.

### Unions

Unions should generally be avoided. Strong justification must be provided for their use.

### `goto`

`goto` statements should generally be avoided. Strong justification must be provided for their use.

### `do-while`

`do-while` loops should generally be avoided. Strong justification must be provided for their use.

### Use `typedef` (and `enum`s) in preference to `#defines`

New types should be introduced via `typedef`s rather than `#define`s. This makes types visible in debuggers and allows for stronger type-checking by the compiler. Use `enum`s as appropriate.

### Use of `const` qualifier

Where possible, pointers should be passed using the `const` qualifier, especially for strings.

### Global and Static variables

Do not make any variable global or static without good reason. Access to module-level statics in other files can often be granted via a function call rather than making the variable global.

### Constants

Numerical constants (literals) should not be coded directly, except for -1, 0, and 1, or other numbers used in loop counters. Use named constants instead.

### Variable Assignments

- Avoid assigning several variables to the same value in a single statement. It reduces readability.

  ```c
  fchar = lchar = 'c'; /* AVOID! */
  ```

- Do not use the assignment operator in a place where it can be easily confused with the equality operator.

  ```c
  if (file = fopen(...)) /* AVOID! */
  {
      // ...
  }
  ```

  Should be written as:

  ```c
  if ((file = fopen(...)) != NULL)
  {
      // ...
  }
  ```

- Do not use embedded assignments to improve run-time performance; this is the compiler's job.

  ```c
  d = (a = b + c) + r; /* AVOID! */
  ```

  Should be written as:

  ```c
  a = b + c;
  d = a + r;
  ```

### Strong Typing

C is a weakly typed language. Be mindful of this and ensure variables are used with appropriate types to prevent issues where a variable of type A is passed to a function expecting type B.

### Miscellaneous Practices

#### Parentheses

Use parentheses liberally in expressions involving mixed operators to avoid operator precedence problems. Even if precedence seems clear to you, it might not be to others.

```c
if (a == b && c == d) /* AVOID! */
if ((a == b) && (c == d)) /* RIGHT */
```

#### Variable Types

All variables must take appropriate values for their type. For example, if a variable is a `bool` type, it must be set to `TRUE`/`FALSE`, not `0` or `1`.

```c
bool LinkUp = FALSE;
```

#### Returning Values

Try to make the structure of your programme match the intent.

```c
if (booleanExpression)
{
    return true;
}
else
{
    return false;
}
```

Should instead be written as:

```c
return booleanExpression;
```

Similarly:

```c
if (condition)
{
    return x;
}
return y;
```

Should be written as:

```c
return (condition ? x : y);
```

**Single Return Statement:** There should ideally be only one return statement in a function. Multiple returns can lead to confusion and are a frequent source of errors.

```c
if (foo)
{
    return a;
}
// ... lots of code ...
return b;
```

Should be written as:

```c
errcode_t retval; // Assuming errcode_t is the return type
if (foo)
{
    retval = a;
}
else
{
    // ... lots of code ...
    retval = b;
}
return retval;
```

#### Expressions before `?` in the Conditional Operator

If an expression containing a binary operator appears before the `?` in the ternary `?:` operator, it should be parenthesized.

```c
(x >= 0) ? x : -x;
```

#### Special Comments

- Use `@warning` in a comment to flag something that is "bogus but works."
- Use `@bug` in a comment to flag something that is "bogus and broken."

#### Pointers

All pointers passed to functions should be checked for validity. Static analysis tools can assist in identifying potential issues with pointer usage and validity.

## Static Analysis 🔍

Static analysis should be performed on all code. This should be done using dedicated static analysis tools that support **MISRA C:2012** compliance checking. These tools should be **integrated into the CI/CD pipeline** to automate the enforcement of coding standards and identify issues early in the development cycle.

## File Templates

### `.h` Template

```c
/**
 * @file template.h
 * @brief Brief description of contents of file.
 * @details Long description of the header file's purpose and contents.
 * @date date of last edit @todo to be auto added
 * @version CVS $Header$ field
 * @copyright
 * COPYRIGHT NOTICE: ® 20?? <Company Name> All rights reserved. <br>
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * @addtogroup name-of-library-or-application-or-module
 * @{
 */

#ifndef NAMEOFHEADERFILEINCAPITALS_H
#define NAMEOFHEADERFILEINCAPITALS_H 1

/*******************************************************************************
 * INCLUDES
 ******************************************************************************/

/*******************************************************************************
 * MACROS AND DEFINES
 ******************************************************************************/

/*******************************************************************************
 * TYPEDEFS
 ******************************************************************************/
typedef struct Books {
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
} book;

/*******************************************************************************
 * EXPORTED VARIABLES
 ******************************************************************************/

/********************************************************************************
 * GLOBAL FUNCTION PROTOTYPES
 ********************************************************************************/
errcode_t bar(int a, int b, int c);

#endif /* NAMEOFHEADERFILEINCAPITALS_H */

/** @} end of Doxygen group */
```

### `.c` Template

```c
/**
 * @file template.c
 * @brief Brief description of contents of file.
 * @details Long description of the file's purpose and functionality.
 * @date date of last edit @todo to be auto added
 * @version CVS $Header$ field
 * @copyright
 * COPYRIGHT NOTICE: ® 20?? <Company Name> All rights reserved. <br>
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * @addtogroup name-of-library-or-application-or-module
 * @{
 */

/*******************************************************************************
 * INCLUDES
 ******************************************************************************/

/*******************************************************************************
 * DEFINES
 ******************************************************************************/

/*******************************************************************************
 * LOCAL DATA TYPES
 ******************************************************************************/

/*******************************************************************************
 * LOCAL FUNCTION PROTOTYPES
 ******************************************************************************/

/*******************************************************************************
 * LOCAL DATA
 ******************************************************************************/

/*******************************************************************************
 * GLOBAL FUNCTIONS
 ******************************************************************************/
/**
 * @brief The function bar.
 * @details This function does something which is doing nothing. So this text
 * is totally senseless and you really do not need to read this,
 * because this text is basically saying nothing.
 * @note This optional text shall only show you, how such a "note" section
 * is looking. There is nothing which really needs your notice, so you
 * do not really need to read this section.
 * @param[in] a Description of parameter a.
 * @param[out] b Description of the parameter b.
 * @param[in,out] c Description of the parameter c.
 * @return The error return code of the function.
 * @retval ERR_SUCCESS The function is successfully executed
 * @retval ERR_FAILURE An error occurred
 */
errcode_t bar(int a, int b, int c)
{
    /** More detailed description inside the code */

    return ERR_SUCCESS;
}

/*******************************************************************************
 * LOCAL FUNCTIONS
 ******************************************************************************/

/** @} end of Doxygen group */
```
