# Import libraries
import ast
import re
import io
import contextlib
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model class for checking student code
class StudentCompetenceModel:
    def __init__(self, model_name="Salesforce/codet5-small"):
        print("Loading model...")

        # load the tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#short summary for the code
    def summarize_code(self, code: str) -> str:
        inputs = self.tokenizer("Summarize this Python code: " + code,
                                return_tensors="pt", truncation=True)
        outputs = self.model.generate(**inputs, max_length=80)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

#find common mistakes
    def detect_common_errors(self, code: str) -> list:
        errors = []
        # check syntax
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append(f"Syntax Error: {e.msg} at line {e.lineno}")
            return errors

        # Check for mistakes
        if re.search(r"\bif\s+.*=", code) and "==" not in code:
            errors.append("Used '=' instead of '==' in if condition.")
        if "while True" in code:
            errors.append("Possible infinite loop with 'while True'.")
        if "print" not in code:
            errors.append("No print statement found. Might not show output.")
        return errors

#ask reflective question
    def reflective_prompt(self, errors: list) -> str:
        if not errors:
            return "How could this code be improved for efficiency or readability?"
        if any("==" in e or "=" in e for e in errors):
            return "What is the difference between '=' and '==' in Python logic?"
        if any("infinite loop" in e for e in errors):
            return "What conditions should be added to stop this loop?"
        if any("Syntax Error" in e for e in errors):
            return "How does Python tell you where syntax errors occur?"
        return "Why does the error occur, and how would fixing it change the output?"

#simple scoring system
    def competence_score(self, errors: list) -> tuple:
        if not errors:
            return 10, "Expert"
        elif len(errors) == 1:
            return 7, "Advanced"
        elif len(errors) == 2:
            return 5, "Intermediate"
        else:
            return 2, "Beginner"

# run code safely and capture output
    def run_code_safely(self, code: str) -> str:
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                exec(code, {})  # run code in isolated namespace
            return output.getvalue().strip()
        except Exception as e:
            return f"Runtime Error: {e}"

#full analysis
    def analyze_code(self, code: str):
        summary = self.summarize_code(code)
        errors = self.detect_common_errors(code)
        reflection = self.reflective_prompt(errors)
        score, level = self.competence_score(errors)

        print("\n---Student Competence Analysis---")
        print("\nCode Summary:", summary)
        if errors:
            print("Detected Errors:")
            for e in errors:
                print(" -", e)
        else:
            print("No errors found.")
            output = self.run_code_safely(code)
            print("Program Output:", output if output else "No visible output")
        print(f"Competence Score: {score} ({level}) - based on {len(errors)} error(s).")
        print("Reflective Prompt:", reflection)


# eg 1: wrong code with error (= instead of ==)
student_code_error = """
for i in range(1,10):
    if i = 5:         # mistake
        print("Five")
"""

# eg 2: correct code
student_code_correct = """
for i in range(1,6):
    if i == 3:
        print("Three")
"""

# Run model on both codes
model = StudentCompetenceModel()
print("\n 1.Error Case:")
model.analyze_code(student_code_error)

print("\n 2.Correct Case:")
model.analyze_code(student_code_correct)
