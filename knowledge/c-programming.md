# C/C++ Programming

- [C/C++ Programming](#cc-programming)
  - [Memory allocation stack vs heap](#memory-allocation-stack-vs-heap)
  - [The Heap](#the-heap)
  - [preemptive vs non-preemptive](#preemptive-vs-non-preemptive)
    - [difference of malloc and calloc](#difference-of-malloc-and-calloc)

## Memory allocation stack vs heap

Basic structure:

1. text/instruction (machine code)
2. Global and static variables (non)initialized data
3. Stack: parameters and local variables
4. Heap: dynamic allocated memories

The advantage of using the stack to store variables, is that memory is managed for you. You don't have to allocate memory by hand, or free it once you don't need it any more. What's more, because the CPU organizes stack memory so efficiently, reading from and writing to stack variables is very fast.

A key to understanding the stack is the notion that when a function exits, all of its variables are popped off of the stack (and hence lost forever). Thus stack variables are local in nature. This is related to a concept we saw earlier known as variable scope, or local vs global variables. A common bug in C programming is attempting to access a variable that was created on the stack inside some function, from a place in your program outside of that function (i.e. after that function has exited).

Another feature of the stack to keep in mind, is that there is a limit (varies with OS) on the size of variables that can be stored on the stack. This is not the case for variables allocated on the heap.

To summarize the stack:

* the stack grows and shrinks as functions push and pop local variables
* there is no need to manage the memory yourself, variables are allocated and freed automatically
* the stack has size limits
* stack variables only exist while the function that created them, is running

## The Heap

The heap is a region of your computer's memory that is not managed automatically for you, and is not as tightly managed by the CPU. It is a more free-floating region of memory (and is larger). To allocate memory on the heap, you must use malloc() or calloc(), and use free() to release the memory.

Note that heap allocation must be a continuous memory block. So sometimes, it needs to clean up to coalesce for large objects.

## preemptive vs non-preemptive

1. Preemptive Scheduling:
Preemptive scheduling is used when a process switches from running state to ready state or from waiting state to ready state. The resources (mainly CPU cycles) are allocated to the process for the limited amount of time and then is taken away, and the process is again placed back in the ready queue if that process still has CPU burst time remaining. That process stays in ready queue till it gets next chance to execute. 

Algorithms based on preemptive scheduling are: Round Robin (RR),Shortest Remaining Time First (SRTF), Priority (preemptive version), etc. 

1. Non-Preemptive Scheduling:
Non-preemptive Scheduling is used when a process terminates, or a process switches from running to waiting state. In this scheduling, once the resources (CPU cycles) is allocated to a process, the process holds the CPU till it gets terminated or it reaches a waiting state. In case of non-preemptive scheduling does not interrupt a process running CPU in middle of the execution. Instead, it waits till the process complete its CPU burst time and then it can allocate the CPU to another process. 

Algorithms based on non-preemptive scheduling are: Shortest Job First (SJF basically non preemptive) and Priority (non preemptive version), etc.

- select is for block reading socket
- ioctl is blocking mode
- fcntl is for non-blocking mode (REQARG set 0, 1 is blocking mode)

### difference of malloc and calloc

- calloc 和malloc 区别 : malloc(size), calloc(num, size) allocates num*size, and initializes to 0

###########

- memory management, stack, heap,）给了我一段简单C++ 代码 问计算机内部内存发生了什么。 建议大家好好复习一下关于pointer,  reference, object 这种东西。
