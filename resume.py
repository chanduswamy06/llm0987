"""Simple Python script that prints a resume"""

# TODO: python resume

def main():
    resume = {
        "name": "John Doe",
        "summary": "Experienced Python developer with expertise in full stack web development and automation.",
        "skills": ["Python", "Django", "Flask", "SQL", "Git"],
        "experience": [
            {
                "company": "TechCorp",
                "title": "Senior Python Developer",
                "years": "2018-2023"
            }
        ],
        "education": "B.Sc. in Computer Science"
    }

    for key, value in resume.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
