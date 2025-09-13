# Student Competence Analysis using Open Source Models

This repository is my submission for **Python Screening Task 3: Evaluating Open Source Models for Student Competence Analysis**.  
The project uses **Salesforce/CodeT5-small**, an open-source code model, combined with rule-based methods to analyze student Python programs, detect errors, and generate reflective prompts that encourage deeper learning.
For detailed installation and running instructions, see SETUP.md

Author Information
Name: Anuja Rawat
College: VIT Bhopal University
Email: anuja.23bhi10158@vitbhopal.ac.in
GitHub: https://github.com/enuje12

---

## Research Plan

My approach to this evaluation was to identify open-source models that could analyze Python code and support student learning without directly providing solutions. I chose **Salesforce/CodeT5-small** from Hugging Face because it is free, lightweight, and trained specifically for code understanding. To complement the model, I added Python’s **ast** and **re** libraries for detecting syntax issues, common mistakes (like using `=` instead of `==`), and potential infinite loops. Together, this creates a hybrid approach that balances AI-driven insights with reliable rule-based detection.  

To evaluate model suitability, I tested it on both correct and incorrect student-written Python code. The main criteria were:  
1. Ability to summarize code meaningfully  
2. Ability to detect errors or misconceptions  
3. Generation of reflective prompts that encourage reasoning  
4. Practicality of using the model locally  

While CodeT5 shows promise in summarizing and interpreting code, its limitations include shallow conceptual understanding compared to larger models. However, when combined with simple rule-based methods, it becomes useful for competence analysis.

---

## Reasoning

**1. What makes a model suitable for high-level competence analysis?**  
> A suitable model should understand student intent, highlight errors or misconceptions, and provide feedback that supports reasoning rather than giving direct solutions.  

**2. How would you test whether a model generates meaningful prompts?**  
> I tested prompts by checking whether they guided reflection (e.g., asking the difference between `=` and `==`) instead of simply fixing the mistake.  

**3. What trade-offs might exist between accuracy, interpretability, and cost?**  
> Larger models may provide more accurate insights but are costly and harder to run locally. Smaller models like CodeT5 are cheaper and interpretable, but may not fully capture deeper conceptual misunderstandings.  

**4. Why did you choose the model you evaluated, and what are its strengths or limitations?**  
> I chose CodeT5-small because it is free, trained for code tasks, and easy to integrate. Its strength is code summarization and lightweight usability, while its limitation is that it cannot always explain deeper reasoning as effectively as larger models.  

---

## References

- [Salesforce CodeT5 Model (Hugging Face)](https://huggingface.co/Salesforce/codet5-small)  
- [AST Documentation (Python Official)](https://docs.python.org/3/library/ast.html)  
- [Regular Expressions in Python](https://docs.python.org/3/library/re.html)  

---

## Sample Output

### 1. Error Case (= instead of ==)

---Student Competence Analysis--- <br>
Code Summary: loop through numbers and check condition <br>
Detected Errors: <br>
 - Used '=' instead of '==' in if condition. <br>
Competence Score: 5 (Intermediate) - based on 1 error(s). <br>
Reflective Prompt: What is the difference between '=' and '==' in Python logic? <br>

### 2. Correct Case

---Student Competence Analysis--- <br>
Code Summary: loop from 1 to 5 and print when number equals 3 <br>
No errors found. <br>
Program Output: Three <br>
Competence Score: 10 (Expert) - based on 0 error(s). <br>
Reflective Prompt: How could this code be improved for efficiency or readability? <br>

