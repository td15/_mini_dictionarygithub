const readline = require("readline");

class GitHubDictionary {
    constructor() {
        this.terms = {
            "repo": "A storage space for your project's code, issues, and discussions.",
            "fork": "A copy of a repository to freely experiment with.",
            "pull request": "A way to propose changes to a repository.",
            "commit": "A saved change in a repository.",
            "branch": "A parallel version of a repository for separate development.",
            "merge": "Combining changes from one branch to another.",
            "workflow": "A set of automated processes in GitHub Actions.",
        };
    }

    lookup(term) {
        return this.terms[term.toLowerCase()] || "Term not found in dictionary.";
    }

    addTerm(term, definition) {
        this.terms[term.toLowerCase()] = definition;
        return `Added: ${term} -> ${definition}`;
    }

    removeTerm(term) {
        if (this.terms[term.toLowerCase()]) {
            delete this.terms[term.toLowerCase()];
            return `Removed: ${term}`;
        }
        return "Term not found in dictionary.";
    }

    listTerms() {
        return Object.keys(this.terms).sort().join("\n");
    }
}

// CLI Interface
const dict = new GitHubDictionary();
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function showMenu() {
    console.log("\nGitHub Dictionary");
    console.log("1. Look up a term");
    console.log("2. Add a term");
    console.log("3. Remove a term");
    console.log("4. List all terms");
    console.log("5. Exit");
    rl.question("Choose an option: ", (choice) => {
        if (choice === "1") {
            rl.question("Enter term: ", (term) => {
                console.log(dict.lookup(term));
                showMenu();
            });
        } else if (choice === "2") {
            rl.question("Enter term: ", (term) => {
                rl.question("Enter definition: ", (definition) => {
                    console.log(dict.addTerm(term, definition));
                    showMenu();
                });
            });
        } else if (choice === "3") {
            rl.question("Enter term to remove: ", (term) => {
                console.log(dict.removeTerm(term));
                showMenu();
            });
        } else if (choice === "4") {
            console.log("GitHub Terms:\n" + dict.listTerms());
            showMenu();
        } else if (choice === "5") {
            console.log("Goodbye!");
            rl.close();
        } else {
            console.log("Invalid choice. Try again.");
            showMenu();
        }
    });
}

showMenu();
