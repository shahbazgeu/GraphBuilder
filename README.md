# GraphBuilder
Build graphs based on the daily data pull and push timings

***************************************************************************************************************************************************

How to Use the UI

	1.	Select Type
		•	Data Pull
		•	Data Push
	2.	Enter:
		•	Hour (0–23)
		•	Start minute (0, 20, 40…)
		•	Duration (minutes)
	3.	For Data Pull, enter Network Name
	4.	Click “Add Job”

📊 The chart updates instantly.

***************************************************************************************************************************************************

1. ✏️ Edit / Delete Jobs

What’s implemented

	•	Every job appears in a table
	•	✏️ Edit → loads the job back into the form
	•	🗑 Delete → removes it instantly
	•	Chart updates in real time

How it works

	•	Jobs are stored in a jobs[] array
	•	Edit uses an editIndex
	•	Delete uses splice()

***************************************************************************************************************************************************

2. 📅 Real Timestamps (UTC / IST Toggle)

What’s implemented

	•	Dropdown: UTC / IST
	•	Chart shifts hours dynamically

The toggle:

	•	Changes only the visualization
	•	Keeps raw data in UTC (best practice for data systems)

***************************************************************************************************************************************************

3. 📤 Export Config as JSON

What’s implemented

	•	One click → downloads data_jobs.json
  
Example output:

```json
[
  {
    "type": "pull",
    "hour": 2,
    "start": 0,
    "duration": 40,
    "network": "Facebook"
  }
]
```

This file is:

	•	Backend-ready
	•	API-ready
	•	Version-controllable

***************************************************************************************************************************************************

5. 🐍 Connect to Python (Flask / FastAPI)

Now let’s wire this UI to Python.

⸻

🔹 Backend Option A: Flask (Beginner-friendly)

1️⃣ Flask API (server.py)

```python
from flask import Flask, request, jsonify
app = Flask(__name__)
jobs = []
@app.route("/jobs", methods=["GET"])
def get_jobs():
    return jsonify(jobs)
@app.route("/jobs", methods=["POST"])
def save_jobs():
    global jobs
    jobs = request.json
    return {"status": "saved"}
if __name__ == "__main__":
    app.run(debug=True)
```

Run:

```python
bash

pip install flask
python server.py`
```

2️⃣ Connect HTML to Flask

Replace exportJSON() with:

*/
fetch("http://localhost:5000/jobs", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(jobs)
});
/*

Now your UI:

	•	Saves to Python
	•	Python can push to DB / logs / pipelines
