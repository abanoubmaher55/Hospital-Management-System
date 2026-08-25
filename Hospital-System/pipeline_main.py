"""
Main Execution Pipeline for Hospital Management System.
"""
from cli import HospitalCLI

def main():
    app = HospitalCLI()
    app.run()

if __name__ == "__main__":
    main()