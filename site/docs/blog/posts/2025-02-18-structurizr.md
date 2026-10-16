---
date: 2025-02-18T09:12:00
authors:
  - markbac
categories:
  - Architecture as Code
slug: structurizr
---

# Structurizr: Bringing the C4 Model to Life in Code

When it comes to documenting and visualising software architecture, the C4 model offers a structured and effective approach. But what if you could automate the creation and maintenance of your C4 diagrams directly from the code? That’s where **Structurizr** comes in. In this post, we'll explore how Structurizr makes the C4 model even more powerful by allowing you to define, visualise, and update your architecture in code. That keeps it aligned with the actual system as it evolves.

<!-- more -->

As an architect, I’ve found that Structurizr is a game-changer for architecture diagrams. They are always up-to-date, easy to generate, and simple to integrate into the development process. Let’s dive into how Structurizr works and how you can use it to implement the C4 model in your projects.

## What is Structurizr?

**Structurizr** is a set of tools that allows you to define and visualise software architecture using the **C4 model**. It takes a code-first approach, meaning that you can define your system’s architecture in a simple, programmatic way, and then automatically generate high-quality diagrams. Structurizr supports the entire C4 hierarchy, from system context diagrams to code-level diagrams, enabling you to capture architecture at various levels of abstraction.

Structurizr is built around the idea that architecture documentation should be an integral part of your development process—just like the code itself. By storing architectural definitions in version control, you can ensure that your diagrams stay up-to-date with the evolving codebase. Changes to architecture are also visible to everyone on the team.

## Key Features of Structurizr

1. **Code-Based Definition**: Instead of manually creating diagrams in a graphical tool, you define your architecture using a domain-specific language (DSL) or programmatically using the Structurizr SDK. This allows your architecture to be stored as code, making it versionable, testable, and integrated into your CI/CD pipeline.
    
2. **Flexible Diagram Generation**: Once your architecture is defined in code, Structurizr generates high-quality, interactive diagrams at various levels of abstraction. You can generate context, container, component, and code-level diagrams, all tailored to your needs.
    
3. **Automated Updates**: By integrating Structurizr into your development workflow, your architecture diagrams are automatically updated whenever changes are made to the architecture code. This ensures that the diagrams always reflect the current state of your system.
    
4. **Cloud and On-Premise Options**: Structurizr offers both a cloud-based version and an on-premise version, giving you the flexibility to choose where to host your architecture data. The cloud version is a SaaS product, while the on-premise version can be self-hosted behind your corporate firewall.
    
5. **Collaboration-Friendly**: Since the architecture definitions are stored in version control, team members can collaborate on the architecture just like they would on any other part of the codebase. Pull requests and code reviews ensure that changes to the architecture are discussed and validated before being merged.
    

## How Structurizr Works with the C4 Model

To get started with Structurizr, you need to define your system’s architecture using the C4 model. Here’s a breakdown of how you would go about this:

### 1\. Define Your System Context

The first step is to define your system context. This is the highest level in the C4 model and shows how your system interacts with external users and systems. In Structurizr, you can define your system context diagram in code, specifying the system and the people, external systems, and other entities it interacts with.

Here’s an example of how you might define the system context in the Structurizr DSL:

```java
workspace {

    model {
        user = person "User" {
            description "A person who uses the system"
        }
        
        system = softwareSystem "MySystem" {
            description "A system that provides services to users"
        }
        
        user -> system "Uses"
    }

    views {
        systemContext system {
            include *
            autolayout lr
        }
    }
}

```

This code defines a system called “MySystem” and a user who interacts with it. It also generates a system context diagram that shows this relationship.

### 2\. Break Down the System into Containers

Next, you can define the **containers** within your system. A container is a deployable unit of your software (e.g., a web application, microservice, or database). In the code, you define the containers and how they interact with each other. Here’s an example:

```java
workspace {

    model {
        user = person "User" {
            description "A person who uses the system"
        }

        system = softwareSystem "MySystem" {
            description "A system that provides services to users"
            
            webApp = container "Web Application" {
                description "A web application that users interact with"
                technology "JavaScript, HTML, CSS"
            }
            
            apiService = container "API Service" {
                description "Handles business logic and data processing"
                technology "Java"
            }
            
            database = container "Database" {
                description "Stores user and order data"
                technology "MySQL"
            }
            
            user -> webApp "Uses"
            webApp -> apiService "Calls"
            apiService -> database "Reads from and writes to"
        }
    }

    views {
        container system {
            include *
            autolayout lr
        }
    }
}

```

In this example, the system is broken down into three containers: a web application, an API service, and a database. The relationships between these containers are also defined, and Structurizr automatically generates a container diagram showing how they interact.

### 3\. Define Components Within Each Container

After defining the containers, you can drill down further and define the **components** within each container. Components are the building blocks of a container and represent a piece of functionality, like a service or a data access layer.

Here’s how you might define the components of the API service container:

```java
workspace {

    model {
        apiService = container "API Service" {
            description "Handles business logic and data processing"
            technology "Java"
            
            userService = component "User Service" {
                description "Manages user-related operations"
            }
            
            orderService = component "Order Service" {
                description "Handles order-related operations"
            }
            
            apiService -> userService "Calls"
            apiService -> orderService "Calls"
        }
    }

    views {
        component apiService {
            include *
            autolayout lr
        }
    }
}

```

This code defines two components inside the **API Service** container: the **User Service** and the **Order Service**, and shows the relationships between them. Structurizr generates a component diagram to reflect this structure.

### 4\. Visualising Code-Level Detail (Optional)

If necessary, you can also dive into the **code-level** detail, defining classes, methods, or functions that make up each component. This is usually done using a UML-style class diagram or sequence diagrams. This level of detail can be valuable for developers when they need to understand the inner workings of a component.

## Benefits of Using Structurizr

1. **Automation**: Structurizr makes it easy to automate architecture diagram creation. As your system evolves, so do your architecture diagrams. With Structurizr integrated into your CI/CD pipeline, you can ensure that your diagrams always reflect the latest changes.
    
2. **Version Control**: Since your architecture definitions are stored in code, they can be managed using version control systems like Git. This allows you to track changes, collaborate effectively, and revert to previous versions if needed.
    
3. **Collaboration**: Structurizr facilitates collaboration by making the architecture definitions accessible to all team members. Developers can suggest changes, architects can review them, and everyone can have a clear, up-to-date view of the system’s architecture.
    
4. **Clarity**: By integrating the C4 model into your development workflow, you make architecture diagrams an integral part of the system design process. This ensures that the architecture is always clear and understandable, even as the system evolves.
    

## Conclusion

Structurizr is an excellent tool for bringing the **C4 model** to life in a code-driven, automated way. It helps you create architecture diagrams that are always in sync with the codebase, making it easier to communicate and maintain your software architecture. Whether you're working on a small application or a large, complex system, Structurizr enables you to document and visualise your architecture with clarity and precision.

In the next post, we'll explore common **architecture anti-patterns** that can arise when using the C4 model and Structurizr, and how to avoid them. Stay tuned!
