# oop-principles-in-python
# Line
OOP PRinciples refresh / practice

# 🐍 Python OOP Concepts

## ✅ Basics

- **Classes & Objects**: How to define classes and create instances.
- **Attributes & Methods**: Use of instance data and behavior.
- **Encapsulation**: Protect internal data using `_` and `__`, and control access with `@property`.
- **Inheritance**: Subclasses reuse logic from parent classes.
- **Polymorphism**: Objects with the same method name can be used interchangeably.
- **Duck Typing**: “If it quacks like a duck…” — Python doesn't care about type, only behavior.
- **MRO (Method Resolution Order)**: Python looks up methods in a specific order with multiple inheritance.

---

## ✅ `@property`, Getter, Setter

- `@property` lets you treat method calls like attributes.
- Used for **validation**, **encapsulation**, and **computed values**.
- You saw both **classic** (`get_...`, `set_...`) and **modern** (`@property`) styles.

---

## ✅ Type Checking Tools

- `isinstance(obj, Class)` → Checks if an object is an instance of a class.
- `issubclass(ClassA, ClassB)` → Checks if a class inherits from another.

---

# 🧱 SOLID Principles (with code examples)

### **S – Single Responsibility**

- One class = one job (e.g. `Order` vs `Payment`)

### **O – Open/Closed**

- Extend behavior (e.g. add `BitcoinPayment`) without modifying existing code

### **L – Liskov Substitution**

- Subclasses must behave like their base class (real-world shape example)

### **I – Interface Segregation**

- Use small, focused interfaces (e.g. `Scanner`, `Printer`, etc. instead of one giant `Machine`)

### **D – Dependency Inversion**

- High-level code (`Order`) depends on an abstraction (`PaymentMethod`), not a specific payment class
