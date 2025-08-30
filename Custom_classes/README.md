Question:

You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over,
we first get its length in the format: {'length': <VALUE_OF_LENGTH>}
followed by the width {width: <VALUE_OF_WIDTH>}

Algorithm:

### **Algorithm for Rectangle Class**

**Step 1: Define the class**  
- Creating a class named **`Rectangle`**.

**Step 2: Initialize the object**  
- Use the **`__init__`** method to accept **`length`** and **`width`** as integers.  
- Store the values in instance variables: **`self.length`**, **`self.width`**.

**Step 3: Make the class iterable**  
- Define the **`__iter__`** method in the class.  
- Yield dictionary keys in order:  
  - `yield {'length': self.length}`  
  - `yield {'width': self.width}`

**Step 4: Create an object**  
- Instantiate the class with specific values for length and width:  
  ```python
  rect = Rectangle(10, 5)


OUTPUT: 

![Rectangle Output](https://raw.githubusercontent.com/devi1262005/AccuKnox_Django-Trainee/ffe044a100481adedbe971d3e6e1f2ce3c58c29c/images/Output-Rect.png)
