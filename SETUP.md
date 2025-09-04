# Setup Instructions

Follow these steps to set up and run the Student Competence Analysis project locally.

---

## 1. Clone the Repository
```bash
git clone https://github.com/enuje12/Student-Competence-Analysis.git
cd student-competence-analysis
```

## 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```
On Linux/Mac
```bash
source venv/bin/activate  
```
On Windows
```bash
venv\Scripts\activate  
```

## 3. Install Dependencies

All required packages are listed in requirements.txt.

```bash
pip install -r requirements.txt
```

If you don’t have requirements.txt, install directly:

```bash
pip install transformers torch
```

## 4. Run the Code

Run the Python script with:

```bash
python student_competence_model.py
```
