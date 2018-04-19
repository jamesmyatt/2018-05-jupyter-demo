# jupyter-demo

Demo of Python data science using Jupyter

* [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jamesmyatt/jupyter-demo/master) (notebook)
* [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jamesmyatt/jupyter-demo/master?urlpath=lab) (lab)

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── environment.yml    <- The conda environment file for reproducing the analysis environment, e.g.
    │                         generated with `conda env export -n jupyter-demo > environment.yml`
    ├── tasks.py           <- Invoke tasks definitions
    ├── postBuild          <- Binder post-build install script
    │
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── decisions          <- Lightweight decision records, for both architecture and analysis. See 
    |                         http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.

## Third-party examples

1. Jake VanderPlas, [Reproducible Data Analysis in Jupyter](https://github.com/jakevdp/JupyterWorkflow)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
