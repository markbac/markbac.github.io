---
title: Designing LwM2M objects and resources
---

# Designing LwM2M objects and resources

This guide covers how to design new LwM2M objects, how to group or split data items, and how to choose resource access types (R, W, RW, or Execute).\
It works for: sensors, actuators, gateways, industrial controllers, wearables, home devices, vehicles, etc.

## What an LwM2M Object Is

An LwM2M *object* is a structured container used to model a feature, capability, or function of an IoT device.\
It defines a standard way for a server and client to exchange configuration, commands, and data.

Objects are the building blocks of the LwM2M data model.

### How an Object Is Structured

An object contains:

- Object ID\
  A unique numeric identifier (for example, 3 for Device, 5 for Firmware Update). Standard object IDs are defined by OMA, but manufacturers can also use their own custom object IDs for device-specific functionality.
- Object Instances\
  One object can have **one instance** or **many instances**.\
  Each instance represents one occurrence of the object’s concept.
- Resources\
  Each instance contains a set of **resources**.\
  Resources are the individual data points, settings, or actions the server interacts with.

A resource can be:

- a configuration value (write),
- a measurement (read),
- a command (execute),
- or a value that both sides read and write (RW).

### Basic Hierarchy

LwM2M addresses data using a simple three-level path:

```swift
/ObjectID/InstanceID/ResourceID
```

A resource is always accessed through this path.

### Examples

```pgsql
/1000/0/1  →   Read a status value  
/1000/0/2  →   Update configuration  
/1000/0/3  →   Execute an action  
```

### Single-instance vs Multi-instance Objects

Objects may support **one** instance or **multiple**:

#### Single-instance objects

Used when the device only ever has one of something.

Structure:

```swift
/ObjectID/0/ResourceID
```

There will only ever be instance **0**.

#### Multi-instance objects

Used when a device has a list of similar items or entries.

Structure:

```bash
/ObjectID/0/...  
/ObjectID/1/...  
/ObjectID/2/...
```

Each instance represents one item, record, channel, or entity.

### Resource Types

Each resource has:

- ID – numeric identifier
- Name – descriptive field name
- Type - data representation used by the resource
  - Integer Whole numbers, often used for counters, IDs, thresholds, flags.
  - String: human-readable text or structured text fields.
  - Boolean True/false states.
  - Opaque Raw binary data, uninterpreted by LwM2M (keys, payloads, custom formats).
  - Time Timestamp in seconds since Unix epoch (signed integer).
  - ObjLnk A reference to another object instance in the form `<ObjectID>:<InstanceID>`.
- Access Mode – how the server interacts with the resource
  - R (Read) The server can read the value; the device owns and updates it.
  - W (Write) The server sets the value; used for configuration or parameters.
  - RW (Read/Write) Both sides can access the value; use only when the value is legitimately shared.
  - E (Execute) Triggers an action with side effects (commands, operations, one-shot behaviour).
- Mandatory/Optional flag
- Description – what it means and how it behaves

The object definition lists all resources available for any instance.

### Why Object Design Matters

A well-designed object:
- is clear and unambiguous
- cleanly separates configuration, status, and commands
- is secure by design
- is easy for clients and servers to implement
- supports versioning without redesigning the protocol
- avoids coupling unrelated behaviours into a single object

Good object modelling ensures predictable behaviour across millions of devices and years of lifecycle.

## Define the purpose of the object

Every object should have a **single, clear purpose**.\
A simple method:

**“This object exists to…”**

Examples of good-purpose statements (generic):

- “…configure communication behaviour.”
- “…report sensor measurements.”
- “…control a device function.”
- “…manage a firmware update operation.”

If the purpose needs multiple “and”s, it’s too broad.

## Group data by lifecycle and behaviour

A clean LwM2M model groups resources that naturally belong together.\
Ask:

### Do these items change together?

If yes, keep them in the same object.

### Do they change independently?

If yes, they likely belong in different objects.

You’re aiming to keep:

- long-lived configuration separate from
- real-time measurements, and separate again from
- operational commands, and separate again from
- transaction-like actions.

Grouping by lifecycle reduces coupling and keeps versioning straightforward.

## Identify resource access types (R, W, RW, Execute)

Use simple rules:

### Read (R)

Values the device exposes but the server should not modify.\
Typical patterns:

- Status
- Sensor readings
- Identity information
- Diagnostics

### Write (W)

Values the server can set, normally configuration or modes.\
Patterns:

- Thresholds
- Timers
- Limits
- Operational parameters

### Execute (E)

An operation with side effects.\
Patterns:

- Trigger a function
- Reset something
- Start/stop an operation
- Load or apply something

### Read–Write (RW)

Only used when both sides legitimately control a value.

RW is valid but should be used sparingly because it blurs ownership.

## Questions to ask when choosing access types

A small set of questions helps you classify properly:

### Does changing this value cause behaviour?

If yes, it’s usually Execute, not Write.

### Is the value permanent or semi-permanent?

If yes, Write (configuration).\
If no, maybe it’s status (Read).

### Does the device own the value?

If the device produces the value and the server only observes it -> Read.

### Does the server own the value?

If the server controls the value → Write.

### Do both need to influence it?

If genuinely yes-> RW.

### Is it a one-off operation?

If so -> Execute.

## Avoid mixing configuration, state, and commands

This is the biggest design mistake people make.

### Keep these separate

- Configuration
- Current operational status
- Commands / actions
- Historical/event data

Each has its own cadence and behaviour.

If you mix them inside one object:

- Access rights become messy
- Version control becomes awkward
- You risk unintended updates or accidental overwrites
- Servers become more complex

Split objects whenever these concerns diverge.

## Single-instance vs multi-instance

Ask: **“Could there ever be more than one of these?”**

### Single-instance

Use when only one set of data makes sense:

- Device identity
- Core configuration
- Communication parameters

### Multi-instance

Use when items form a list or history:

- Sensors of the same type
- Logs
- Events
- Tasks
- Rules/schedules
- Per-channel configurations

Watching this early prevents awkward redesigns later.

## Object and resource naming

Keep naming:

- Neutral
- Descriptive
- Domain-independent
- Easy to understand at a glance

Good names simplify onboarding and maintenance.

Avoid:

- Abbreviations that need a dictionary
- Vendor-specific naming inside generic objects
- Jargon that ties the object to one use case

## Respect security boundaries

Security is often the reason to split objects.

Keep separate:

- Sensitive parameters
- Credentials
- Commands that produce physical or financial effects
- Logs that may contain sensitive data

If different security levels apply, you need separate objects.

## Versioning considerations

Objects tend to live for years.\
Design to make versioning manageable:

- Keep objects narrow in scope
- Don’t overload a single object with too many responsibilities
- When behaviour changes meaningfully, version the object rather than hack new semantics into an existing resource
- Use optional resources for new features if backwards compatibility matters

## Decision checklist (simple “flowchart in words”)

:::mermaid
flowchart TD

    Start([Start Object Design]) --> CheckPurpose

    CheckPurpose{Is the object's purpose clear?} 
    CheckPurpose -->|Yes| ClassifyData
    CheckPurpose -->|No| SplitForPurpose[Split the object based on purpose] --> ClassifyData

    ClassifyData{Are data items config, status, or operations?} --> CheckLifecycle

    CheckLifecycle{Do any items differ in lifecycle, update rate, or ownership?}
    CheckLifecycle -->|Yes| SplitForLifecycle[Split objects based on lifecycle differences] --> CheckSecurity
    CheckLifecycle -->|No| CheckSecurity

    CheckSecurity{Do any items require separate security?}
    CheckSecurity -->|Yes| SplitForSecurity[Split objects based on security boundaries] --> DetermineOwnership
    CheckSecurity -->|No| DetermineOwnership

    DetermineOwnership{Who owns each resource?}
    DetermineOwnership --> DeviceRead[Device-Owned → Read]
    DetermineOwnership --> ServerWrite[Server-Owned → Write]
    DetermineOwnership --> SharedRW["Shared → Read/Write (only when justified)"]

    DeviceRead --> CheckForAction
    ServerWrite --> CheckForAction
    SharedRW --> CheckForAction

    CheckForAction{Is the resource an action?}
    CheckForAction -->|Yes| UseExecute[Use Execute resource]
    CheckForAction -->|No| CheckHistory

    CheckHistory{Does this require historical entries?}
    CheckHistory -->|Yes| UseMultiInstance[Use a multi-instance object]
    CheckHistory -->|No| End([End Object Design])
:::

## Recommended generic object structure template

A clean structure you can reuse across projects:

1. Object Purpose
1. High-level Description
1. Device Role (producer/consumer)
1. Resource Table:
   - ID
   - Name
   - Type (string, int, boolean, opaque, time, objlink)
   - Access (R, W, RW, E)
   - Mandatory/optional
   - Description
1. Security Notes
1. Instance Model:
   - Single-instance or multi-instance
1. Expected Client Behaviour
1. Expected Server Behaviour
1. Versioning Notes

This ensures consistent modelling across teams.
