class GitHubDictionary:
    def __init__(self):
        self.terms = {
            "repo": "Short for repository, a storage space for your project's code, issues, and discussions.",
            "fork": "A copy of a repository that allows you to freely experiment without affecting the original project.",
            "pull request": "A way to propose changes to a repository. Maintainers can review and merge these changes.",
            "commit": "A saved change to a file or set of files within a repository.",
            "branch": "A parallel version of a repository, used to work on features separately from the main branch.",
            "merge": "Combining changes from one branch into another.",
            "issue": "A way to track work, report bugs, or discuss topics related to a repository.",
            "clone": "A local copy of a remote repository, created using 'git clone'.",
            "gist": "A simple way to share snippets of code or text files.",
            "workflow": "A set of automated processes defined in GitHub Actions.",
            "CI/CD": "Continuous Integration/Continuous Deployment - automating testing and deployment.",
            "action": "A reusable script used in GitHub Actions to automate workflows.",
        }
    
    def lookup(self, term):
        return self.terms.get(term.lower(), "Term not found in dictionary.")

# Example Usage
dictionary = GitHubDictionary()
print(dictionary.lookup("fork"))  # Outputs explanation for 'fork'
