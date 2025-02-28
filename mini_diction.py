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
            "release": "A packaged version of your project, often including compiled binaries and documentation.",
            "milestone": "A collection of issues and pull requests associated with a goal or project phase.",
            "webhook": "A way to notify external services about events in a GitHub repository.",
            "starring": "A way to mark repositories as favorites.",
            "collaborator": "Someone with permissions to contribute to a repository.",
        }
    
    def lookup(self, term):
        return self.terms.get(term.lower(), "Term not found in dictionary.")

    def add_term(self, term, definition):
        self.terms[term.lower()] = definition
        return f"Added: {term} -> {definition}"

    def remove_term(self, term):
        if term.lower() in self.terms:
            del self.terms[term.lower()]
            return f"Removed: {term}"
        return "Term not found in dictionary."

    def list_terms(self):
        return "\n".join(sorted(self.terms.keys()))

# Example Usage
dictionary = GitHubDictionary()
print(dictionary.lookup("fork"))  
print(dictionary.add_term("tag", "A label that marks specific points in repository history."))
print(dictionary.remove_term("gist"))  
print(dictionary.list_terms())  
