##### Project Development Guidelines:
## Versioning and workflow

This project uses [Github](https://github.com/) for versioning. The project repository is located [here](#)

I suggest reading the git-workflow.md in the root directory. (credits to [blackfalcon](https://gist.github.com/blackfalcon) for creating this helpful guide!)

## Integrating front-end to back-end

**All** static files (css, js, images) always be imported. Other than that, integrate *only* the final UI templates. This is to ensure that there will be minimal changes when a template has been integrated with a working back-end.


Updated Front-end files are located in a different [repository](https://github.com/chynnasevilleno/SAD-Enrollment).


## Development of back-end

**will be specified further in the future**


## File Structure

```
main
│   README.md *Project details
│   Guidelines.md *For this project's developers
│   git-workflow.md *A small workflow convention when developing with git
│   
│   manage.py
│
│
└───administrative *project app for the administrative module
│
└───cashier *project app for the cashier module
│
└───enrollment *project app for the enrollment module
└───front-end *templates directory for account management (login, logout, etc)
│   └───templates
│       │
│       │   base.html *Static files imports are located here (CSS, Bootstrap, JS, etc)
│       │ 
│       └───administrative *for the 'administrative' app
│       └───cashier *for the 'cashier' app
│       └───enrollment *for the 'enrollment' app
│       └───registrar *for the 'registration' app
│       └───registration *this is for account authentication, the names clashed (see directory before this), so i changed the other to registrar
│    
└───main *this is where the project settings.py is located, and other configuration
│   │   urls.py *set up url mapping of the website
│   │   settings.py *various settings (like database set-up, middlewares, apps, etc.)
│   
└───static *contains static files for the templates (CSS, Images, JS, fonts)
```