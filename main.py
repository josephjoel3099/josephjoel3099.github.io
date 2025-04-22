"""
@mainpage Joseph Joel Portfolio
@brief Auto-generated resume using Doxygen and Python code structure.
"""

import yaml

# Load YAML configuration
def load_resume_config(file_path):
    """
    @brief Load the YAML configuration file.
    @param file_path Path to the YAML file.
    @return Parsed YAML data as a dictionary.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Define functions for each main heading in the YAML
def experience_section(data):
    """
    @brief Process and display the experience section.
    @param data Experience data from the YAML file.
    """
    print("Experience:")
    for item in data:
        print(f"- {item['title']} at {item['company']} ({item['years']})")

def education_section(data):
    """
    @brief Process and display the education section.
    @param data Education data from the YAML file.
    """
    print("Education:")
    for item in data:
        print(f"- {item['degree']} from {item['institution']} ({item['years']})")

def projects_section(data):
    """
    @brief Process and display the projects section.
    @param data Projects data from the YAML file.
    """
    print("Projects:")
    for item in data:
        print(f"- {item['name']}: {item['description']}")

def main():
    """
    @brief This is the entry point to the Doxygen-based portfolio.
    """
    # Load the YAML file
    resume_data = load_resume_config("config/resume.yaml")

    # Call functions for each section
    if 'experience' in resume_data:
        experience_section(resume_data['experience'])
    if 'education' in resume_data:
        education_section(resume_data['education'])
    if 'projects' in resume_data:
        projects_section(resume_data['projects'])

if __name__ == "__main__":
    main()
