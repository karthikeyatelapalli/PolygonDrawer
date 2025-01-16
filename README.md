# Polygon Drawer with Turtle Module

This Python program uses the `turtle` module to draw polygons based on user-defined dimensions. It calculates the required angles and draws polygons with 3 to 12 sides. After drawing, the program labels the polygon based on its number of sides.

---

## **Features**
1. **Interactive User Input**:
   - Prompts the user to input:
     - The number of sides (3–12).
     - The length of each side (50–250).
   - Input is handled via the `turtle.numinput()` method, allowing default, minimum, and maximum values.

2. **Polygon Drawing**:
   - Dynamically calculates the angles required to draw the polygon.
   - Uses the `turtle` module to draw the polygon graphically.

3. **Polygon Labeling**:
   - Labels the polygon with its appropriate name (e.g., Triangle, Square, Hexagon) using the `turtle.write()` method.

---

## **How to Run**

### **Requirements**
- Python 3.x
- Turtle graphics module (part of Python's standard library).

### **Steps**
1. Save the program as `polygon_drawer.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the program.
4. Run the program:
   ```bash
   python3 polygon_drawer.py
