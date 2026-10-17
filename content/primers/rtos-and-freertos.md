---
title: Real-time operating systems and FreeRTOS
---

# Real-time operating systems and FreeRTOS

A real-time operating system (RTOS) lets firmware be written as several independent tasks, each with a priority, and guarantees that the highest-priority task that is ready always runs. "Real time" means predictable, not fast: the point is a known worst-case response time.

FreeRTOS is the most widely used RTOS on microcontrollers. It is small (a few kilobytes of flash), MIT-licensed, ported to dozens of architectures, and maintained by Amazon Web Services since 2017. Zephyr, ThreadX (now Eclipse ThreadX) and the RTOS in Mbed and NuttX are common alternatives.

## Bare metal or RTOS

| Approach | Good for | Drawbacks |
| --- | --- | --- |
| Superloop with interrupts | Simple devices, one main activity, tight resources | Timing of each job depends on all the others; long jobs block everything |
| Cooperative scheduler | A few jobs that yield willingly | One misbehaving job still blocks the rest |
| Pre-emptive RTOS | Several activities with different deadlines; networking stacks | More RAM (a stack per task), more ways to get concurrency wrong |

[[CAPTION:Table]] Ways to structure firmware.

## Core concepts

- **Task**: a function with its own stack and priority that normally loops forever. A task is running, ready, blocked (waiting for something) or suspended.
- **Scheduler**: picks the highest-priority ready task. Equal-priority tasks can share time in turns.
- **Queue**: the main way tasks pass data. A task blocks on an empty queue without using CPU time.
- **Semaphore**: a signal or a count, often given from an interrupt to wake a task.
- **Mutex**: protects a shared resource. FreeRTOS mutexes use priority inheritance to limit priority inversion.
- **Event groups and task notifications**: lighter ways to signal one or more tasks.
- **Software timers**: run a callback after a delay or periodically.

```c
static QueueHandle_t readings;

static void sensor_task(void *arg)
{
    for (;;) {
        int16_t value = sensor_read();
        xQueueSend(readings, &value, 0);
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

static void report_task(void *arg)
{
    int16_t value;
    for (;;) {
        if (xQueueReceive(readings, &value, portMAX_DELAY) == pdPASS) {
            report(value);
        }
    }
}

void app_main(void)
{
    readings = xQueueCreate(16, sizeof(int16_t));
    xTaskCreate(sensor_task, "sensor", 256, NULL, 2, NULL);
    xTaskCreate(report_task, "report", 512, NULL, 1, NULL);
    vTaskStartScheduler();
}
```

[[CAPTION:Figure]] Two FreeRTOS tasks connected by a queue.

## Common mistakes

- **Priority inversion**: a low-priority task holds a mutex that a high-priority task needs, while a medium-priority task runs. Use mutexes (not binary semaphores) for shared resources and keep critical sections short.
- **Deadlock**: two tasks each hold a lock the other needs. Always take locks in the same order, or avoid sharing.
- **Stack overflow**: enable stack checking (`configCHECK_FOR_STACK_OVERFLOW`) during development and measure the high-water mark.
- **Doing work in interrupts**: keep interrupt handlers short and defer the work to a task with a semaphore or notification. Only call the `FromISR` versions of API functions inside interrupts.
- **Too many tasks**: each one costs a stack and adds interactions. Group related work; use [state machines](finite-state-machines.md) within a task.

## Where next

- [Interrupts and DMA](interrupts-and-dma.md) and [embedded systems design](embedded-systems-design.md) give the wider picture.
- The [FreeRTOS documentation](https://www.freertos.org/Documentation/00-Overview) is the reference, and the free book *Mastering the FreeRTOS Real Time Kernel* is a good tutorial.
