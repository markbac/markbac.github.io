---
title: Design patterns
---

# Design patterns

A design pattern is a named, reusable solution to a problem that keeps coming up in software design. The name is half the value: saying "put an adapter in front of it" communicates a whole design in four words.

The best-known catalogue is *Design Patterns: Elements of Reusable Object-Oriented Software* (1994) by Gamma, Helm, Johnson and Vlissides, the "Gang of Four" (GoF). It describes 23 patterns in three groups.

## Creational patterns

These control how objects are made, so the code that uses an object does not depend on exactly which class it gets.

| Pattern | Use it when |
| --- | --- |
| Factory method | A class needs to create objects but subclasses should decide which kind |
| Abstract factory | You need families of related objects that must match (for example, one per hardware board) |
| Builder | An object has many optional parts and a constructor would be unreadable |
| Prototype | Copying an existing object is cheaper or simpler than building one |
| Singleton | There must be exactly one instance. Use sparingly: it is global state with a nicer name |

[[CAPTION:Table]] The creational patterns.

## Structural patterns

These are about composing classes and objects into larger structures.

| Pattern | Use it when |
| --- | --- |
| Adapter | You need to use a class whose interface does not match what your code expects |
| Bridge | Both an abstraction and its implementation need to vary independently |
| Composite | Clients should treat a single item and a group of items the same way (trees) |
| Decorator | You want to add behaviour to an object without subclassing it |
| Facade | A subsystem is complicated and most callers need a simple front door |
| Flyweight | You have very many similar objects and need to share their common state |
| Proxy | Access to an object needs control: lazy loading, caching, remote calls, permissions |

[[CAPTION:Table]] The structural patterns.

## Behavioural patterns

These are about how objects share responsibility and communicate.

| Pattern | Use it when |
| --- | --- |
| Chain of responsibility | Several handlers might deal with a request and the sender should not care which |
| Command | You want to treat a request as an object: queue it, log it, undo it |
| Interpreter | You have a small language to evaluate |
| Iterator | Clients need to walk a collection without knowing its structure |
| Mediator | Many objects talk to each other and the wiring has become a tangle |
| Memento | You need to save and restore an object's state without exposing its internals |
| Observer | Other objects must be told when something changes (the basis of event handling) |
| State | An object's behaviour depends on its state and the `if` statements are spreading |
| Strategy | You need to swap one algorithm for another at run time |
| Template method | The steps of an algorithm are fixed but some steps vary |
| Visitor | You need to add operations to a stable set of classes without changing them |

[[CAPTION:Table]] The behavioural patterns.

## A small example

The strategy pattern in Python, choosing how to compress a log file:

```python
from typing import Protocol
import gzip, lzma

class Compressor(Protocol):
    def compress(self, data: bytes) -> bytes: ...

class Gzip:
    def compress(self, data: bytes) -> bytes:
        return gzip.compress(data)

class Xz:
    def compress(self, data: bytes) -> bytes:
        return lzma.compress(data)

def archive(data: bytes, compressor: Compressor) -> bytes:
    return compressor.compress(data)
```

[[CAPTION:Figure]] The strategy pattern: the caller picks the algorithm.

## Using patterns well

- Start from the problem, not the pattern. If you cannot name the force a pattern resolves, you probably do not need it.
- Modern languages absorb some patterns. First-class functions make many strategies and commands a plain function; iterators are built into most languages.
- Patterns in embedded C look different (function pointer tables, static allocation) but the ideas carry over.
- Overuse is its own [anti-pattern](anti-patterns.md): an abstract factory for one product is just extra code.

## Where next

- [Design principles](design-principles.md) explains the ideas the patterns rest on.
- Architectural patterns work at a larger scale: see [hexagonal architecture](hexagonal-architecture.md) and [event-driven architecture](event-driven-architecture.md).
- [refactoring.guru](https://refactoring.guru/design-patterns) has a clear illustrated description of every GoF pattern.
