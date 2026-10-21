import os
import sys
import subprocess

def convert_to_pdf(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    # Handle Jupyter Notebook
    if file_path.endswith(".ipynb"):
        print("📒 Converting Jupyter Notebook to PDF...")
        try:
            subprocess.run([
                "jupyter", "nbconvert", "--to", "pdf", file_path
            ], check=True)
            print("✅ Notebook converted successfully!")
        except subprocess.CalledProcessError:
            print("⚠️ Conversion failed. Make sure LaTeX is installed.")

    # Handle Python script
    elif file_path.endswith(".py"):
        print("🐍 Converting Python script to PDF...")
        try:
            # First convert to HTML using pygments
            html_file = file_path.replace(".py", ".html")
            pdf_file = file_path.replace(".py", ".pdf")

            subprocess.run([
                "pygmentize", "-f", "html", "-O", "full", "-o", html_file, file_path
            ], check=True)

            # Convert HTML to PDF using wkhtmltopdf
            subprocess.run([
                "wkhtmltopdf", html_file, pdf_file
            ], check=True)

            print(f"✅ Script converted successfully! Saved as {pdf_file}")
        except subprocess.CalledProcessError:
            print("⚠️ Conversion failed. Ensure pygments and wkhtmltopdf are installed.")

    else:
        print("❌ Unsupported file type. Use .py or .ipynb")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_pdf.py <file_path>")
    else:
        convert_to_pdf(sys.argv[1])
