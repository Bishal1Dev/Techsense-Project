# 🔄 Unit Converter

A full-stack web application for converting values across 8 categories of units — Length, Weight, Temperature, Volume, Storage (data), Time, Speed, and Currency. Built with a Flask backend, a clean HTML/CSS interface, and interactive JavaScript using a responsive single-page design.

---

## 1. Abstract / Executive Summary

The **Unit Converter** is a Flask-powered web application that lets users instantly convert a value between any two units within a chosen category. The backend performs all mathematical conversions in Python, the frontend provides a modern glassmorphism-style interface, and JavaScript handles user interactions, live unit selection, one-click swapping, copying results to the clipboard, and a local conversion history. This document explains the problem it solves, the technology behind it, and provides a **full, line-by-line walkthrough of every file in the project**.

---

## 2. Introduction / Problem

### Why does this project exist?

Unit conversion is a universal need. Students, engineers, travelers, and programmers frequently need to translate between different measurement systems — for example, miles to kilometers, pounds to kilograms, or gigabytes to megabytes. Doing these by hand is slow and error-prone, and remembering the conversion factors for dozens of units across many categories is impractical.

### What problem does it solve?

This project solves that problem by providing:

- A **fast, accurate, and simple** interface for common and specialized conversions.
- Support for **8 unit categories** with multiple units each.
- A **visually clean, mobile-friendly** single-page interface.
- **Immediate feedback** with a live result, copy-to-clipboard, swap functionality, and recent history.

---

## 3. Background

### What the reader needs to know

To fully understand this project, you should be familiar with:

- **Python** — the backend logic and the Flask web framework.
- **Flask** — a lightweight micro web framework that maps URLs to Python functions and renders HTML templates.
- **HTML / CSS / JavaScript** — the structure, styling, and interactivity of the frontend.
- **REST and JSON** — the frontend communicates with the backend via a `POST` endpoint using JSON payloads.
- **The conversion factor technique** — most categories are converted by normalizing to a **base unit**. Each unit has a factor relative to that base. To convert, you multiply the input by the *from* factor, then divide by the *to* factor.

### Project structure

```
Python-Project/
│
├── app.py                  # Flask server + API endpoint
├── conversions.py          # The conversion engine (all math)
├── requirements.txt        # Python dependencies (only Flask)
├── templates/
│   └── index.html          # The frontend page + unit data
└── static/
    ├── style.css           # All styling/theming
    └── script.js           # Frontend interactivity & API calls
```

---

## 4. Methodology / Approach

### How was it built?

The application follows a clean **client-server model**:

1. **Frontend (HTML/CSS/JS)** collects the user's category, value, "from" unit, and "to" unit.
2. The browser sends this data as a **JSON POST request** to the Flask endpoint `/convert`.
3. **Flask** parses the request and hands the data to the conversion engine in `conversions.py`.
4. The **conversion engine** computes the result using lookup tables and mathematical formulas.
5. Flask returns the result as **JSON**.
6. JavaScript displays the result, stores it in history, and offers copy functionality.

### Key design decisions

| Decision | Reasoning |
|----------|-----------|
| **Base-unit normalization** | Reduces the number of stored ratios. Only one factor per unit is needed instead of pair-wise factors. |
| **Dictionaries as lookup tables** | Python dicts are fast and readable — mapping unit name → conversion factor. |
| **Separate `conversions.py`** | Keeps business logic isolated from the web layer, making it reusable and testable. |
| **JSON over form-data** | Modern, structured, and easy to parse on both sides. |
| **Rounded results** | Prevents long floating-point trails; standard conversions round to 6 decimal places, temperatures to 2. |
| **Temperature handled specially** | Because Celsius/Fahrenheit/Kelvin are *offset-based*, they cannot use simple multiplication — a dedicated function is required. |

---

## 5. Results / Findings

### What was built

This project successfully delivers a functional, polished unit converter with:

- **8 categories**, each with its own set of units (see table below).
- **Live result** display after pressing Convert.
- **Swap button** that exchanges the "from" and "to" selections instantly.
- **Copy to clipboard** button with visual confirmation.
- **Recent history** storing the last 10 conversions in the current session.
- **Enter key support** to trigger conversion from the value input.
- **Validation & error handling** for invalid numbers and unsupported conversions.
- **Responsive layout** that adapts to mobile screens.

### Supported categories & units

| Category | Units |
|----------|-------|
| **Length** | Meter, Kilometer, Centimeter, Millimeter, Foot, Inch, Yard, Mile |
| **Weight** | Kilogram, Gram, Milligram, Pound, Ounce, Ton |
| **Temperature** | Celsius, Fahrenheit, Kelvin |
| **Volume** | Liter, Milliliter, Gallon, Cup |
| **Storage** | Byte, KB, MB, GB, TB |
| **Time** | Second, Minute, Hour, Day |
| **Speed** | m/s, km/h, mph |
| **Currency** | USD, NPR, EUR, GBP |

### Example conversions after running the app

```
Input:  100 Meter   →  to Kilometer
Result: 0.1 Kilometer

Input:  32 Fahrenheit → to Celsius
Result: 0 °C

Input:  1 Gigabyte  →  to Megabyte
Result: 1024 MB
```

---

## 6. Discussion

### What does it mean? How does it compare to expectations?

The project meets its goals of being **fast, accurate, and simple** as advertised in the UI subtitle. The base-unit normalization approach is efficient: adding a new unit to any category requires only one new entry in the lookup table, not dozens of pair relationships.

Temperature conversion stands out as the correct and necessary exception — using simple multiplication on temperatures would be mathematically wrong, so the dedicated `temperature()` function handles offset conversions with explicit formulas for all six pair combinations.

### Notes & possible observations

- **Currency rates are static** (e.g., `1 USD = 138 NPR`). In production, these values would ideally update from a live API.
- **History is session-only.**
- The rounding to 6 decimals is a deliberate trade-off between readability and precision.

---

## 7. Conclusion

The **Unit Converter** is a complete, well-architected full-stack example that demonstrates how a Flask backend, a Python conversion engine, and an interactive HTML/CSS/JS frontend can be combined into a small but genuinely useful tool. Its clean separation of concerns makes it easy to extend, and its base-unit table design means adding units is trivial. It serves as both a practical everyday tool and a solid learning reference for building Flask + REST + JSON web applications.

### Key takeaways

- Separation of backend logic (`conversions.py`) from web handling (`app.py`) improves clarity and maintainability.
- The base-unit factor table is a scalable, low-maintenance way to define conversion ratios.
- Some conversions (temperature) require formulas rather than simple ratios.
- A well-layered frontend keeps the interface responsive and intuitive.

---

## 8. Installation

Assume the reader knows nothing. Follow these steps exactly.

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/) installed on your machine.
- (Recommended) A virtual environment.

### Step-by-step

```bash
# 1. Clone 

git clone https://github.com/#Bishal Lamichhane
#Arpit Kharel
#Dipak Yadav
#Bibek Shahi1Dev/Techsense-Project.git

#navigate into the project folder
cd Python-Project

# 2. (Recommended) Create and activate a virtual environment
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# 3. Install the required dependency (Flask)
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open your browser and visit:
#    http://127.0.0.1:5000
```

> 💡 If the above commands don't work on Windows, try `py -m venv venv` and `py app.py`.

---

## 9. Usage

Once the server is running, use the interface like this:

1. Choose a **Category** (e.g., Length).
2. Enter a numeric **Value** in the input field.
3. Select the **From** unit (e.g., Meter).
4. Select the **To** unit (e.g., Kilometer).
5. Click **Convert** (or press **Enter**).
6. Read the result, then optionally click **Copy Result** to copy it to your clipboard.

```
$ python app.py
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

Browser interaction:
Choose Category: Length
Enter Value:    100
From:           Meter
To:             Kilometer
Result:         100 Meter = 0.1 Kilometer
```

Use the **⇄ Swap** button to quickly reverse the from/to selection, and check the **Recent Conversions** panel for your last 10 conversions this session.

---

## 10. Full Code Explanation

### 10.1 `conversions.py` — The Conversion Engine

This file contains all the mathematical logic and requires **no external dependencies**. It is pure Python.

#### Lookup tables (dictionaries)

Each dictionary maps a **unit name** to its **conversion factor** relative to the first (base) unit.

```python
length = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Yard": 0.9144,
    "Mile": 1609.344
}
```

**Why this works:** The number stored is how many *of the base unit* one of this unit equals. For example, `1 Kilometer = 1000 Meters`, so its factor is `1000`. `1 Foot = 0.3048 Meters`, so its factor is `0.3048`.

The same pattern is used for **weight**, **volume**, **storage**, **time**, **speed**, and **currency**:

```python
weight = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Milligram": 0.000001,
    "Pound": 0.45359237,
    "Ounce": 0.0283495,
    "Ton": 1000
}

volume = {
    "Liter": 1,
    "Milliliter": 0.001,
    "Gallon": 3.78541,
    "Cup": 0.236588
}

storage = {
    "Byte": 1,
    "KB": 1024,
    "MB": 1024**2,   # 1024 * 1024
    "GB": 1024**3,
    "TB": 1024**4
}

time = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400
}

speed = {
    "m/s": 1,
    "km/h": 0.277778,
    "mph": 0.44704
}

currency = {
    "USD": 1,
    "NPR": 138,
    "EUR": 1.17,
    "GBP": 1.34
}
```

#### `normal_convert()` — Generic converter

```python
def normal_convert(table, from_unit, to_unit, value):
    base = value * table[from_unit]
    return round(base / table[to_unit], 6)
```

**How it works:**
1. `value * table[from_unit]` converts the input value into the **base unit**.
   - Example: `100 Meters → 100 * 1 = 100` base units.
2. `base / table[to_unit]` converts from base units into the desired **to-unit**.
   - Example: `100 / 1000 = 0.1 Kilometers`.
3. `round(..., 6)` limits the result to 6 decimal places for clean output.

This single function handles **any** of the 7 ratio-based categories by passing the appropriate table.

#### `temperature()` — Specialized converter

```python
def temperature(from_unit, to_unit, value):
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return round(value * 9 / 5 + 32, 2)
        if to_unit == "Kelvin":
            return round(value + 273.15, 2)

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return round((value - 32) * 5 / 9, 2)
        if to_unit == "Kelvin":
            return round((value - 32) * 5 / 9 + 273.15, 2)

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return round(value - 273.15, 2)
        if to_unit == "Fahrenheit":
            return round((value - 273.15) * 9 / 5 + 32, 2)

    raise Exception("Temperature conversion not supported.")
```

**Why temperatures are special:** Unlike the other categories, temperature scales have offsets (the zero-point differs). You cannot just multiply by a factor — you must apply specific formulas. This function uses the standard formulas:

- **C → F:** `(C × 9/5) + 32`
- **C → K:** `C + 273.15`
- **F → C:** `(F − 32) × 5/9`
- **F → K:** `(F − 32) × 5/9 + 273.15`
- **K → C:** `K − 273.15`
- **K → F:** `(K − 273.15) × 9/5 + 32`

The `if from_unit == to_unit: return value` guard avoids unnecessary work. If an unsupported pair is requested, it raises an exception (which the Flask layer catches and reports to the user).

#### `convert()` — The dispatch function

```python
def convert(category, from_unit, to_unit, value):
    if category == "Length":
        return normal_convert(length, from_unit, to_unit, value)
    elif category == "Weight":
        return normal_convert(weight, from_unit, to_unit, value)
    elif category == "Volume":
        return normal_convert(volume, from_unit, to_unit, value)
    elif category == "Storage":
        return normal_convert(storage, from_unit, to_unit, value)
    elif category == "Time":
        return normal_convert(time, from_unit, to_unit, value)
    elif category == "Speed":
        return normal_convert(speed, from_unit, to_unit, value)
    elif category == "Currency":
        return normal_convert(currency, from_unit, to_unit, value)
    elif category == "Temperature":
        return temperature(from_unit, to_unit, value)
    raise Exception("Invalid category.")
```

This is a **router**. It receives the category name as a string and dispatches to the correct table or function. If the category is unknown, it raises an `Invalid category` exception.

---

### 10.2 `app.py` — The Flask Web Server

This is the web layer that connects the browser to the conversion engine.

```python
from flask import Flask, render_template, request, jsonify
from conversions import convert

app = Flask(__name__)
```

- Import the Flask tools needed.
- Import the `convert()` function from our engine.
- Create the Flask application instance.

#### The homepage route

```python
@app.route("/")
def home():
    return render_template("index.html")
```

When a user visits the root URL (`/`), Flask renders the `index.html` template and returns it to the browser. This is the page the user interacts with.

#### The conversion API endpoint

```python
@app.route("/convert", methods=["POST"])
def converter():
    data = request.get_json()
```

This route accepts **POST** requests at `/convert`. It reads the incoming JSON body sent by JavaScript, containing `category`, `from`, `to`, and `value`.

```python
    category = data.get("category")
    from_unit = data.get("from")
    to_unit = data.get("to")
    value = data.get("value")
```

Each piece of data is extracted from the JSON payload.

```python
    try:
        value = float(value)
    except (ValueError, TypeError):
        return jsonify({
            "success": False,
            "message": "Please enter a valid number."
        })
```

The input value is converted to a **float**. If it cannot be converted (empty, text, etc.), the API returns a JSON error message telling the user to enter a valid number.

```python
    try:
        result = convert(category, from_unit, to_unit, value)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })
```

The `convert()` engine is called. On success, its numeric result is returned in a JSON object with `"success": True`. If any exception occurs (e.g., invalid category, unsupported temperature), it is caught and converted into a JSON error message with the exception's text.

```python
if __name__ == "__main__":
    app.run(debug=True)
```

This runs the server in **debug mode** (with auto-reload on code changes) when the script is executed directly.

---

### 10.3 `requirements.txt`

```
Flask
```

This simply declares that the project depends on **Flask**, which is installed via `pip install -r requirements.txt`.

---

### 10.4 `templates/index.html` — The Frontend Structure

This is a Flask **Jinja2 template**. It defines the page layout and also contains an inline JavaScript object listing all units.

#### `<head>` section

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

- The `{{ url_for('static', filename='style.css') }}` Jinja expression generates the correct URL for the CSS file stored in the `static/` folder.
- The Google Fonts link loads the **Poppins** font family used throughout the design.

#### Body structure

The page consists of a `container` → `card`. Inside the card:

1. **Title & subtitle** — the page heading.
2. **Category select** — a dropdown `#category` listing all 8 categories.
3. **Value input** — a number field `#value`.
4. **From select** — `#fromUnit`, populated dynamically by JavaScript.
5. **Swap button** — `#swapBtn`.
6. **To select** — `#toUnit`, also populated dynamically.
7. **Convert button** — `#convertBtn`.
8. **Result box** — `#result`, where the answer (or error) is shown.
9. **Copy button** — `#copyBtn`.
10. **History panel** — a `#historyList` unordered list for recent conversions.

#### The inline unit data script

```html
<script>
const units = {
Length: ["Meter","Kilometer","Centimeter","Millimeter","Foot","Inch","Yard","Mile"],
Weight: ["Kilogram","Gram","Milligram","Pound","Ounce","Ton"],
Temperature: ["Celsius","Fahrenheit","Kelvin"],
Volume: ["Liter","Milliliter","Gallon","Cup"],
Storage: ["Byte","KB","MB","GB","TB"],
Time: ["Second","Minute","Hour","Day"],
Speed: ["m/s","km/h","mph"],
Currency: ["USD","NPR","EUR","GBP"]
};
</script>
```

This JavaScript object maps **each category** to its **list of units**. The `units` keys must match the category names used elsewhere exactly.

```javascript
const category = document.getElementById("category");
const from = document.getElementById("fromUnit");
const to = document.getElementById("toUnit");

function loadUnits(){
    const list = units[category.value];
    from.innerHTML = "";
    to.innerHTML = "";

    list.forEach(unit => {
        let o1 = document.createElement("option");
        o1.text = unit;
        from.appendChild(o1);

        let o2 = document.createElement("option");
        o2.text = unit;
        to.appendChild(o2);
    });

    if (list.length > 1)
        to.selectedIndex = 1;
}

category.addEventListener("change", loadUnits);
loadUnits();
```

- The three relevant elements are grabbed.
- `loadUnits()` reads the selected category, clears both dropdowns, and repopulates them with `<option>` elements for each unit.
- It defaults the "To" dropdown to the second unit (if more than one exists).
- The function runs when the category changes **and** once on page load.

Finally, the external interaction script is loaded:

```html
<script src="{{ url_for('static', filename='script.js') }}"></script>
```

---

### 10.5 `static/style.css` — Styling & Theme

This stylesheet implements a modern **dark glassmorphism** design.

#### Global reset

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}
```

Resets default browser spacing and sets the Poppins font everywhere.

#### Body & background

```css
body {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #0f172a, #1e293b, #2563eb);
    padding: 40px;
}
```

Centers content and applies a three-color diagonal gradient background (dark blue tones).

#### The card

```css
.card {
    width: 100%;
    max-width: 600px;
    background: rgba(255, 255, 255, .08);
    backdrop-filter: blur(18px);
    border-radius: 25px;
    padding: 40px;
    border: 1px solid rgba(255, 255, 255, .15);
    box-shadow: 0 25px 50px rgba(0, 0, 0, .35);
}
```

Creates the frosted-glass card effect using a semi-transparent white background, `backdrop-filter` blur, rounded corners, a subtle border, and a soft drop shadow.

#### Form controls

```css
select, input {
    padding: 15px;
    border: none;
    outline: none;
    border-radius: 12px;
    font-size: 16px;
    background: white;
    transition: .3s;
}

input:focus, select:focus {
    transform: scale(1.02);
    box-shadow: 0 0 15px rgba(37, 99, 235, .5);
}
```

Styles dropdowns and inputs as rounded white fields with a smooth focus animation (subtle scale + blue glow).

#### Buttons

```css
.convert {
    width: 100%;
    padding: 15px;
    border: none;
    border-radius: 12px;
    background: #2563eb;
    color: white;
    font-size: 18px;
    cursor: pointer;
    transition: .3s;
    margin-top: 10px;
}
.convert:hover { background: #1d4ed8; transform: translateY(-2px); }
```

The main Convert button is blue, full-width, and lifts slightly on hover. The swap and copy buttons use accent colors (`#0ea5e9` and `#16a34a` respectively).

#### Result box

```css
.result {
    margin-top: 30px;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    background: #111827;
    color: #22c55e;
    min-height: 70px;
}
```

Displays the answer in bold green text on a dark panel. The `min-height` reserves space so the layout doesn't jump when a result appears (or an error is shown).

#### History

```css
.history li {
    background: rgba(255, 255, 255, .08);
    color: white;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    word-break: break-word;
}
```

Recent conversions are shown as subtle white rounded list items.

#### Responsive media query

```css
@media (max-width: 700px) {
    .card { padding: 25px; }
    h1 { font-size: 28px; }
    .result { font-size: 18px; }
    .convert { font-size: 16px; }
}
```

On small screens (≤700px), padding and font sizes shrink to fit mobile viewports.

---

### 10.6 `static/script.js` — Frontend Interactivity

This file handles all user actions and communication with the backend.

#### Element references

```javascript
const valueInput = document.getElementById("value");
const convertBtn = document.getElementById("convertBtn");
const resultBox = document.getElementById("result");
const historyList = document.getElementById("historyList");
const copyBtn = document.getElementById("copyBtn");
const swapBtn = document.getElementById("swapBtn");
```

It grabs references to all interactive elements. Note: `category`, `from`, and `to` are already defined in the inline script in `index.html`, so they are available globally here.

#### The Convert handler

```javascript
convertBtn.addEventListener("click", convert);

async function convert() {
    const value = valueInput.value.trim();

    if (value === "") {
        alert("Please enter a value.");
        return;
    }
```

The Convert button is wired to the `convert()` async function. It first checks if the value field is empty and alerts the user if so.

```javascript
    const data = {
        category: category.value,
        from: from.value,
        to: to.value,
        value: value
    };

    try {
        const response = await fetch("/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
```

The user's selections and value are packaged into a JSON object and sent to the Flask `/convert` endpoint via a `fetch` **POST** request. The response is parsed as JSON.

```javascript
        if (!result.success) {
            resultBox.innerHTML = result.message;
            return;
        }

        const text = `${value} ${from.value} = ${result.result} ${to.value}`;
        resultBox.innerHTML = text;
        addHistory(text);
    } catch (err) {
        resultBox.innerHTML = "Unable to connect to server.";
    }
}
```

- If the server reports an error, the message is shown in the result box.
- Otherwise, a formatted string (e.g., `50 Meter = 0.05 Kilometer`) is displayed and added to history.
- If the network request itself fails, a friendly connection-error message is shown.

#### Swap functionality

```javascript
swapBtn.addEventListener("click", () => {
    let temp = from.value;
    from.value = to.value;
    to.value = temp;
});
```

Clicking **Swap** exchanges the values of the From and To dropdowns, making it easy to reverse a conversion.

#### Copy to clipboard

```javascript
copyBtn.addEventListener("click", async () => {
    if (resultBox.innerText === "Result will appear here")
        return;

    try {
        await navigator.clipboard.writeText(resultBox.innerText);
        copyBtn.innerHTML = "Copied ✓";
        setTimeout(() => { copyBtn.innerHTML = "Copy Result"; }, 1500);
    } catch {
        alert("Copy failed.");
    }
});
```

- Ignores the action if no result exists yet.
- Uses the Clipboard API to copy the current result text.
- Temporarily changes the button label to "Copied ✓" for 1.5 seconds.
- Alerts if copying fails.

#### History management

```javascript
function addHistory(item) {
    history.unshift(item);
    if (history.length > 10)
        history.pop();

    historyList.innerHTML = "";

    history.forEach(entry => {
        let li = document.createElement("li");
        li.innerHTML = entry;
        historyList.appendChild(li);
    });
}
```

- New conversions are added to the **front** of the `history` array.
- The list is capped at **10 entries** — older ones are removed from the end.
- The `#historyList` is cleared and rebuilt, prepending each item as a new `<li>`.

#### Enter key support

```javascript
valueInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter")
        convert();
});
```

Pressing **Enter** while focused on the value input triggers the conversion, matching the Convert button behavior.

---

## 11. How Everything Fits Together (Flow Summary)

1. The page loads → `loadUnits()` fills the From/To dropdowns for the default category.
2. The user picks a category → dropdowns refresh.
3. The user enters a value and clicks Convert (or presses Enter).
4. `script.js` sends a JSON POST to `/convert`.
5. `app.py` validates the value, then calls `convert()` in `conversions.py`.
6. `conversions.py` looks up the correct table/formula and returns a number.
7. `app.py` returns JSON (`{"success": true, "result": ...}`).
8. `script.js` displays the formatted result and adds it to history.
9. The user can Swap units, Copy the result, or keep converting.

---

## 12. Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository.
2. **Create a feature branch** (`git checkout -b feature/my-feature`).
3. **Commit your changes** with clear messages.
4. **Push** to the branch.
5. **Open a Pull Request** describing your changes.

### Ideas for improvement
- Connect **Currency** rates to a live API for up-to-date exchange values.
- Persist history with **localStorage** or a database.
- Add more categories/units (Area, Pressure, Energy, etc.).
- Write unit tests for the conversion engine.
- Add a dark/light theme toggle.

---

## 13. License

This project is provided for **educational purposes** and is free to use. If you intend to distribute it, consider applying an open-source license such as the **MIT License**. *(Update this section once you decide on a license.)*

---

## 14. Reference / Credits

- **Flask** – The Python web framework used for the backend and API.
- **Poppins** (Google Fonts) – The typeface used in the interface.
- **MDN Web Docs** – For the Fetch API and Clipboard API patterns.
- Author: **#Bishal Lamichhane
#Arpit Kharel
#Dipak Yadav
#Bibek Shahi**

